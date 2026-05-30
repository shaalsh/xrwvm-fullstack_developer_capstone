import React, { useState } from "react";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const register = () => {
    const user = {
      userName,
      firstName,
      lastName,
      email,
      password,
    };

    console.log("Register user:", user);
  };

  return (
    <div className="container" style={{ marginTop: "40px" }}>
      <h2>Sign-up</h2>

      <div className="form-group">
        <label>Username</label>
        <input
          type="text"
          className="form-control"
          value={userName}
          onChange={(e) => setUserName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>First Name</label>
        <input
          type="text"
          className="form-control"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Last Name</label>
        <input
          type="text"
          className="form-control"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Email</label>
        <input
          type="email"
          className="form-control"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>

      <div className="form-group">
        <label>Password</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      <button className="btn btn-primary" onClick={register}>
        Register
      </button>
    </div>
  );
};

export default Register;
