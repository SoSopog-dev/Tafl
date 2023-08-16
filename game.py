import numpy as np
import time
from itertools import repeat
from random import randint


class Tafl():
    def __init__(self):
        self.row_count = 11
        self.column_count = 11
        self.action_size = self.row_count * self.column_count
        self.board_size = 11
    
    def get_initial_state(self):
        return np.matrix([[0,0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,-1,0,0,0,0,1], [1,0,0,0,-1,-1,-1,0,0,0,1], [1,1,0,-1,-1,-2,-1,-1,0,1,1],[1,0,0,0,-1,-1,-1,0,0,0,1], [1,0,0,0,0,-1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,1,0,0,0]])

    def get_initial_valid_moves(self, state, player):
        valid_moves = []
        state = state.reshape(1, -1)
        c = 0
        len_state = 120 - 1#TODO fix this 
        for i in range(len_state):
            if player == -1:
                white = True
            else:
                white = False
            if state[0,i] == player or (white and state[0,i]):
                c = i
                s = True
                while (c - 11) > -1 and s == True:
                    c -= 11 
                    if state[0,c] == 0:
                        valid_moves.append((i,c))
                    else:
                        s = False
                c = i
                s = True
                while (c + 11) < len_state and s == True:
                    c += 11
                    if state[0,c] == 0:
                        valid_moves.append((i,c))
                    else:
                        s = False
                c = i
                s = True
                while (c+1)//11 == i//11 and s == True:
                    c += 1
                    if state[0,c] == 0:
                        valid_moves.append((i,c))
                    else:
                        s = False
                c = i
                s = True
                while (c-1)//11 == i//11 and s == True:
                    c -= 1
                    if state[0,c] == 0:
                        valid_moves.append((i,c))
                    else:
                        s = False
        return valid_moves  
                
                
    def get_valid_moves(self, state, action):
        #TODO
        valid_moves = []
        state = state.reshape(-1, 1)
        
        a = action[0]
        b = action[1]
        a_col = a//11
        a_row = a%11
        



    def check_for_captures(self, state, action):
        remove = []
        state = state.reshape(1, -1)
        b = action[1]
        b_t = state[0,b]
        if b - 1 > 0  and (b-2)//11 == b//11 and state[0,b-1] == -b_t and state[0,b-2] == b_t:
            remove.append(b-1)
        if b + 1 < 120 - 1 and(b+2)//11 == b//11  and state[0,b+1] == -b_t and state[0,b+2] == b_t:
            remove.append(b+1)
        if b - 11 > 11  and state[0,b-11] == -b_t and state[0,b-22] == b_t:
            remove.append(b-11)
        if b + 11 < 120 - 11  and state[0,b+11] == -b_t and state[0,b+22] == b_t:
            remove.append(b+11)
        return remove


    def get_next_state(self, state, action):
        print(f"\n {state}\n")
        state = state.reshape(1,-1)
        print(f" this is the action: {action}, \n {state} \n")
        print(action[0])
        p = state[0,action[0]]
        print(p)
        state[0,action[0]] = 0
        state[0, action[1]] = p
        remove = self.check_for_captures(state, action)
        print(f"\n {state}\n")
        for r in remove:
            state[0,r] = 0
        state = state.reshape(11, 11)
        return state

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
                

    def check_win(self, state, action, player):

        n_state = self.get_next_state(state, action)
        print(f" \n ---\n {n_state} \n --- \n")
        king = np.argwhere(n_state == -2)[0]
        print(king)
        #King check
        if player == -1:
            corner_positions = [[0, 0], [0, 11], [11, 0], [11, 11]]
            if any((king == corner).all() for corner in corner_positions):
                print("The king has escaped")
                return True
            if self.check_fortress(n_state)[1]:
                print("The king has a fortress")
                return True
            return False

        else:
            print(f"ello ninos \n ___ \n{state}\n ___ \n")
            lst = self.get_adjacent_positions(king)
            lst = [n_state[i[0], i[1]] for i in lst]
            print(lst)
            if player in lst and len(lst) == 4:
                repeated = list(repeat(lst[0], len(lst)))
                if repeated == lst:
                    print("Da king is dead")
                    return True # The king is mated 
                else:
                    return False
            else:
                return False


    
    def get_opponent(self, player):
        return - player
    def get_opponent_value(self, value):
        return - value
    def change_perspective(self, state, player):
        return state * player
    def get_value_and_terminated(self, state, action, player):
        if self.check_win(state, action, player):
            return 1, True
        return 0, False
        
    def get_encoded_state(self, state):
        #Will change later
        encoded_state = np.stack(
            (state == -1, state == 0, state == 1)
        ).astype(np.float32)
        
        return encoded_state


t = Tafl()  

test1 = np.matrix([[ 0,-2, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
                   [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [ 0, 0, 0, 0, 0, 0, 0,-1, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

#print(t.get_initial_valid_moves(test1, 1))

#print(t.get_next_state(test1, (3,14)))
state = test1
#t.get_initial_state()
run = True
player = 1
while run:
    if player == -1:
        a = int(input())
        b = int(input())
        action = (a,b)
        n_state = state.copy()
        result = t.get_value_and_terminated(n_state, action, player)
        print(result)

        print(f"--------------------------------\n this is after the result \n --------------------------------\n")

        state = t.get_next_state(state, action)
        
        if result[1]:
            print("White has won")
            run = False
    else:
        moves = t.get_initial_valid_moves(state, player)
        print(moves)
        r = randint(0, len(moves))
        result = t.get_value_and_terminated(state, moves[r], player)
        state = t.get_next_state(state, moves[r])
        
        if result[1]:
            print("Black has won")
            run = False
    print(state)
    player *= -1
