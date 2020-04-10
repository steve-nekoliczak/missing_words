import React, { Component } from "react";
import axios from "axios";

class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false
      },
      documentList: []
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/documents/")
      .then(res => this.setState({ documentList: res.data }))
      .catch(err => console.log(err));
  };

  displayCompleted = status => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };

  renderItems = () => {
    const { viewCompleted } = this.state;
    /*
    const newItems = this.state.documentList.filter(
      item => item.completed === viewCompleted
    );
    */
    const items = this.state.documentList;
    return items.map(item => (
      <li
        key={item.id}
      >
        <span>
          {item.author}
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main>
        <h1>Todo app</h1>
        <ul>
          {this.renderItems()}
        </ul>
      </main>
    );
  }

}

export default HomePage;
