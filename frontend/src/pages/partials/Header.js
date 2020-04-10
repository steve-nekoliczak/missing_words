import React, { Component } from "react";
import { Link } from "react-router-dom";

class Header extends Component {

  render() {
    return (
      <nav class='navbar' role='navigation'>
        <h1 class="title is-1">
          Missing Words
        </h1>
        <div class="navbar-menu">
          <div class="navbar-start">
            <Link to="/" class="navbar-item"> home </Link>
          </div>
          <div class="navbar-start">
            <Link to="/stats" class="navbar-item"> stats </Link>
          </div>
          <div class="navbar-start">
            <Link to="/how-to" class="navbar-item"> how-to </Link>
          </div>
          <div class="navbar-start">
            <Link to="/upload" class="navbar-item"> upload </Link>
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>

      </nav>
    );
  }

}

export default Header;
