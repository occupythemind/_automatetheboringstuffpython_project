import sys

# Best Tic-Tac-Toe game in he world.

# Exceptions to raise
class InvalidMoveError(Exception): #For an invalid move
    pass

class TicTacToe():
    def __init__(self):
        # ' X ' is red while ' O ' is blue 
        self.msg = "\033[92m BesT TicTacToe Game in the World\033[0m\n\
            Just comply with the games rules and at any point hit 'q' to quit"
        self.board = {'top-L':'   ', 'top-M':'   ', 'top-R':'   ',
                'mid-L':'   ', 'mid-M':'\033[91m X \033[0m', 'mid-R':'   ',
                'low-L':'   ', 'low-M':'   ', 'low-R':'   '}
    
    def print_gameplay(self):
        # a b c, 0 1 2 represent the co-ordinates for a gameplay
        print(f"\033[90m{self.board['top-L']}|{self.board['top-M']}|{self.board['top-R']}\033[0m   2")
        print("\033[90m---+---+---\033[0m")
        print(f"\033[90m{self.board['mid-L']}|{self.board['mid-M']}|{self.board['mid-R']}\033[0m   1")
        print("\033[90m---+---+---\033[0m")
        print(f"\033[90m{self.board['low-L']}|{self.board['low-M']}|{self.board['low-R']}\033[0m   0")
        print(f"\na    b    c    ")

    def play(self):
        # User implements choice
        while True:
            try:
                tac = input("\n\033[95mChoose your play(X or O)?\n>> \033[0m")
                if tac.lower() == 'x':
                    tac = '\033[91m X \033[0m'
                    msgI = "\n\033[91mEnter the co-ordinates of your move(eg. a1 for 1st upper left row)\n>> \033[0m" #Red color input
                elif tac.lower() == 'o':
                    tac = '\033[94m O \033[0m'
                    msgI = "\n\033[94mEnter the co-ordinates of your move(eg. a1 for 1st upper left row)\n>> \033[0m" #Blue color input
                elif tac.lower() == 'q':
                    sys.exit()
                else:
                    raise ValueError(f"Unsupported value, expecting X or O but got '{tac}'")
                
                return tac, msgI
                break
            except ValueError:
                print(f"ValueError: Unsupported value, expecting X or O but got '{tac}'")
                continue
            except KeyboardInterrupt:
                sys.exit()
            except EOFError:
                sys.exit()
            
    def move(self, tac, msg):
        # Move by the co-ordinates
        
        move = input(msg).lower()
        if move == 'a2':
            self.board['top-L'] = tac
        elif move == 'a1':
            self.board['mid-L'] = tac
        elif move == 'a0':
            self.board['low-L'] = tac
        elif move == 'b2':
            self.board['top-M'] = tac
        elif move == 'b1':
            self.board['mid-M'] = tac
        elif move == 'b0':
            self.board['low-M'] = tac
        elif move == 'c2':
            self.board['top-R'] = tac
        elif move == 'c1':
            self.board['mid-R'] = tac
        elif move == 'c0':
            self.board['low-R'] = tac
        elif move.lower() == 'q':
            sys.exit()
        else:
            raise InvalidMoveError(f"Unsupported value, expecting a1, a2, a3, b1, b2, b3, c1, c2, c3 but got '{move}'")

if __name__ == '__main__':
    game = TicTacToe()
    game.msg
    game.print_gameplay()
    tact = game.play()
    tac, msg = tact[0], tact[1]
    while True:
        try:
            game.move(tac, msg)
            game.print_gameplay()
        except InvalidMoveError:
            print("InvalidMove: Doesn't count")
            continue
        except KeyboardInterrupt:
            sys.exit()
        except EOFError:
            sys.exit()


