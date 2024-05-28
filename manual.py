
class ManualGame:

    def __init__(self, current_player):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = current_player

    def print_board(self):
        for row in self.board:
            print(row)

    def is_valid_index(self, index):
        if index < 0 and index > 6:
            return False
        if self.board[0][index] == 0:
            return True 
        return False

    def get_row(self, index):
        for i in range(5, -1, -1):
            if self.board[i][index] == 0:
                return i


    def make_move_for_player(self, index):
        empty_row = self.get_row(index)
        self.board[empty_row][index] = self.current_player


    def change_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def is_winner(self):

        print("Checking vertical....")
        # vertical |
        for c in range(7):
            count = 0
            for r in range(6):
                if self.board[r][c] == self.current_player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
    
        print("Checking horizontal....")
        # horizontal -
        for r in range(6):
            count = 0
            for c in range(7):
                if self.board[r][c] == self.current_player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0
                    
        print("Checking diagonal to right....")
        # diagonal /
        for r in range(0,3):
            temp_r = r
            for c in range(0, 3):
                temp_c = c
                count = 0
                while temp_r < 6 and temp_c < 7 and self.board[temp_r][temp_c] == self.current_player:
                    print(f"{temp_r},{temp_c} :: {self.current_player}")
                    temp_c += 1
                    temp_r += 1
                    count += 1
                    print(f"u{temp_r},{temp_c} :: {self.current_player}")
                if count == 4:
                        return True
                else:
                    count = 0
                    
        
        print("Checking diagonal to left....")
        # diagonal \
        for r in range(0,3):
            temp_r = r
            for c in range(6, 2, -1):
                temp_c = c
                count = 0
                while temp_r < 6 and temp_c > -1 and self.board[temp_r][temp_c] == self.current_player:
                    print(f"{temp_r},{temp_c} :: {self.current_player}")
                    temp_r += 1
                    temp_c -= 1
                    count += 1
                    print(f"uu{temp_r},{temp_c} :: {self.current_player}")
                if count == 4:
                    return True
                else:
                    count = 0
                    


    def play(self):

        while True:
            
            print(f"Player {self.current_player} turn")
            index = int(input("Enter column range from 1 to 7::"))

            while not self.is_valid_index(index - 1):
                print(f"HERE: {index - 1}")
                index = int(input("Enter column range from 1 to 7::"))
                
            self.make_move_for_player(index - 1)
            self.print_board()
            if self.is_winner():
                print(f"{self.current_player} WON")
                break
            self.change_player()
                

player = int(input("enter current player::"))

manualGame = ManualGame(player)
manualGame.play()