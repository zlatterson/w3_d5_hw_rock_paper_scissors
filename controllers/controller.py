from flask import render_template, request

from app import app
from models.game import *
from models.player import *

import random

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<p1_input>/<p2_input>")
def play_game(p1_input, p2_input, p1_name="Player 1", p2_name="Player 2"):
    print(p1_name)
    player1 = Player(p1_name, p1_input)
    player2 = Player(p2_name, p2_input)

    find_winner = Game.play_rps(player1.choice, player2.choice)

    if find_winner == 1:
        winner = player1.name + " wins"
    elif find_winner == 0:
        winner = player2.name + " wins"
    elif find_winner == 2:
        winner = "Draw"
    else: winner = "Not found"

    return render_template("index.html", title="results", winner=winner)
    
@app.route("/<p1_input>")
def play_vs_computer(p1_input, p1_name="Player 1"):

    human= Player(p1_name, p1_input)

    moves = ["rock","paper","scissors"]
    computer_input = moves[random.randint(0,2)]
    computer = Player("Computer", computer_input)

    find_winner = Game.play_rps(human.choice, computer.choice)

    if find_winner == 1:
        winner = human.name + " wins"
    elif find_winner == 0:
        winner = computer.name + " wins"
    elif find_winner == 2:
        winner = "Draw"
    else: winner = "Not found"

    return render_template("index.html", title="results", winner=winner)

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/play", methods=["POST"])
def play_submit():
    print(request.form.keys())
    if "checkbox_computer" in request.form.keys():
        return play_vs_computer(request.form["player1_move"], request.form["player1_name"])
    return play_game(request.form["player1_move"],request.form["player2_move"],request.form["player1_name"],request.form["player2_name"])