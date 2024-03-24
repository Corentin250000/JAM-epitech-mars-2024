import random
import keyboard
import os

def set_maze_original():

    """

    Définit le labyrinthe

    Valeurs :

        - 0 : mur
        - 1 : chemin vide
        - 2 : point de départ
        - 3 : point d'arrivée
        - 4 : porte ouverte (compte comme un chemin vide)
        - 5 : porte fermée (compte comme un mur)
        - 6 : chasseur
        - 7 : proies
    
    """

    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 4, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 7, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    return maze

def set_maze_complete():

    """

    Définit le labyrinthe

    Valeurs :

        - 0 : mur
        - 1 : chemin vide
        - 2 : point de départ
        - 3 : point d'arrivée
        - 4 : porte ouverte (compte comme un chemin vide)
        - 5 : porte fermée (compte comme un mur)
        - 6 : chasseur
        - 7 : proies
    
    """

    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 1, 0, 7, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 4, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 4, 1, 7, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 4, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 7, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    return maze

def print_maze(maze):

    for i in range(len(maze)):
        print(maze[i])

def nb_prey(maze):

    result = 0

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 7:
                result += 1

    return result

def pos_prey(maze):

    result = []

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 7:
                result.append((i, j))

    return result

def pos_hunter(maze):

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 6:
                return (i, j)
            
def pos_departure(maze):

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 2:
                return (i, j)

def pos_exit(maze):

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 3:
                return (i, j)
            
def pos_closed_doors(maze):

    result = []

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 5:
                result.append((i, j))

    return result

def pos_opened_doors(maze):

    result = []

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == 4:
                result.append((i, j))

    return result

def actions_prey(maze, original, game_turn):

    if game_turn % 2 != 0:
        pass

    else:

        for u in range(2):
            positions_preys = pos_prey(maze)

            for n in range(len(positions_preys)):
                i, j = positions_preys[n]
                action = random.randint(1, 6)

                if action == 1: # do nothing
                    pass

                elif action == 2: # go up

                    if maze[i - 1][j] == 3 or maze[i - 1][j] == 2:
                        maze[i][j] = original[i][j]

                    if maze[i - 1][j] == 1 or maze[i - 1][j] == 4:
                        maze[i][j] = 1
                        maze[i - 1][j] = 7

                    else:
                        pass

                elif action == 3: # go left

                    if maze[i][j - 1] == 3 or maze[i][j - 1] == 2:
                        maze[i][j] = original[i][j]

                    if maze[i][j - 1] == 1 or maze[i][j - 1] == 4:
                        maze[i][j] = 1
                        maze[i][j - 1] = 7

                    else:
                        pass

                elif action == 4: # go down

                    if maze[i + 1][j] == 3 or maze[i + 1][j] == 2:
                        maze[i][j] = original[i][j]

                    if maze[i + 1][j] == 1 or maze[i + 1][j] == 4:
                        maze[i][j] = 1
                        maze[i + 1][j] = 7

                    else:
                        pass

                elif action == 5: # go right

                    if maze[i][j + 1] == 3 or maze[i][j + 1] == 2:
                        maze[i][j] = original[i][j]

                    if maze[i][j + 1] == 1 or maze[i][j + 1] == 4:
                        maze[i][j] = 1
                        maze[i][j + 1] = 7

                    else:
                        pass

                elif action == 6: # Open or close a door nearby

                    if maze[i - 1][j] == 4:
                        maze[i - 1][j] == 5
                        original[i - 1][j] == 5

                    elif maze[i][j - 1] == 4:
                        maze[i][j - 1] == 5
                        original[i][j - 1] == 5

                    elif maze[i + 1][j] == 4:
                        maze[i + 1][j] == 5
                        original[i + 1][j] == 5

                    elif maze[i][j + 1] == 4:
                        maze[i][j + 1] == 5
                        original[i][j + 1] == 5

                    elif maze[i - 1][j] == 5:
                        maze[i - 1][j] == 4
                        original[i - 1][j] == 4

                    elif maze[i][j - 1] == 5:
                        maze[i][j - 1] == 4
                        original[i][j - 1] == 4

                    elif maze[i + 1][j] == 5:
                        maze[i + 1][j] == 4
                        original[i + 1][j] == 4

                    elif maze[i][j + 1] == 5:
                        maze[i][j + 1] == 4
                        original[i][j + 1] == 4

                    else:
                        pass
    return maze

def move(maze, original):

    game_turn = 0
    
    while 1:
    
        if nb_prey(maze) == 0:
            break

        os.system("cls") # clear the terminal
        print_maze(maze)

        i, j = pos_hunter(maze)
        preys = pos_prey(maze)
        opened_doors = pos_opened_doors(original)

        for a in range(len(opened_doors)):

            if pos_hunter(maze) != opened_doors[a]:
                x, y = opened_doors[a]
                maze[x][y] = original[x][y]

            for z in range(len(preys)):

                if preys[z] != opened_doors[a]:
                    x, y = opened_doors[a]
                    maze[x][y] = original[x][y]

        if pos_departure(original) != pos_hunter(maze):
            x, y = pos_departure(original)
            maze[x][y] = original[x][y]

        if pos_exit(original) != pos_hunter(maze):
            x, y = pos_exit(original)
            maze[x][y] = original[x][y]

        if keyboard.read_key() == "z":

            if maze[i - 1][j] == 4:
                maze[i][j] = 1
                maze[i - 1][j] = 6

            elif maze[i - 1][j] == 1:
                maze[i][j] = 1
                maze[i - 1][j] = 6

            elif maze[i - 1][j] == 7:
                maze[i][j] = 1
                maze[i - 1][j] = 6

        elif keyboard.read_key() == "q":

            if maze[i][j - 1] == 4:
                maze[i][j] = 1
                maze[i][j - 1] = 6

            elif maze[i][j - 1] == 1:
                maze[i][j] = 1
                maze[i][j - 1] = 6

            elif maze[i][j - 1] == 7:
                maze[i][j] = 1
                maze[i][j - 1] = 6

        elif keyboard.read_key() == "s":

            if maze[i + 1][j] == 4:
                maze[i][j] = 1
                maze[i + 1][j] = 6

            elif maze[i + 1][j] == 1:
                maze[i][j] = 1
                maze[i + 1][j] = 6

            elif maze[i + 1][j] == 7:
                maze[i][j] = 1
                maze[i + 1][j] = 6

        elif keyboard.read_key() == "d":

            if maze[i][j + 1] == 4:
                maze[i][j] = 1
                maze[i][j + 1] = 6

            elif maze[i][j + 1] == 1:
                maze[i][j] = 1
                maze[i][j + 1] = 6

            elif maze[i][j + 1] == 7:
                maze[i][j] = 1
                maze[i][j + 1] = 6

        elif keyboard.read_key() == "c":

            if maze[i - 1][j] == 4:
                maze[i - 1][j] == 5
                original[i - 1][j] == 5

            elif maze[i][j - 1] == 4:
                maze[i][j - 1] == 5
                original[i][j - 1] == 5

            elif maze[i + 1][j] == 4:
                maze[i + 1][j] == 5
                original[i + 1][j] == 5

            elif maze[i][j + 1] == 4:
                maze[i][j + 1] == 5
                original[i][j + 1] == 5
            else:
                print("Pas OK")

        elif keyboard.read_key() == "o":

            if maze[i - 1][j] == 5:
                maze[i - 1][j] == 4
                original[i - 1][j] == 4

            elif maze[i][j - 1] == 5:
                maze[i][j - 1] == 4
                original[i][j - 1] == 4

            elif maze[i + 1][j] == 5:
                maze[i + 1][j] == 4
                original[i + 1][j] == 4

            elif maze[i][j + 1] == 5:
                maze[i][j + 1] == 4
                original[i][j + 1] == 4
            
            else:
                print("Pas OK")

        maze = actions_prey(maze, original, game_turn)
        game_turn += 1
    
    return 0
