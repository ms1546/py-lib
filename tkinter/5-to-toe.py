import tkinter as tk
import tkinter.messagebox

class GomokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('五目並べ')
        self.board_size = 15
        self.cell_size = 40
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.canvas_size = self.board_size * self.cell_size
        self.canvas = tk.Canvas(self, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()
        self.init_board()
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.current_player = 'X'

    def init_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline='gray', fill='white')
                self.board[i][j] = ''

    def on_canvas_click(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.board[y][x] == '':
            self.draw_move(x, y, self.current_player)
            if self.check_win(y, x, self.current_player):
                tkinter.messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            tkinter.messagebox.showwarning("Invalid Move", "This position is already taken. Choose another.")

    def draw_move(self, x, y, player):
        x0 = x * self.cell_size + self.cell_size // 4
        y0 = y * self.cell_size + self.cell_size // 4
        x1 = x0 + self.cell_size // 2
        y1 = y0 + self.cell_size // 2
        color = 'black' if player == 'X' else 'white'
        self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)
        self.board[y][x] = player

    def check_win(self, y, x, player):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dy, dx in directions:
            count = 1
            for d in [1, -1]:
                step = 1
                while True:
                    new_x = x + dx * step * d
                    new_y = y + dy * step * d
                    if 0 <= new_x < self.board_size and 0 <= new_y < self.board_size and self.board[new_y][new_x] == player:
                        count += 1
                        step += 1
                    else:
                        break
            if count >= 5:
                return True
        return False

    def reset_game(self):
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.canvas.delete("all")
        self.init_board()
        self.current_player = 'X'

if __name__ == "__main__":
    app = GomokuApp()
    app.mainloop()
