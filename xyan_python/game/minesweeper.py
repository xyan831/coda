# import module
import random
import pandas as pd

# minesweeper game
class MineSweeper:
    def __init__(self):
        self.streak = [0,0]     # [current, all-time]

        self.df = 0             # difficulty
        self.size = 0           # board size [h(row), w(col)]
        self.mine = 0           # number of mines
        self.board_now = 0      # current board
        self.board_map = 0      # solution
        self.mine_coord = 0     # coordinates of mines
        self.stat = 0           # current game status

    def play(self):
        # initialize
        self.set_df()
        self.set_board()
        # play game
        self.stat = "play"
        print(self.board_now)
        while self.stat=="play":
            print("input format: type x y (quit/exit to end game)")
            print(f"type: mine/flag, x:(0-{self.size[1]-1}), y:(0-{self.size[0]-1})")
            self.stat = self.process()
            print(self.board_now)
        # check stat
        self.check_stat
        # if play again
        self.play_again()

    def check_stat(self):
        if self.stat=="exit":
            print("exit game")
        elif self.stat=="win":
            print("you win!")
            self.streak[0]+=1
            if self.streak[0]>self.streak[1]:
                self.streak[1] = self.streak[0]
            print(f"current streak: {self.streak[0]} | max streak: {self.streak[1]}")
        elif self.stat=="lose":
            print("you lose")
            self.streak[0] = 0
        else:
            print("error")
        # reset stat
        self.stat = 0

    def play_again(self):
        print("play again?[y/n] change diffuculty?[y/n]")
        ipt = input("input: ").split(" ")
        if ipt[0]==("yes" or "y"):
            if ipt[1]==("yes" or "y"):
                self.df = 0
            self.play()
        else:
            print("ok bye bye~")

    def set_df(self):
        if self.df!=("easy" or "medium" or "hard"):
            print("set difficulty [easy/medium/hard]")
            df = input("input: ")
        if df==("easy" or "e"):
            print("set easy")
            self.df = "easy"
            self.size = [8,8]
            self.mine = 8
        elif df==("medium" or "m"):
            print("set medium")
            self.df = "medium"
            self.size = [9,10]
            self.mine = 15
        elif df==("hard" or "h"):
            print("set hard")
            self.df = "hard"
            self.size = [9,14]
            self.mine = 27
        else:
            print("default set medium")
            self.df = "medium"
            self.size = [9,10]
            self.mine = 15

    def set_board(self):
        height, width = self.size
        board = [["_" for _ in range(width)] for _ in range(height)]
        self.board_now = pd.DataFrame(board)
        self.board_map = pd.DataFrame(board)
        all_coord = [[x,y] for y in range(height) for x in range(width)]
        self.mine_coord = random.sample(all_coord, self.mine)
        for x, y in all_coord:
            if [x,y] in self.mine_coord:
                self.board_map.loc[y,x] = "*"
            else:
                mine = 0
                neighbor = self.get_neighbor(x, y)
                for nx, ny in neighbor:
                    if [nx,ny] in self.mine_coord:
                        mine+=1
                self.board_map.loc[y,x] = mine
        #print(self.board_map)

    def get_neighbor(self, x, y):
        height, width = self.size
        neighbor = []
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dx==0 and dy==0:
                    continue
                nx,ny = x+dx, y+dy
                if 0<=nx<width and 0<=ny<height:
                    neighbor.append([nx,ny])
        return neighbor

    def process(self):
        ipt = input("input: ")
        if ("quit" or "exit") in ipt:
            return "exit"
        ipt = ipt.split(" ")
        type = ipt[0]
        x_str = ipt[1]
        y_str = ipt[2]
        try:
            x = int(x_str)
            y = int(y_str)
            if (x or y)<0 or x>(self.size[1]-1) or y>(self.size[0]-1):
                print(f"out of range, x:(0-{self.size[1]-1}), y:(0-{self.size[0]-1})")
                return "play"
        except ValueError:
            print("invalid input: input integer for (x,y)")
            return "play"
        if self.board_now.loc[y,x]!="_":
            print("not blank place, if flag need unflag")
            return "play"
        if type=="mine":
            self.board_now.loc[y,x]=self.board_map.loc[y,x]
            if self.board_map.loc[y,x]=="*":
                print("touch bomb oh no")
                return "lose"
            elif self.board_map.loc[y,x]==0:
                self.reveal_zero(x, y)
            return self.check_win()
        elif type=="flag":
            if self.board_now.loc[y,x]=="#":
                self.board_now.loc[y,x] = "_"
            else:
                self.board_now.loc[y,x] = "#"
        else:
            print("invalid type: use mine/flag")
        return "play"

    def reveal_zero(self, x, y):
        height, width = self.size
        visited = set()
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            # Reveal current cell
            self.board_now.loc[cy, cx] = self.board_map.loc[cy, cx]
            # If it's 0, keep revealing neighbors
            if self.board_map.loc[cy, cx] == 0:
                for nx, ny in self.get_neighbor(cx, cy):
                    if self.board_now.loc[ny, nx] == "_":
                        stack.append((nx, ny))

    def check_win(self):
        height, width = self.size
        for y in range(height):
            for x in range(width):
                if self.board_map.loc[y, x] != "B" and self.board_now.loc[y, x] == "_":
                    return "play"
        return "win"

if __name__ == "__main__":
    # start game
    game = MineSweeper()
    game.play()

