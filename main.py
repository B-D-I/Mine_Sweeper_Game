from tkinter import *
from cell import Cell
import settings


root = Tk()
root.configure(bg=settings.background_colour)
root.geometry(f'{settings.window_width}x{settings.window_height}')
root.resizable(False, False)
root.title("Minesweeper")

top_frame = Frame(
    root,
    bg=settings.background_colour,
    width=settings.window_width,
    height=settings.height_pc(25)
)
top_frame.place(x=50, y=0)

game_title = Label(
    top_frame,
    bg=settings.background_colour,
    fg=settings.foreground_colour,
    text='Mine-sweeper',
    font=('', 45)
)
game_title.place(
    x=settings.width_pc(25), y=0
)

left_frame = Frame(
    root,
    bg=settings.background_colour,
    width=settings.width_pc(45),
    height=settings.height_pc(75)
)
left_frame.place(x=10, y=settings.height_pc(25))

center_frame = Frame(
    root,
    bg=settings.background_colour,
    width=settings.width_pc(75),
    height=settings.height_pc(75)
)
center_frame.place(
    x=settings.width_pc(40),
    y=settings.height_pc(25),
)
for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn(center_frame)
        c.cell_btn.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(
    x=0, y=0
)

Cell.randomize_mines()

root.mainloop()
