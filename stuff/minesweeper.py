import random
import re
import math

class Board:
    
    def __init__(self, size, no_of_bomb):
        
        self.size = size
        self.no_of_bomb = no_of_bomb
        self.board = self.make_new_board()
        self.assign_value_to_board()
        self.dug = set()
        
    def make_new_board(self):
        
        board = [[None for _ in range(self.size)] for _ in range(self.size)]
        plant_bomb = 0
        
        while plant_bomb < self.no_of_bomb:
            
            location = random.randint(0, math.pow(self.size, 2) - 1)))
            row = location // self.size
            col = location % self.size
            
            if board[row][col] == '*':
                
                continue
            
            board[row][col] = '*'
            plant_bomb += 1
            
        return board