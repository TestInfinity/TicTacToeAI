# import modules
import random
import turtle
import time

# Global Variables
player_marker = "X"
bot_marker = "O"
running = True
isPlayerTurn = True
board = {
    0: '', 1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '}

# create objects
layout = turtle.Turtle()
layout.speed(0)

turn_tracker = turtle.Turtle()
turn_tracker.speed(0)
turn_tracker.pu()
turn_tracker.hideturtle()

wn = turtle.Screen()

wn.addshape("O-image_50x50.gif")
wn.addshape("X-image_50x50.gif")

tile_turtles = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

unused_x = []
unused_o = []

used_o = []
used_x = []

# Create X's and O's
wn.tracer(False)
for i in range(10):
    x = turtle.Turtle()
    x.speed(0)
    x.shape("X-image_50x50.gif")
    x.shapesize(2)
    x.penup()
    x.goto(200, 200)
    x.speed(3)

    unused_x.append(x)

    o = turtle.Turtle()
    o.speed(0)
    o.shape("O-image_50x50.gif")
    o.shapesize(2)
    o.penup()
    o.goto(200, 100)
    o.speed(3)

    unused_o.append(o)


# Create turtles for tiles

index = 1
for y in range(3):
    c = 1
    for i in range(3):
        t = turtle.Turtle()
        t.color("white")
        t.speed(0)
        t.penup()
        t.goto(-250, 150 - y * 100)

        t.forward(c * 100)

        t.shape("square")
        t.shapesize(4.5)
        tile_turtles[index] = t
        c += 1
        index += 1

# draw layout
for y in range(100, -1, -100):
    layout.pu()
    layout.goto(-200, y)

    layout.pd()
    layout.forward(300)

layout.seth(90)

for x in range(-100, 100, 100):
    layout.pu()
    layout.goto(x, -100)

    layout.pd()
    layout.forward(300)

layout.hideturtle()
wn.tracer(True)


# Move turtles to proper location


# Functions
def insertLetter(letter, position):
    global running

    if winCheck(board):
        return 0
    if checkDraw():
        return 0
    if board[position] == ' ':
        board[position] = letter
        tile_clicked(tile_turtles[position].xcor(), tile_turtles[position].ycor(), tile_turtles[position], position,
                     letter)

    if winCheck(board):
        return 0
    if checkDraw():
        return 0


def winCheck(board):
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def markerWinCheck(board, mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def tile_clicked(x, y, tile, board_index, marker):
    global isPlayerTurn
    if marker == "X" and isPlayerTurn:
        tile.hideturtle()
        marker = unused_x.pop(0)
        marker.goto(x, y)
        used_x.append(marker)

        board[board_index] = "X"
        isPlayerTurn = False

    elif marker == "O" and not isPlayerTurn:
        tile.hideturtle()
        marker = unused_o.pop(0)
        marker.goto(x, y)
        used_o.append(marker)

        board[board_index] = "O"
        isPlayerTurn = False

    wn.update()


def evaluateBotLocation():
    possible_moves = []

    for key in board.keys():
        if board[key] == ' ':
            possible_moves.append(key)

    # Steals Wins and Blocks
    for i in possible_moves:
        boardCopy = list(board.values())
        boardCopy[i] = bot_marker
        if markerWinCheck(boardCopy, bot_marker):
            return i

    for i in possible_moves:
        boardCopy = list(board.values())
        boardCopy[i] = player_marker
        if markerWinCheck(boardCopy, player_marker):
            return i

    corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
    if len(corners) > 0:
        move = random.choice(corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = random.choice(corners)
        return move

    return 0


def finishGame():
    layout.pu()
    layout.goto(-300, -150)

    if markerWinCheck(board, bot_marker):
        layout.write("Opponent Won Better Luck Next Time", font=('Courier', 30, 'italic'))
    elif markerWinCheck(board, player_marker):
        layout.write("Congratulations You Won", font=('Courier', 30, 'italic'))
    else:
        layout.write("There was a Draw", font=('Courier', 30, 'italic'))

    layout.goto(-300, -210)
    layout.write("Press Q to quit the game")


def stopGame():
    turtle.bye()

turn_tracker.goto(0, 250)
turn_tracker.write("Your turn", font=('Courier', 30, 'italic'))


# Event Management

#Game Loop
while running:
    tile_turtles[1].onclick(
        lambda x, y: tile_clicked(tile_turtles[1].xcor(), tile_turtles[1].ycor(), tile_turtles[1], 1, player_marker))
    tile_turtles[2].onclick(
        lambda x, y: tile_clicked(tile_turtles[2].xcor(), tile_turtles[2].ycor(), tile_turtles[2], 2, player_marker))
    tile_turtles[3].onclick(
        lambda x, y: tile_clicked(tile_turtles[3].xcor(), tile_turtles[3].ycor(), tile_turtles[3], 3, player_marker))

    tile_turtles[4].onclick(
        lambda x, y: tile_clicked(tile_turtles[4].xcor(), tile_turtles[4].ycor(), tile_turtles[4], 4, player_marker))
    tile_turtles[5].onclick(
        lambda x, y: tile_clicked(tile_turtles[5].xcor(), tile_turtles[5].ycor(), tile_turtles[5], 5, player_marker))
    tile_turtles[6].onclick(
        lambda x, y: tile_clicked(tile_turtles[6].xcor(), tile_turtles[6].ycor(), tile_turtles[6], 6, player_marker))

    tile_turtles[7].onclick(
        lambda x, y: tile_clicked(tile_turtles[7].xcor(), tile_turtles[7].ycor(), tile_turtles[7], 7, player_marker))
    tile_turtles[8].onclick(
        lambda x, y: tile_clicked(tile_turtles[8].xcor(), tile_turtles[8].ycor(), tile_turtles[8], 8, player_marker))
    tile_turtles[9].onclick(
        lambda x, y: tile_clicked(tile_turtles[9].xcor(), tile_turtles[9].ycor(), tile_turtles[9], 9, player_marker))

    wn.onkeypress(stopGame, "q")

    wn.listen()


    if not isPlayerTurn:

        move = evaluateBotLocation()

        turn_tracker.clear()
        turn_tracker.goto(0, 250)
        turn_tracker.write("Opponent turn", font=('Courier', 30, 'italic'))

        time.sleep(1)

        if insertLetter(bot_marker, move) == 0:
            finishGame()

        else:
            turn_tracker.clear()
            turn_tracker.goto(0, 250)
            turn_tracker.write("Your turn", font=('Courier', 30, 'italic'))
            isPlayerTurn = True

wn.mainloop()
