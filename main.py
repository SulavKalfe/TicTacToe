import tkinter as tk
from tkinter import messagebox


class Hangman:
    def __init__(self):

        self.moves_done = 1
        self.player1_move = list()
        self.player2_move = list()
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.find_section)
        # self.canvas.bind("<Configure>", self.draw_grid)

    def game(self):
        self.root.mainloop()

    def find_section(self, event):
        self.moves_done+=1
        # print(self.moves_done)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        # print(width, height)

        row = int(event.y // (height/3))
        column = int(event.x // (width/3))

        section = row*3+column+1
        # print(f"Section: {section}")

        self.check_if_already_placed(self.moves_done, section, event)
        self.is_game_draw(self.moves_done)

    def check_if_already_placed(self, move_done, section, event):
        if section in self.player1_move or section in self.player2_move:
            self.moves_done-=1
            messagebox.showinfo("Invalid Position", "This spot is already taken.")
        else:
            self.check_whose_turn(move_done, section, event)

    def check_whose_turn(self, move_done, section, event):
        if move_done%2==0:
            self.draw_circle(self.get_position(event))
            self.player1_move.append(section)
            self.has_player_won(self.player1_move, 1)
            # print("Player 1 turn")
        else:
            self.draw_cross(self.get_position(event))
            self.player2_move.append(section)
            self.has_player_won(self.player2_move, 2)
        #     print("Player 2 turn")
        # print(f"P1 move :{self.player1_move}")
        # print(f"P2 move {self.player2_move}")

    def has_player_won(self, player_moves, player):
        winning_move= list()
        moves_to_win = [[1, 4, 7], [2, 5, 8], [3, 6, 9],
                        [1, 2, 3], [4, 5, 6], [7, 8, 9],
                        [1, 5, 9], [3, 5, 7]]
        for i in moves_to_win:
            for j in player_moves:
                if j in i:
                    winning_move.append(j)
            sortedlist = sorted(winning_move)
            # print(sortedlist)
            # print(i)
            if i == sortedlist:
                self.draw_winning_line(winning_move)
                messagebox.showinfo("Congratulations", f"Player {player} has won the game!")
                self.canvas.unbind('<Button-1>')
                self.root.destroy()

            else:
                winning_move = list()


    def is_game_draw(self, move_done):
    # print(move_done)
        chances = 9
        # print(f"moves: {move_done}")
        if chances < move_done:
            messagebox.showinfo("Draw", "The game is draw")
            self.canvas.unbind('<Button-1>')
            self.root.destroy()

    def get_position(self, event):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        row_size = width//3
        col_size = height//3

        pos_x = (event.x//row_size)*row_size
        pos_y = (event.y//col_size)*col_size

        centre_for_x = pos_x+row_size//2
        centre_for_y = pos_y+col_size//2

        return centre_for_x, centre_for_y

    def draw_circle(self, position):
        centre_for_x, centre_for_y = position
        self.canvas.create_oval(centre_for_x - 25, centre_for_y - 25, centre_for_x + 25, centre_for_y + 25, outline="black", width=2)

    def draw_cross(self, position):
        centre_for_x, centre_for_y = position
        self.canvas.create_line(centre_for_x - 20, centre_for_y - 20, centre_for_x + 20, centre_for_y + 20, fill="black", width=2)
        self.canvas.create_line(centre_for_x + 20, centre_for_y - 20, centre_for_x - 20, centre_for_y + 20, fill="black", width=2)

    def draw_winning_line(self, winning_list):
        section_row_column = {
            '1': [0, 0],
            '2': [0, 1],
            '3': [0, 2],
            '4': [1, 0],
            '5': [1, 1],
            '6': [1, 2],
            '7': [2, 0],
            '8': [2, 1],
            '9': [2, 2],
        }
        start_section = section_row_column[str(winning_list[0])]
        end_section = section_row_column[str(winning_list[-1])]
        # print(start_section, end_section)
        start_section_x, start_section_y = self.find_coords(start_section[0], start_section[1])
        end_section_x, end_section_y = self.find_coords(end_section[0], end_section[1])
        self.canvas.create_line(start_section_x, start_section_y, end_section_x, end_section_y, fill="black", width=2)


    def find_coords(self, row, column):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        # print(canvas_width, canvas_height)

        section_width = canvas_width // 3
        section_height = canvas_height // 3
        # print(section_width, section_height)

        centre_x = (column * section_width) + (section_width / 2)
        centre_y = (row * section_height) + (section_height / 2)

        return centre_x, centre_y


game1 = Hangman()
# x, y =game1.find_coords(3, 1)
game1.game()
# game1.draw_winning_line([1, 2, 3])
# print(x, y)