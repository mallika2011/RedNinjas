// import logo from './logo.svg';
import React, { Component } from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Landing from "./components/Landing";
import Error from "./components/Error";
import { Navbar, Nav} from "react-bootstrap";
import Overview from "./components/Overview";
import Rules from "./components/Rules";
import Message from "./components/Message";
import ThreeGame from "./components/threeGame";
import NineGame from "./components/nineGame";
import Scores from "./components/Scores";
import "bootstrap/dist/css/bootstrap.min.css";

class NavigationBar extends Component {
  constructor(props) {
    super(props);

    this.listener = null;
    this.state = {
      status: "top",
    };
  }

  componentDidMount() {
    this.listener = document.addEventListener("scroll", (e) => {
      var scrolled = document.scrollingElement.scrollTop;
      if (scrolled >= 120) {
        if (this.state.status !== "nav") {
          this.setState({ status: "nav" });
        }
      } else {
        if (this.state.status !== "top") {
          this.setState({ status: "top" });
        }
      }
    });
  }
  componentDidUpdate() {
    document.removeEventListener("scroll", this.listener);
  }
  render() {
    return (
      <Navbar expand="lg" style={navstyles} variant="dark">
        <Navbar.Brand href="/">Red Ninjas</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/three">3x3</Nav.Link>
            <Nav.Link href="/nine">9x9</Nav.Link>
            <Nav.Link href="/rules">Rule Book</Nav.Link>
            <Nav.Link href="/overview">About</Nav.Link>
            <Nav.Link href="/scores">Past Scores</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={Landing} />
          <Route exact path="/three" component={ThreeGame} />
          <Route exact path="/nine" component={NineGame} />

          {/* <Route exact path='/win_player_three' component={WinHumanThree} /> */}
          {/* <Route exact path='/lose_player_three' component={WinAgentThree} /> */}

          {/* <Route exact path='/win_player_nine' component={WinHumanNine} /> */}
          {/* <Route exact path='/lose_player_nine' component={WinAgentNine} /> */}
          {/* <Route exact path='/config' component={Config} /> */}
          {/* <Route exact path='/Result' component={Result} /> */}
          <Route exact path="/overview" component={Overview} />
          <Route exact path="/rules" component={Rules} />
          <Route exact path="/message" component={Message} />
          <Route exact path="/scores" component={Scores} />
          <Route path="*" exact={true} component={Error} />
        </Switch>
      </Router>
      <NavigationBar />
    </div>
  );
}

export default App;

const navstyles = {
  backgroundColor: "#3b3251",
  position: "fixed",
  top: "0%",
  overflow: "hidden",
  width: "100%",
  zIndex: "9999999 !important",
};
