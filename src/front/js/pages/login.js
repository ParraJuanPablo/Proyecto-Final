import React, { useState, useContext } from "react";
import "../../styles/pages/signup.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Login = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [auth, setAuth] = useState(false);
  const navigate = useNavigate();
  // const token = sessionStorage.getItem("token");
  // console.log("This is your token, token");

  const sendData = async (event) => {
    event.preventDefault();
    const response = await actions.login(email, password);
    if (response) {
      navigate("/");
    } else {
      alert("invalid credentials");
    }
  };
  return (
    <div className="container">
      <div className="row">
        <div className="col-md-3 register">
          <h3>Log In</h3>
          <form onSubmit={sendData}>
            <div className="form-group">
              <label htmlFor="exampleInputEmail1">Email address</label>
              <input
                onChange={(e) => setEmail(e.target.value)}
                value={email}
                type="text"
                className="form-control"
                id="exampleInputEmail1"
                placeholder="Enter email"
              />
            </div>
            <div className="form-group">
              <label htmlFor="exampleInputPassword1">Password</label>
              <input
                onChange={(e) => setPassword(e.target.value)}
                value={password}
                type="password"
                className="form-control"
                id="exampleInputPassword1"
                placeholder="Enter password"
              />
            </div>

            <div className="form-group">
              <div className="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  className="custom-control-input"
                  id="customCheck1"
                />
                <label className="custom-control-label" htmlFor="customCheck1">
                  Remember me
                </label>
              </div>
            </div>

            <button type="submit" className="btn btn-primary btn-block">
              Log In
            </button>

            <div className="d-flex justify-content-between">
              <p className="cancel text-left">
                <a href="/">Cancel</a>
              </p>

              <p className="forgot-password text-right">
                Forgot <a href="forgotpassword">password?</a>
              </p>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};
