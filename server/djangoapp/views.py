import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from .restapis import get_request, analyze_review_sentiments, post_review


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state

    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchDealer/" + str(dealer_id)
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})

    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = "/fetchReviews/dealer/" + str(dealer_id)
        reviews = get_request(endpoint)

        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])

            if response and 'sentiment' in response:
                review_detail['sentiment'] = response['sentiment']
            else:
                review_detail['sentiment'] = "neutral"

        return JsonResponse({"status": 200, "reviews": reviews})

    return JsonResponse({"status": 400, "message": "Bad Request"})


def get_cars(request):
    cars = get_request("/fetchCars")
    return JsonResponse({"status": 200, "cars": cars})


def add_review(request):
    data = json.loads(request.body)

    try:
        response = post_review(data)
        print(response)
        return JsonResponse({"status": 200})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 401, "message": "Error in posting review"})

    return JsonResponse({"status": 403, "message": "Unauthorized"})


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("userName")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return JsonResponse({
                "status": "Authenticated",
                "userName": username
            })

        return JsonResponse({"status": "Failed"})

    return JsonResponse({"status": "Bad Request"})