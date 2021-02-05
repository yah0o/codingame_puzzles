import sys
import math

# https://www.codingame.com/ide/puzzle/the-descent
# Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.
# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
        fire_index = 0
        max_mountain_height = -1
        for i in range(8):
            mountain_h = int(input()) # represents the height of one mountain.
            if mountain_h > max_mountain_height:
                max_mountain_height = mountain_h
                fire_index = i
        # The index of the mountain to fire on.
        print(fire_index)
