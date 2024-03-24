from maze import *

def main():
    maze = set_maze_complete()
    original = set_maze_original()
    move(maze, original)

main()