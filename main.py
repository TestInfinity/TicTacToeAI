# TicTacToe Game for Ap Computer Science Principles
# Click on any grid location to play
# R to play again
# Q to quit the game

# import modules
import random
import turtle
import time

# define variables
board = {
    0: '', 1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '}

player_marker = "X"
bot_marker = "O"
running = True
bgcolor = "beige"
isPlayerTurn = True

tile_turtles = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

unused_x = []
unused_o = []

used_o = []
used_x = []

# create & customize screen
wn = turtle.Screen()
wn.bgcolor(bgcolor)
wn.addshape("O-image_50x50.gif")
wn.addshape("X-image_50x50.gif")

# create & customize layout
layout = turtle.Turtle()
layout.pu()
layout.speed(0)
layout.hideturtle()

# create & customize turn_tracker
turn_tracker = turtle.Turtle()
turn_tracker.speed(0)
turn_tracker.pu()
turn_tracker.hideturtle()


# Functions

# Initializes Game
def start():
    global layout
    global turn_tracker
    global used_x
    global used_o
    global unused_x
    global unused_o
    global board

    board = {
        0: '', 1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}

    unused_o = []
    unused_x = []
    used_o = []
    used_x = []

    wn.bgcolor(bgcolor)
    wn.tracer(False)

    turn_tracker = turtle.Turtle()
    turn_tracker.hideturtle()
    turn_tracker.speed(0)
    turn_tracker.pu()

    turn_tracker.goto(100, 250)
    turn_tracker.write("Player Turn", font=('Courier', 25, 'italic'))

    layout = turtle.Turtle()
    layout.hideturtle()
    layout.pu()
    layout.speed(0)

    turn_tracker.pu()
    layout.pu()
    layout.goto(0, 0)
    layout.seth(0)
    turn_tracker.goto(0, 0)

    layout.goto(250, 190)
    layout.write("(Player)", font=('Courier', 15, 'italic'))

    layout.goto(250, 90)
    layout.write("(Opponent)", font=('Courier', 15, 'italic'))

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
            t.color(bgcolor)
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

    # Guidance's Draw
    layout.pu()
    layout.goto(-300, -210)
    layout.write("Press Q to quit the game")

    layout.goto(-300, -230)
    layout.write("Press R to play again")
    wn.tracer(True)


# Inserts letter to dict, and moves marker to key
def insertLetter(letter, position):
    global running

    if winCheck(board):
        return 0
    if checkDraw(board):
        return 0
    if board[position] == ' ':
        board[position] = letter
        tile_clicked(tile_turtles[position].xcor(), tile_turtles[position].ycor(), tile_turtles[position], position,
                     letter)

    if winCheck(board):
        return 0
    if checkDraw(board):
        return 0


# Checks if someone has won the game
def winCheck(boardState):
    if boardState[1] == boardState[2] and boardState[1] == boardState[3] and boardState[1] != ' ':
        return True
    elif boardState[4] == boardState[5] and boardState[4] == boardState[6] and boardState[4] != ' ':
        return True
    elif boardState[7] == boardState[8] and boardState[7] == boardState[9] and boardState[7] != ' ':
        return True
    elif boardState[1] == boardState[4] and boardState[1] == boardState[7] and boardState[1] != ' ':
        return True
    elif boardState[2] == boardState[5] and boardState[2] == boardState[8] and boardState[2] != ' ':
        return True
    elif boardState[3] == boardState[6] and boardState[3] == boardState[9] and boardState[3] != ' ':
        return True
    elif boardState[1] == boardState[5] and boardState[1] == boardState[9] and boardState[1] != ' ':
        return True
    elif boardState[7] == boardState[5] and boardState[7] == boardState[3] and boardState[7] != ' ':
        return True
    else:
        return False


# Checks if a specific marker has one
def markerWinCheck(boardState, mark):
    if boardState[1] == boardState[2] and boardState[1] == boardState[3] and boardState[1] == mark:
        return True
    elif (boardState[4] == boardState[5] and boardState[4] == boardState[6] and boardState[4] == mark):
        return True
    elif (boardState[7] == boardState[8] and boardState[7] == boardState[9] and boardState[7] == mark):
        return True
    elif (boardState[1] == boardState[4] and boardState[1] == boardState[7] and boardState[1] == mark):
        return True
    elif (boardState[2] == boardState[5] and boardState[2] == boardState[8] and boardState[2] == mark):
        return True
    elif (boardState[3] == boardState[6] and boardState[3] == boardState[9] and boardState[3] == mark):
        return True
    elif (boardState[1] == boardState[5] and boardState[1] == boardState[9] and boardState[1] == mark):
        return True
    elif (boardState[7] == boardState[5] and boardState[7] == boardState[3] and boardState[7] == mark):
        return True
    else:
        return False


# Checks for a draw
def checkDraw(boardState):
    for key in boardState.keys():
        if (boardState[key] == ' '):
            return False
    return True


# Moves Marker to tile
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


# Places the opponent at the best location
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

    if 5 in possible_moves:
        move = 5
        return move

    corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners.append(i)
    if len(corners) > 0:
        move = random.choice(corners)
        return move

    edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges.append(i)
    if len(edges) > 0:
        move = random.choice(edges)
        return move

    return 0


# gets called when game can no longer continue
def finishGame():
    layout.pu()
    layout.goto(-300, -150)

    if markerWinCheck(board, bot_marker):
        layout.write(f"Opponent \"{bot_marker}\" Won", font=('Courier', 30, 'italic'))
    elif markerWinCheck(board, player_marker):
        layout.write(f"You \"{player_marker}\" Won", font=('Courier', 30, 'italic'))
    else:
        layout.write("It is a Draw", font=('Courier', 30, 'italic'))


# Ends the game
def stopGame():
    turtle.bye()


# Restarts the game
def restart():
    wn.tracer(False)
    wn.clear()
    start()
    wn.tracer(True)


# Initialize Game
start()

# Game Loop
try:
    while running:
        tile_turtles[1].onclick(
            lambda x, y: tile_clicked(tile_turtles[1].xcor(), tile_turtles[1].ycor(), tile_turtles[1], 1,
                                      player_marker))
        tile_turtles[2].onclick(
            lambda x, y: tile_clicked(tile_turtles[2].xcor(), tile_turtles[2].ycor(), tile_turtles[2], 2,
                                      player_marker))
        tile_turtles[3].onclick(
            lambda x, y: tile_clicked(tile_turtles[3].xcor(), tile_turtles[3].ycor(), tile_turtles[3], 3,
                                      player_marker))

        tile_turtles[4].onclick(
            lambda x, y: tile_clicked(tile_turtles[4].xcor(), tile_turtles[4].ycor(), tile_turtles[4], 4,
                                      player_marker))
        tile_turtles[5].onclick(
            lambda x, y: tile_clicked(tile_turtles[5].xcor(), tile_turtles[5].ycor(), tile_turtles[5], 5,
                                      player_marker))
        tile_turtles[6].onclick(
            lambda x, y: tile_clicked(tile_turtles[6].xcor(), tile_turtles[6].ycor(), tile_turtles[6], 6,
                                      player_marker))

        tile_turtles[7].onclick(
            lambda x, y: tile_clicked(tile_turtles[7].xcor(), tile_turtles[7].ycor(), tile_turtles[7], 7,
                                      player_marker))
        tile_turtles[8].onclick(
            lambda x, y: tile_clicked(tile_turtles[8].xcor(), tile_turtles[8].ycor(), tile_turtles[8], 8,
                                      player_marker))
        tile_turtles[9].onclick(
            lambda x, y: tile_clicked(tile_turtles[9].xcor(), tile_turtles[9].ycor(), tile_turtles[9], 9,
                                      player_marker))

        wn.onkeypress(stopGame, "q")
        wn.onkeypress(restart, "r")

        wn.listen()

        if not isPlayerTurn:

            move = evaluateBotLocation()

            turn_tracker.clear()
            turn_tracker.goto(100, 250)
            turn_tracker.write("Opponent turn", font=('Courier', 25, 'italic'))

            time.sleep(1)

            if insertLetter(bot_marker, move) == 0:
                finishGame()

            else:
                turn_tracker.clear()
                turn_tracker.goto(100, 250)
                turn_tracker.write("Player turn", font=('Courier', 25, 'italic'))
                isPlayerTurn = True

except:
    pass
