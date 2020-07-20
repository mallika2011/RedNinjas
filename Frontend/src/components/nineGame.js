import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Button, Container, Col, Row } from "react-bootstrap";

import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import styles from "../static/css/Landing.module.css";
import common from "../static/css/Common.module.css";


import NineBoard from './nineBoard.js'
import NineConfiguration from './nineConfiguration.js'
import GameResults from './gameResults.js'

export default class ThreeGame extends Component {
    constructor(props) {
      super(props);
      this.state = {
          showNineConfigurationComponent : true,
          showNineGameComponent : false,
          showNineWinComponent : false,
          gameBeginner : " ",
          route : " ",
          winner : " "

      }

      this.updateStateOfComponents_Nine = this.updateStateOfComponents_Nine.bind(this);
      this.updateStateForWinComponent = this.updateStateForWinComponent.bind(this);  
      this.handleStartAgent_Nine = this.handleStartAgent_Nine.bind(this);
      this.handleStartHuman_Nine = this.handleStartHuman_Nine.bind(this);
    }
    

    updateStateForWinComponent(gameRoute,gameWinner)
    {
      console.log("Heyyyyy")
      this.setState({
        showNineConfigurationComponent : false,
        showNineGameComponent : false,
        showNineWinComponent : true,
        winner : gameWinner,
        route : gameRoute
      })
    }

    handleStartAgent_Nine(e)
    {
        this.setState({
          gameBeginner : "AGENT"
        })
    }

    handleStartHuman_Nine(e)
    {
      this.setState({
        gameBeginner : "HUMAN"
      })
    }


    updateStateOfComponents_Nine(message)
    {
      if(message === "Go To Game")
      {
        this.setState({
          showNineConfigurationComponent : false,
          showNineGameComponent : true,
          showNineWinComponent : false
        })
      }
      else if(message === "Show Configuration")
      {
        this.setState({
          shownNineConfigurationComponent : true,
          showNineGameComponent : false,
          showNineWinComponent : false,
          gameBeginner : " ",
          route : " ",
          winner : " "
        })
      }
    }

    render() {
      return (
            <div>
                {this.state.showNineConfigurationComponent && <NineConfiguration update_Nine={this.updateStateOfComponents_Nine} handleStartAgent_Nine={this.handleStartAgent_Nine} handleStartHuman_Nine={this.handleStartHuman_Nine} gameBeginner={this.state.gameBeginner}/>}
                {this.state.showNineGameComponent && <NineBoard update_Win_Nine={this.updateStateOfComponents_Nine} gameBeginner = {this.state.gameBeginner}/>}
                {this.state.showNineWinComponent && <GameResults update_Nine={this.updateStateOfComponents_Nine} winner = {this.state.winner} route = {this.state.route}/>}
          </div>
      )}
}