# TicTacToe Game for Ap Computer Science Principles
# Click on any grid location to play

# R to play again
# Q to quit the game

# Run this with 2 50x50 asset files both an X, and a O
# Titled X-image_50x50.gif, O-image_50x50.gif

# import modules
import random
import turtle
import time

# define variables
board = {
    0: '', 1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '}

# markers
player_marker = "X"
bot_marker = "O"

isPlayerTurn = True  # Decides whether it is player or robots turn

bgcolor = "beige"

# Binds each of the tiles with a coodinate
tile_turtles = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

# Used to track the X's and O's
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

def start():  # Initializes, and Resets Game
    wn.clear()  # In case of a reset

    # Imports all variables that will be edited
    global layout
    global turn_tracker
    global used_x
    global used_o
    global unused_x
    global unused_o
    global board
    global isPlayerTurn

    # resets the board
    board = {
        0: '', 1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}

    # Reset's all X's and O's in list
    unused_o = []
    unused_x = []

    # Resets isPlayerTurn
    isPlayerTurn = True

    used_o = []
    used_x = []

    wn.bgcolor(bgcolor)  # Sets background color for aesthetic

    wn.tracer(False)  # Disables all animation

    # Sets up turn_tracker turtle
    turn_tracker = turtle.Turtle()
    turn_tracker.hideturtle()
    turn_tracker.speed(0)
    turn_tracker.pu()

    # Initializes with player turn
    turn_tracker.goto(150, 250)
    turn_tracker.write("Player Turn", font=('Courier', 25, 'italic'))

    # Sets up player variable
    layout = turtle.Turtle()
    layout.hideturtle()
    layout.pu()
    layout.speed(0)
    layout.goto(0, 0)
    layout.seth(0)

    # Draws title
    layout.goto(-200, 300)
    layout.write("Tic Tac Toe", font=('Courier', 40, "bold"))

    # Draws indicators for the turtles
    layout.goto(250, 190)
    layout.write("(Player)", font=('Courier', 15, 'italic'))

    layout.goto(250, 90)
    layout.write("(Opponent)", font=('Courier', 15, 'italic'))

    # Create X's and O's
    for i in range(10):
        # Creates all X's
        x = turtle.Turtle()
        x.speed(0)
        x.shape("X-image_50x50.gif")
        x.shapesize(2)
        x.penup()
        x.goto(200, 200)
        x.speed(3)
        unused_x.append(x)

        # Create all O's
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
    # loop to draw horizantal lines
    for y in range(100, -1, -100):
        # Goes to correct location
        layout.pu()
        layout.goto(-200, y)
        # draws the lines
        layout.pd()
        layout.forward(300)

    # Sets heading for next to lines
    layout.seth(90)

    # loop to draw horizantal lines
    for x in range(-100, 100, 100):
        # Goes to correct location
        layout.pu()
        layout.goto(x, -100)

        # draws the lines
        layout.pd()
        layout.forward(300)

    # Guidance's Draw
    layout.pu()
    layout.goto(-350, -210)
    layout.write("Press Q to quit the game", font=("Open Sans", 10))

    layout.goto(-350, -230)
    layout.write("Press R to reset the game", font=("Open Sans", 10))
    wn.tracer(True)


# Inserts letter to dict, and moves marker to key
def insertLetter(letter, position):
    # Informs the client if game is already over
    if winCheck(board):
        return 0
    if checkDraw(board):
        return 0

    # Inserts letter into dict, and moves marker to key
    if board[position] == ' ':
        board[position] = letter
        tile_clicked(tile_turtles[position].xcor(), tile_turtles[position].ycor(), tile_turtles[position], position,
                     letter)

    # Informs the client if game is over because of this move
    if winCheck(board):
        return 0
    if checkDraw(board):
        return 0


# Checks if someone has won the game
def winCheck(boardState):
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9

    # Pseudocode for winCheck:
    # If 1 = 2, and 1 = 3, and 1 is a marker:
    #   return True
    # repeat for all remaining cases

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
    # 1 | 2 | 3
    # 4 | 5 | 6
    # 7 | 8 | 9

    # Pseudocode for markerWinCheck:
    # If 1 = 2, and 1 = 3, and 1 = mark:
    #   return True
    # repeat for all remaining cases

    if boardState[1] == boardState[2] and boardState[1] == boardState[3] and boardState[1] == mark:
        return True
    elif boardState[4] == boardState[5] and boardState[4] == boardState[6] and boardState[4] == mark:
        return True
    elif boardState[7] == boardState[8] and boardState[7] == boardState[9] and boardState[7] == mark:
        return True
    elif boardState[1] == boardState[4] and boardState[1] == boardState[7] and boardState[1] == mark:
        return True
    elif boardState[2] == boardState[5] and boardState[2] == boardState[8] and boardState[2] == mark:
        return True
    elif boardState[3] == boardState[6] and boardState[3] == boardState[9] and boardState[3] == mark:
        return True
    elif boardState[1] == boardState[5] and boardState[1] == boardState[9] and boardState[1] == mark:
        return True
    elif boardState[7] == boardState[5] and boardState[7] == boardState[3] and boardState[7] == mark:
        return True
    else:
        return False


# Checks for a draw
def checkDraw(boardState):
    # Pseudocode for check draw:

    # If no item in board is empty
    #   return True
    # Else
    #   return False

    for key in boardState.keys():
        if boardState[key] == ' ':
            return False
    return True


# Moves Marker to tile
def tile_clicked(x, y, tile, board_index, marker):
    global isPlayerTurn

    # Pseudocode for tile_clicked:

    # If mark = X, and Its Players Turn:
    #   Move turtle to the tile
    #   Change the Board
    #   Change to Opponents Turn
    # Elif mark = O, and it is not player turn:
    #   Move turtle to tile
    #   Change board

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

    wn.update()


# Places the opponent at the best location
def evaluateBotLocation():
    # Pseudocode for evaluateBotLocation:
    #
    # possibleMoves = getAllPossibleMoves
    #
    # If win is possible:
    #   Place marker there
    #   exit

    # If player win is possible:
    #   Place marker there
    #   exit

    # If center is available
    #   place marker there

    # If corner is available
    #   place marker in a random corner
    #   exit

    # If edge is available
    #   place marker in a random edge
    #   exit

    # exit

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

    # Displays who won or whether its a draw
    if markerWinCheck(board, bot_marker):
        layout.write(f"Opponent \"{bot_marker}\" Won", font=('Courier', 30, 'italic'))
    elif markerWinCheck(board, player_marker):
        layout.write(f"You \"{player_marker}\" Won", font=('Courier', 30, 'italic'))
    elif checkDraw(board):
        layout.write("It is a Draw", font=('Courier', 30, 'italic'))


# Ends the game
def stopGame():
    turtle.bye()


# Restarts the game
def restart():
    start()


# Initialize Game
start()

# Game Loop

# Note: The reason for the try catch is when the player exits the game,
# It is often in the middle of a task therefore unable to finsh, and gives an error
try:
    while True:

        # Pseudocode

        # When tile is clicked
        #   Move X to tile

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

        # Key presses for extra features
        wn.onkeypress(stopGame, "q")
        wn.onkeypress(restart, "r")

        # Listens for all keyboard presses
        wn.listen()

        if not isPlayerTurn:

            # Determine bots Move
            move = evaluateBotLocation()

            turn_tracker.clear()
            turn_tracker.goto(150, 250)
            turn_tracker.write("Opponent turn", font=('Courier', 25, 'italic'))

            # waits to create illusion of decision time
            time.sleep(1.61)

            # Plays bot move, if it ends game then finish game
            if insertLetter(bot_marker, move) == 0:
                finishGame()

            # Continue on game if bot move doesn't finish
            else:
                turn_tracker.clear()
                turn_tracker.goto(150, 250)
                turn_tracker.write("Player turn", font=('Courier', 25, 'italic'))
                isPlayerTurn = True

except:
    pass
