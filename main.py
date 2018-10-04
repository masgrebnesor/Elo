games = \
[
    ("Sam", "Connor"), ("Sam", "Connor"), ("Sam", "Connor")
]
players_colors = {"Sam": "CornflowerBlue", "Connor": "gray52"}
players = {}


def calcES(playerArating, playerBrating):
    return 1 / (1 + 10 ** ((playerBrating - playerArating)/400))


for game in games:
    for player in game:
        if player not in players:
            players[player] = 1600
    playerA = game[0]
    playerB = game[1]
    ratingA = players[playerA]
    ratingB = players[playerB]
    AES = calcES(ratingB, ratingA)
    print(AES)
    players[playerA] = ratingA + 32*(AES)
    players[playerB] = ratingB - 32*(AES)

for key,value in players.items():
    print(key + " : " + str(value))

from graphics import *
import random

def draw():
    height = 800
    width = 400
    win = GraphWin('Rankings', width, height) # give title and dimensions
    num = 0
    for player in sorted(players, key=players.__getitem__, reverse=True):
        print(player)
        num += 1
        rect = Rectangle(Point(0, (num - 1)*(height/len(players))), Point(width, num*(height/len(players))))
        rect.setFill(players_colors[player])
        rect.draw(win)
        text = Text(Point(width/2, ((num - 1)*(height/len(players)))+(height/len(players))/2), player + " : " + str(players[player]))
        text.draw(win)

    win.getMouse()
    win.close()

draw()










