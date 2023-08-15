import numpy as np
import time
class Tafl():

    def __init__(self):
        self.row_count = 11
        self.column_count = 11
        self.action_size = self.row_count * self.column_count
        self.board_size = 11
    
    def get_initial_state(self):
        return np.matrix([[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,-1,0,0,0,0,1], [1,0,0,0,-1,-1,-1,0,0,0,1], [1,1,0,-1,-1,-2,-1,-1,0,1,1],[1,0,0,0,-1,-1,-1,0,0,0,1], [1,0,0,0,0,-1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0]])
    
    def get_initial_valid_moves(self):
        pass

    def initial_valid_moves(self, state):
        valid_moves = []
        state = state.reshape(-1, 1)
        print(state)
        c = 0
        for i in range(len(state)):
            if state[i] != 0:
                pass

    def get_valid_moves(self, state, action):
        valid_moves = []
        state = state.reshape(-1, 1)
        print(state)
        

    def get_next_state(sefl, state, action, player):
        pass

    def is_valid_position(self, position):
        row, col = position
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def get_adjacent_positions(self, position):
        row, col = position
        adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        return [pos for pos in adjacent_positions if self.is_valid_position(pos)]
    
    def check_fortress(self, state):
        win = False
        king = np.argwhere(state == -2)[0]
        positions = self.get_adjacent_positions(king)
        while len(positions) > 0:
            for pos in positions:
                if state[pos] == 0:
                    if 11 in pos or 0 in pos:
                        win = True
                    state[pos] = -1
                    for p in self.get_adjacent_positions(pos):
                        positions.append(p)
                elif state[pos] == 1:
                    return False, win
                else:
                    positions.pop(positions.index(pos))
        return True, win
                

    def check_win(self, state, action):
        #TODO
        

        #King check

        king = np.where(state == 2)[0]
        if king == (0,0) or king == (0,11) or king == (11,0) or king == (11, 11):
            return True
        
        #Fortress check

        
            
            

                




    
    def get_opponent(self, player):
        return - player
    def get_opponent_value(self, value):
        return - value
    def change_perspective(self, state, player):
        return state * player
    def get_encoded_state(self, state):
        #Will change later
        encoded_state = np.stack(
            (state == -1, state == 0, state == 1)
        ).astype(np.float32)
        
        return encoded_state


t = Tafl()  

test1 = np.matrix([[0,0,0,1,1,1,1,1,0,0,0],
                   [0,0,0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0], 
                   [1,0,0,0,0,-1,0,0,0,0,1],
                   [1,0,0,0,-1,0,-1,0,0,0,1], 
                   [1,1,0,-1,0,0,-1,-1,0,1,1],
                   [1,0,0,0,-1,-1,-1,0,0,0,1], 
                   [1,0,0,0,0,-1,0,0,0,0,1],
                   [0,0,0,0,-1,0,0,0,0,0,0],
                   [0,0,0,-1,0,-0,0,0,0,0,0],
                   [0,0,-1,0,-2,0,-1,1,0,0,0]])

t.get_valid_moves(test1)