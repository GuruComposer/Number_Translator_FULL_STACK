import React, { useState, useEffect } from "react";
import "./HomePage.css";
import "bootstrap/dist/css/bootstrap.min.css";
import * as ReactBootStrap from "react-bootstrap";
import { render } from "react-dom";

export default function HomePage(props) {
  const [number, setNumber] = useState("");
  const [english_number, setEnglishNumber] = useState("");
  const [loading, setLoading] = useState(false);
  const [is_post, setIsPost] = useState(false);
  const [is_get, setIsGet] = useState(false);
  const [error, setError] = useState("");
  const [validator_size, setSizeValidator] = useState("");
  const [validator_type, setTypeValidator] = useState("");
  const [validator_IsPositive, setIsPositiveValidator] = useState("");

  const urlParams = new URLSearchParams(window.location.search);
  const get_number = urlParams.get("number");
  if (get_number != null) {
    console.log(get_number);
  }

  useEffect(() => {
    // View the updated number
    validateInputSize(number);
    validateHasLetter(number);
    validateIsPositive(number);
  });

  function validateInputSize(number) {
    number.toString().length > 13
      ? setSizeValidator("Number is too large.")
      : setSizeValidator("");
  }

  function validateHasLetter(number) {
    var regExp = /[a-zA-Z]/g;
    regExp.test(number)
      ? setTypeValidator("No letters allowed.")
      : setTypeValidator("");
  }

  function validateIsPositive(number) {
    number.toString()[0] === "-"
      ? setIsPositiveValidator("Please do not submit negative numbers.")
      : setIsPositiveValidator("");
  }

  async function handleClickPost(e) {
    e.preventDefault();
    setError("");
    setIsPost(true);
    setIsGet(false);
    setLoading(true);
    await sleep(5000);
    setLoading(false);
    translateNumberPost();
  }

  function handleClickGet(e) {
    e.preventDefault();
    setIsGet(true);
    setIsPost(false);
    translateNumberGet();
  }

  // POST method
  function translateNumberPost() {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "applicat/json" },
      body: JSON.stringify({
        number: number,
      }),
    };
    fetch("/api/num_to_english", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        {
          data.error ? setError(data.error) : setError("");
        }
        console.log(`setting english_number to ${data.english_number}`);
        setEnglishNumber(data.english_number);
      });
  }

  // GET method
  function translateNumberGet() {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "applicat/json" },
    };
    fetch(`/api/num_to_english?number=${number}`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        {
          data.error ? setError(data.error) : setError("");
        }
        setEnglishNumber(data.num_in_english);
      });
  }

  function sleep(ms) {
    return new Promise((accept) => {
      setTimeout(() => {
        accept();
      }, ms);
    });
  }

  function renderSpinner() {
    return (
      <ReactBootStrap.Spinner
        animation="border"
        variant="primary"
        classaName="english__number__spinner"
      />
    );
  }

  function renderEnglishNumber() {
    return (
      <div>
        <div className="english__number__string">
          {english_number ? <h5>English:</h5> : null}
          {english_number ? english_number : null}
        </div>
      </div>
    );
  }

  return (
    <div className="home">
      <div className="home__container">
        <div className="english__number__container1">
          {is_get ? renderEnglishNumber() : null}
        </div>
        <div className="form__container">
          <div className="form__title">
            {" "}
            <h1>Please enter a number!</h1>
          </div>

          <div className="form__helper__text">
            <p>0 &lt;= n &lt;= 1,000,000,000,000</p>
          </div>
          <form>
            <div class="form-group">
              <input
                class="form-control form-control-lg"
                type="text"
                placeholder="ex: 123456789"
                onChange={(e) => {
                  setNumber(e.target.value);
                }}
              />
              <div className="error__text">
                {validator_size ? validator_size : null}
              </div>
              <div className="error__text">
                {validator_type ? validator_type : null}
              </div>
              <div className="error__text">
                {validator_IsPositive ? validator_IsPositive : null}
              </div>
              <div className="error__text">{error ? error : null}</div>
            </div>
            <div className="button__group">
              <button
                id="postButton"
                className="translate__submitButtonPost"
                onClick={handleClickPost}
              >
                Translate - POST!
              </button>
              <button
                id="getButton"
                className="translate__submitButtonGet"
                onClick={handleClickGet}
              >
                Translate - GET!
              </button>
            </div>
          </form>
        </div>
        <div className="english__number__container2">
          {is_post ? (loading ? renderSpinner() : renderEnglishNumber()) : null}
        </div>
      </div>
    </div>
  );
}
