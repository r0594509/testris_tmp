from tkinter import *
import platform       # used to check os and change keybindings accordingly
import time     # was used for debugging
import sys      # used when closing the script
from random import randint      # used for random color assignment and figure spawning

# Nathan Olmanst
# r0594509
# 1BA Informatica reeks 2
# 14-12-14

properties = ["A", 0, 0]    # default properties [0: block type(string), 1: block state(int), 2: block color(int)]
boundaryBoxY = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
boundaryBoxX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # 5 possible colors + grey defined with values 0 - 5
colorBox = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def initialize():
    # called once when the game is started (main() executed)
    # [ put your own model/representation 
    #   initialization here ]

    return {"dimensions": (10, 20), "square0": {"x": 0, "y": 0}, "square1": {"x": 0, "y": 0}, "square2": {"x": 0, "y": 0}, "square3": {"x": 0, "y": 0}}
    # the data structure returned from this method1
    # is passed as parameter ''model'' to the functions
    # draw(), onkey() and onloop() below

def substring(element, list):
    #returns a list of numbers representing the position of the same "element" in "list"
    #workaround to array.index(element) only returning position of the first value
    return [i for i, value in enumerate(list) if element == value]

def turnfigure(model):
    #efficiency at its finest

    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]

    if properties[0] == "line":
        if properties[1] == 0:
            if canturn(square0["x"] + 2, square1["x"] + 1, square2["x"], (square3["x"] - 1), square0["y"] - 2,
                       square1["y"] - 1, square2["y"], square3["y"] + 1):
                square0["x"] += 2
                square0["y"] -= 2
                square1["x"] += 1
                square1["y"] -= 1
                square3["x"] -= 1
                square3["y"] += 1
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"] - 2, square1["x"] - 1, square2["x"], (square3["x"] + 1), square0["y"] + 2,
                       square1["y"] + 1, square2["y"], square3["y"] - 1):
                square0["x"] -= 2
                square0["y"] += 2
                square1["x"] -= 1
                square1["y"] += 1
                square3["x"] += 1
                square3["y"] -= 1
                properties[1] -= 1

    elif properties[0] == "piramid":
        if properties[1] == 0:
            if canturn(square0["x"] + 1, square1["x"], square2["x"], square3["x"], square0["y"] + 1,
                       square1["y"], square2["y"], square3["y"]):
                square0["x"] += 1
                square0["y"] += 1
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"], square1["x"] - 1, square2["x"], square3["x"], square0["y"],
                       square1["y"] + 1, square2["y"], square3["y"]):
                square1["x"] -= 1
                square1["y"] += 1
                properties[1] += 1

        elif properties[1] == 2:
            if canturn(square0["x"], square1["x"], square2["x"], (square3["x"] - 1), square0["y"],
                       square1["y"], square2["y"], square3["y"] - 1):
                square3["x"] -= 1
                square3["y"] -= 1
                properties[1] += 1

        elif properties[1] == 3:
            if canturn(square0["x"] - 1, square1["x"] + 1, square2["x"], (square3["x"] + 1), square0["y"] - 1,
                       square1["y"] - 1, square2["y"], square3["y"] + 1):
                square0["x"] -= 1
                square0["y"] -= 1
                square1["x"] += 1
                square1["y"] -= 1
                square3["x"] += 1
                square3["y"] += 1
                properties[1] -= 3

    elif properties[0] == "lleft":
        if properties[1] == 0:
            if canturn(square0["x"] + 1, square1["x"] + 2, square2["x"], (square3["x"] - 1), square0["y"] - 1,
                       square1["y"], square2["y"], square3["y"] +1):
                square0["x"] += 1
                square0["y"] -= 1
                square1["x"] += 2
                square3["x"] -= 1
                square3["y"] += 1
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"] - 1, square1["x"], square2["x"], (square3["x"] + 1), square0["y"] + 1,
                       square1["y"] + 1, square2["y"], square3["y"]):
                square0["x"] -= 1
                square0["y"] += 1
                square1["y"] += 1
                square3["x"] += 1
                properties[1] += 1

        elif properties[1] == 2:
            if canturn(square0["x"] + 1, square1["x"] - 1, square2["x"], (square3["x"] - 2), square0["y"] - 1,
                       square1["y"] + 1, square2["y"], square3["y"]):
                square0["x"] += 1
                square0["y"] -= 1
                square1["x"] -= 1
                square1["y"] += 1
                square3["x"] -= 2
                properties[1] += 1

        elif properties[1] == 3:
            if canturn(square0["x"] - 1, square1["x"] - 1, square2["x"], (square3["x"] + 2), square0["y"] + 1,
                       square1["y"] - 2, square2["y"], square3["y"] - 1):
                square0["x"] -= 1
                square0["y"] += 1
                square1["x"] -= 1
                square1["y"] -= 2
                square3["x"] += 2
                square3["y"] -= 1
                properties[1] -= 3

    elif properties[0] == "lstair":
        if properties[1] == 0:
            if canturn(square0["x"] + 2, square1["x"], square2["x"], square3["x"], square0["y"] - 1,
                       square1["y"], square2["y"], square3["y"] - 1):
                square0["x"] += 2
                square0["y"] -= 1
                square3["y"] -= 1
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"] - 2, square1["x"], square2["x"], square3["x"], square0["y"] + 1,
                       square1["y"], square2["y"], square3["y"] + 1):
                square0["x"] -= 2
                square0["y"] += 1
                square3["y"] += 1
                properties[1] -= 1

    elif properties[0] == "lright":
        if properties[1] == 0:
            if canturn(square0["x"] + 1, square1["x"], square2["x"], (square3["x"] - 1), square0["y"] - 1,
                       square1["y"] - 2, square2["y"], square3["y"] + 1):
                square0["x"] += 1
                square0["y"] -= 1
                square1["y"] -= 2
                square3["x"] -= 1
                square3["y"] += 1
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"] + 1, square1["x"] + 2, square2["x"], (square3["x"] - 1), square0["y"] + 1,
                       square1["y"], square2["y"], square3["y"] - 1):
                square0["x"] += 1
                square0["y"] += 1
                square1["x"] += 2
                square3["x"] -= 1
                square3["y"] -= 1
                properties[1] += 1

        elif properties[1] == 2:
            if canturn(square0["x"] - 1, square1["x"], square2["x"], (square3["x"] + 1), square0["y"] + 1,
                       square1["y"] + 2, square2["y"], square3["y"] - 1):
                square0["x"] -= 1
                square0["y"] += 1
                square1["y"] += 2
                square3["x"] += 1
                square3["y"] -= 1
                properties[1] += 1

        elif properties[1] == 3:
            if canturn(square0["x"] - 1, square1["x"] - 2, square2["x"], (square3["x"] + 1), square0["y"] - 1,
                       square1["y"], square2["y"], square3["y"] + 1):
                square0["x"] -= 1
                square0["y"] -= 1
                square1["x"] -= 2
                square3["x"] += 1
                square3["y"] += 1
                properties[1] -= 3

    elif properties[0] == "rstair":
        if properties[1] == 0:
            if canturn(square0["x"], square1["x"], square2["x"], (square3["x"] - 2), square0["y"] - 2,
                       square1["y"], square2["y"], square3["y"]):
                square0["y"] -= 2
                square3["x"] -= 2
                properties[1] += 1

        elif properties[1] == 1:
            if canturn(square0["x"], square1["x"], square2["x"], (square3["x"] + 2), square0["y"] + 2,
                       square1["y"], square2["y"], square3["y"]):
                square0["y"] += 2
                square3["x"] += 2
                properties[1] -= 1

def canturn(x0=5, x1=5, x2=5, x3=5, y0=-10, y1=-10, y2=-10, y3=-10):

    if x0 >= 10 or x1 >= 10 or x2 >= 10 or x3 >= 10:
        #check right edge
        print("stop 1")
        print(x0, x1, x2, x3)
        return False
    elif x0 <= -1 or x1 <= -1 or x2 <= -1 or x3 <= -1:
        #check left edge
        print("stop 2")
        print(x0, x1, x2, x3)
        return False
    else:
        for i in range(0, 10):
            if i in boundaryBoxX:
                temp = substring(i, boundaryBoxX)
                for j in temp:
                    if boundaryBoxY[j] == y0 and boundaryBoxX[i] == x0 or boundaryBoxY[j] == y1 and \
                            boundaryBoxX[i] == x1 or boundaryBoxY[j] == y2 and boundaryBoxX[i] == x2\
                            or boundaryBoxY[j] == y3 and boundaryBoxX[i] == x3:
                        print("stop 3")
                        return False

    return True

def removeline(line):

    templist = substring(line, boundaryBoxY)
    for n in reversed(templist):
        #Reverse is needed else boundaryBox will be shortened by 1 value after every loop. This will cause the element in templist to refer to the wrong value
        #print("THIS IS TEMPLIST !!!", templist)
        #print("this is n:", n)
        #print("boundaryboxX length:", len(boundaryBoxX))
        #haal alle coördinaten van de volledige rij uit de bounderyBoxen
        boundaryBoxX.pop(n)
        boundaryBoxY.pop(n)
        colorBox.pop(n)

def lowersquares(line):

    #check function "check_filled_line()" for syntax explanation
    for var in range((line-1), 0, -1):
        if var in boundaryBoxY:
            positions_of_var = substring(var, boundaryBoxY)
            for m in reversed(positions_of_var):
                boundaryBoxY[m] += 1

def check_filled_line(model, canvas):

    for i in range(19, 0, -1):
        #20 -> 0 cuz filled lines will most likely occur at bottom
        #20 is de bottom boundary en moet niet weggehaald worden
        #print("getal tussen 0 en 20:", i)
        if i in boundaryBoxY:
            #print("getal", i, "is in boundaryBoxY")
            #Neem neem X waarden voor alle blocks met y[i]
            #print("rij", i, "bevat", len(substring(i, boundaryBoxY)), "elementen")
            #maak lijst aan met alle indexen van element i in boundaryBox
            if len(substring(i, boundaryBoxY)) == 10:
                #print("BB:", boundaryBoxX)
                #print("len BB:", len(boundaryBoxX))
                #print("pos counter:", substring(i, boundaryBoxY))
                #als templist = 10 -> er is een rij volledig
                removeline(i)
                #when line is removed, move all blocks above row number "i" down.
                #function lowersquares() follows same syntax as above
                lowersquares(i)
                #check for other filled lines (cannot loop more than there are filled lines)
                check_filled_line(model, canvas)

    #redraw grid with changed values
    draw(model, canvas)

def random_int():
    return randint(0, 5)

def generate_color():

    n = random_int()
    if n == colorBox[-1]:
        #need to use colorBox because properties list gets reset to default before assigning new ones values
        #colorBox[-1] would have the same outcome as properties[-1] if it did not get reset.
        n = random_int()
    return n
    #ranom cijfer, maar nooit 2x same achter elkaar

def game_is_over():
    if 0 in boundaryBoxY:
        print("Game is Over")
        return True
    return False

def getrandom(square0, square1, square2, square3):

    if game_is_over():
        sys.exit(0)
        #stop het spel als game_is_over = True

    #generate_color()
    #generate_color() function moved into init_properties() that is called by every figure function

    n = randint(0, 6)

    if n == 0:
        return spawn_line(square0, square1, square2, square3)
    elif n == 1:
        return spawn_piramid(square0, square1, square2, square3)
    elif n == 2:
        return spawn_square(square0, square1, square2, square3)
    elif n == 3:
        return spawn_lLeft(square0, square1, square2, square3)
    elif n == 4:
        return spawn_srairL(square0, square1, square2, square3)
    elif n == 5:
        return spawn_srairR(square0, square1, square2, square3)
    else:
        return spawn_lRight(square0, square1, square2, square3)

def color_out_of_list(color, var, loopvar=0):
    #functie "vertaalt cijfers in lijst in een bepaalde kleur"
    #parameters:
        # var: bepaalt of de functie voor een nieuwe, "bewegende" block wordt gebruikt, of een oude, vaste ("set") block
        # loopvar: enkel voor bij de oude blocks. haalt color uit list, op positie "loopvar" (omdat eigenschappen van het 'object' in 3 verschillende lijsten zit

    if var == "new":
        #Use function for new blocks
        if properties[-1] == 0:
            color = "RoyalBlue2"
        elif properties[-1] == 1:
            color = "gold2"
        elif properties[-1] == 2:
            color = "brown1"
        elif properties[-1] == 3:
            color = "green4"
        elif properties[-1] == 4:
            color = "cyan"
        elif properties[-1] == 5:
            color = "VioletRed2"
    elif var == "set":
        #Use function to set assigned color to placed blocks
        if colorBox[loopvar] == 0:
            color = "RoyalBlue2"
        elif colorBox[loopvar] == 1:
            color = "gold2"
        elif colorBox[loopvar] == 2:
            color = "brown1"
        elif colorBox[loopvar] == 3:
            color = "green4"
        elif colorBox[loopvar] == 4:
            color = "cyan"
        elif colorBox[loopvar] == 5:
            color = "VioletRed2"
    return color

def draw(model, canvas):
    # called after onkey() and onloop(), so every
    # X milliseconds and after each time the user
    # presses a key
    canvas.delete(ALL)
    # clear canvas
    block_height = 20
    block_margin = 4
    dimensions = model["dimensions"]
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]
    #print(square0)
    #print(square1)
    #print(square2)
    #print(square3)
    #print(properties)
    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            color = "grey80"
            #Original color "#f2f2f2"
            # default color of empty block
            if x == square0["x"] and y == square0["y"]:
                color = color_out_of_list(color, "new")
            if x == square1["x"] and y == square1["y"]:
                color = color_out_of_list(color, "new")
            if x == square2["x"] and y == square2["y"]:
                color = color_out_of_list(color, "new")
            if x == square3["x"] and y == square3["y"]:
                color = color_out_of_list(color, "new")

            #Color block coörds in boundaryBox X&Y
            for i in range(0, len(boundaryBoxX)):
                if x == (boundaryBoxX[i]) and y == (boundaryBoxY[i]):
                    color = color_out_of_list(color, "set", i)
                # color of filled block
            rect = canvas.create_rectangle(
                x*block_height+(x+1)*block_margin, 
                y*block_height+(y+1)*block_margin, 
                (x+1)*block_height+(x+1)*block_margin, 
                (y+1)*block_height+(y+1)*block_margin, 
                fill=color, outline=color)
            # draws a rectangle
    # draws rectangle grid

def setfigure(model, canvas):

    #pass last coordinates of figure to boundarybox's
    #will get drawn next tick by Draw function

    dimensions = model["dimensions"]
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]

    boundaryBoxX.append(square0['x'])
    boundaryBoxY.append(square0['y'])
    colorBox.append(properties[-1])
    boundaryBoxX.append(square1['x'])
    boundaryBoxY.append(square1['y'])
    colorBox.append(properties[-1])
    boundaryBoxX.append(square2['x'])
    boundaryBoxY.append(square2['y'])
    colorBox.append(properties[-1])
    boundaryBoxX.append(square3['x'])
    boundaryBoxY.append(square3['y'])
    colorBox.append(properties[-1])
    #store coördinates of block + color in (huge) list

    #check for filled row
    check_filled_line(model, canvas)

def canmove(model, direction):

    #Going rather heavy on the for loops

    dimensions = model["dimensions"]
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]

    if direction == "left":
        if square0["x"] == 0 or square1["x"] == 0 or square2["x"] == 0 or square3["x"] == 0:
            #boundary left : x=0
            #print("cannot move left")
            return False
        else:
            for i in range(0, len(boundaryBoxX)):
                if square0["x"] == (boundaryBoxX[i]+1) and square0["y"] == boundaryBoxY[i] or \
                                square1["x"] == (boundaryBoxX[i]+1) and square1["y"] == boundaryBoxY[i] or \
                                square2["x"] == (boundaryBoxX[i]+1) and square2["y"] == boundaryBoxY[i] or \
                                square3["x"] == (boundaryBoxX[i]+1) and square3["y"] == boundaryBoxY[i]:
                    #Line too long
                    return False
        return True
    elif direction == "right":
        if square0["x"] == 9 or square1["x"] == 9 or square2["x"] == 9 or square3["x"] == 9:
            #boundary right : x=9
            #print("cannot move right")
            return False
        else:
            for i in range(0, len(boundaryBoxX)):
                if square0["x"] == (boundaryBoxX[i]-1) and square0["y"] == boundaryBoxY[i] or \
                                square1["x"] == (boundaryBoxX[i]-1) and square1["y"] == boundaryBoxY[i] or \
                                square2["x"] == (boundaryBoxX[i]-1) and square2["y"] == boundaryBoxY[i] or \
                                square3["x"] == (boundaryBoxX[i]-1) and square3["y"] == boundaryBoxY[i]:
                    #Line too long
                    return False
        return True
    #elif n == "down":

def can_descend(model, square0, square1, square2, square3):

    dimensions = model["dimensions"]
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]

    #print(square0["x"], square0["y"])
    #print(square1["x"], square1["y"])
    #print(square2["x"], square2["y"])
    #print(square3["x"], square3["y"])
    #print("dis is da box", boundaryBoxY)

    #if k in boundaryBoxY or l in boundaryBoxY or m in boundaryBoxY or n in boundaryBoxY:
    for i in range(0, len(boundaryBoxY)):
        if square0["y"] == (boundaryBoxY[i]-1) and square0["x"] == boundaryBoxX[i] or \
                                square1["y"] == (boundaryBoxY[i]-1) and square1["x"] == boundaryBoxX[i] or \
                                square2["y"] == (boundaryBoxY[i]-1) and square2["x"] == boundaryBoxX[i] or \
                                square3["y"] == (boundaryBoxY[i]-1) and square3["x"] == boundaryBoxX[i]:
            #Split up line cause too long
            # boundaryBoxY[i]-1 to solve the stack on coör issue
            #print("(x;y) coör in boundaryboxX and Y, cannot descend")
            return False
    return True

def onkey(model, keycode):
    # called when user presses a key
    # [ put your own code here ]
    # print(keycode)

    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]
    #print(keycode)

    if keycode == "Left":
        if canmove(model, "left"):
            #check if player can force left
            square0["x"] -= 1
            square1["x"] -= 1
            square2["x"] -= 1
            square3["x"] -= 1
            #print("(" + time.strftime('%X') + ")", "Left arrow with value", keycode, "pressed")

    elif keycode == "Right":
        if canmove(model, "right"):
            #Check if player can force right
            square0["x"] += 1
            square1["x"] += 1
            square2["x"] += 1
            square3["x"] += 1
            #print("(" + time.strftime('%X') + ")", "Right arrow with value", keycode, "pressed")

    elif keycode == "Down":
        if can_descend(model, square0, square1, square2, square3):
            #Check if player can force down
            square0["y"] += 1
            square1["y"] += 1
            square2["y"] += 1
            square3["y"] += 1
            #print("(" + time.strftime('%X') + ")", "Down arrow with value", keycode, "pressed")

    elif keycode == "Up":
        turnfigure(model)
        #square0["y"] -= 1
        #square1["y"] -= 1
        #square2["y"] -= 1
        #square3["y"] -= 1
        #print("(" + time.strftime('%X') + ")", "Up arrow with value", keycode, "pressed")

    elif keycode == "space":
        #spacebar
        spawn_lLeft(square0, square1, square2, square3)
        #getrandom(square0, square1, square2, square3)

def onloop(model, canvas):
    # called every X milliseconds
    # [ put your own code here ]
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]
    if can_descend(model, square0, square1, square2, square3):
        square0["y"] += 1
        square1["y"] += 1
        square2["y"] += 1
        square3["y"] += 1
        #print(square0["x"], square0["y"])
    else:
        setfigure(model, canvas)
        getrandom(square0, square1, square2, square3)

def init_properties(string, value=0):

    del properties[2]
    del properties[1]
    del properties[0]
    properties.insert(0, str(string))
    properties.insert(1, value)
    properties.insert(2, generate_color())

    #print(properties)

def spawn_line(square0, square1, square2, square3):

    init_properties("line")

    square0["x"] = 4
    square1["x"] = 5
    square2["x"] = 6
    square3["x"] = 7
    square0["y"] = 0
    square1["y"] = 0
    square2["y"] = 0
    square3["y"] = 0

    #print("spawned a line")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_square(square0, square1, square2, square3):

    init_properties("square")

    square0["x"] = 5
    square1["x"] = 5
    square2["x"] = 6
    square3["x"] = 6
    square0["y"] = 0
    square1["y"] = 1
    square2["y"] = 0
    square3["y"] = 1

    #print("spawned a square")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_piramid(square0, square1, square2, square3):

    init_properties("piramid")

    square0["x"] = 4
    square1["x"] = 5
    square2["x"] = 5
    square3["x"] = 6
    square0["y"] = 1
    square1["y"] = 0
    square2["y"] = 1
    square3["y"] = 1

    #print("spawned a piramid")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_lRight(square0, square1, square2, square3):

    init_properties("lright")

    square0["x"] = 4
    square1["x"] = 4
    square2["x"] = 5
    square3["x"] = 6
    square0["y"] = 0
    square1["y"] = 1
    square2["y"] = 0
    square3["y"] = 0

    #print("spawned a right l")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_lLeft(square0, square1, square2, square3):

    init_properties("lleft")

    square0["x"] = 4
    square1["x"] = 4
    square2["x"] = 5
    square3["x"] = 6
    square0["y"] = 1
    square1["y"] = 0
    square2["y"] = 1
    square3["y"] = 1

    #print("spawned a left l")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_srairL(square0, square1, square2, square3):

    init_properties("lstair")

    square0["x"] = 4
    square1["x"] = 5
    square2["x"] = 5
    square3["x"] = 6
    square0["y"] = 0
    square1["y"] = 0
    square2["y"] = 1
    square3["y"] = 1

    #print("spawned a left stair")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def spawn_srairR(square0, square1, square2, square3):

    init_properties("rstair")

    square0["x"] = 4
    square1["x"] = 5
    square2["x"] = 5
    square3["x"] = 6
    square0["y"] = 1
    square1["y"] = 1
    square2["y"] = 0
    square3["y"] = 0

    #print("spawned a right stair")
    return square0["x"], square1["x"], square2["x"], square3["x"], square0["y"], square1["y"], square2["y"], square3["y"]

def check_os():

    print("")
    #obsolete function. functionality replaced with the use of "event.keysym" instead of "event.keycode"
    '''
    OS = platform.system()
    #print(OS)

    global LEFT
    global RIGHT
    global UP
    global DOWN
    global SPACE

    if OS == "Windows":
        LEFT = 37
        RIGHT = 39
        UP = 38
        DOWN = 40
        SPACE = 32
        print("Windows OS detected")
    elif OS == "Linux":
        LEFT = 0
        RIGHT = 0
        UP = 0
        DOWN = 0
        SPACE = 0
        print("OS not supported")
    else:
        #most likely used for MAC
        LEFT = 8124162
        RIGHT = 0
        UP = 0
        DOWN = 0
        SPACE = 0
        print("OS not supported")
        '''

###########################################################
# normally, you would not need to change anything in main #    
def main(update_interval, canvas_dimensions):

    #check_os()
    #found a better way to ensure cross-platform compatibility

    def keypress(event, model, canvas):
        onkey(model, event.keysym)
        draw(model, canvas)
    def gameloop(X, model, master, canvas):
        master.after(X, gameloop, X, model, master, canvas)
        onloop(model, canvas)
        draw(model, canvas)
    model = initialize()
    square0 = model["square0"]
    square1 = model["square1"]
    square2 = model["square2"]
    square3 = model["square3"]
    if not game_is_over():
        getrandom(square0, square1, square2, square3)
    # initialize your model
    master = Tk()
    # initialize top level widget
    canvas = Canvas(master, width=canvas_dimensions[0], 
            height=canvas_dimensions[1], background="white")
    # initialize canvas
    canvas.pack()
    master.bind("<Key>", lambda e: keypress(e, model, canvas))
    # bind the keypress() function to a key press event
    # while passing the model and the canvas as arguments too
    gameloop(update_interval, model, master, canvas)
    # start the gameloop
    master.mainloop()
    # enables event handling etc. by tkinter
    
############################################################
    
if __name__ == "__main__":
    update_interval = 750
    #was 500
    canvas_dimensions = (300, 500)
    # [ you might want to adjust these settings ]
    main(update_interval, canvas_dimensions)