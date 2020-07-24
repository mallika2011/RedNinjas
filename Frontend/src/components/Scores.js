import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Button, Container, Col, Row, Table } from "react-bootstrap";
// import axios from 'axios';
import "@fortawesome/fontawesome-free/css/all.min.css";
import "bootstrap-css-only/css/bootstrap.min.css";
import "mdbreact/dist/css/mdb.css";
import styles from "../static/css/scores.module.css";
import common from "../static/css/Common.module.css";

export default class Scores extends Component {
  constructor(props) {
    super(props);
    this.state = {
      scores: []
    }
  }

  componentDidMount() {
    let oldScores = JSON.parse(localStorage.getItem('scores')) || [];
    this.setState({
      scores: oldScores
    })
  }

  render() {
    return (
      <div className={styles.landingBody}>
        <Container className={styles.content}>
          <h1 className={styles.heading}>Previous Scores</h1>
          {this.state.scores.length == 0
            ? 'You have played no games yet!'
            :

            <Table striped bordered hover className={styles.table}>
              <thead>
                <tr >
                  <th className={styles.topics}>#</th>
                  <th className={styles.topics}>GAME TYPE</th>
                  <th className={styles.topics}>LEVEL</th>
                  <th className={styles.topics}>RESULT</th>
                </tr>
              </thead>
              <tbody>
                {
                  this.state.scores.map((score, i) =>
                    <tr className={styles.row}>
                      <td>{i + 1}</td>
                      <td>{score.game}</td>
                      <td>{score.depth == -1 ? 5 : score.depth}</td>
                      <td>{score.winner}</td>
                    </tr>)
                }

              </tbody>
            </Table>
          }
        </Container>
      </div>
    );
  }
}