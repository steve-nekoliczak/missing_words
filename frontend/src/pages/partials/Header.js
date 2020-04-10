import React, { Component } from "react";
import { Link } from "react-router-dom";

class Header extends Component {

  render() {
    return (
      <header>
        <h1>Missing Words</h1>
        <div>
          <p>
            <Link to="/">home</Link>
          </p>
          <p>
            <Link to="/stats">stats</Link>
          </p>
          <p>
            <Link to="/how-to">how-to</Link>
          </p>
          <p>
            <Link to="/upload">upload</Link>
          </p>
        </div>
      </header>
    );
  }

}

export default Header;
