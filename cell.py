from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    all_cells = []
    cell_count = settings.cell_amount
    cell_count_label = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_flagged = False
        self.cell_btn = None
        self.x = x
        self.y = y

        # append the object to the Cell.all list
        Cell.all_cells.append(self)

    def create_btn(self, location):
        btn = Button(
            location,
            width=settings.button_width,
            height=settings.button_height,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg=settings.background_colour,
            fg=settings.foreground_colour,
            text=f"Cells Remaining:{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mine amount equals the cells left amount, player won
            if Cell.cell_count == settings.mine_amount:
                ctypes.windll.user32.MessageBoxW(0, 'You Win!', 'Game Over', 0)
        # cancel click if opened
        self.cell_btn.unbind('<Button-1>')
        self.cell_btn.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # return cell x and y value
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn.configure(text=self.surrounded_cells_mines_length)
            # update cell amount
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(
                    text=f"Cells Remaining:{Cell.cell_count}"
                )
            # return button colour
            self.cell_btn.configure(
                bg='SystemButtonFace'
            )
        self.is_opened = True

    def show_mine(self):
        self.cell_btn.configure(bg=settings.mine_colour)
        ctypes.windll.user32.MessageBoxW(0, 'You stepped on a mine', 'Game Over', 0)
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_flagged:
            self.cell_btn.configure(
                bg=settings.flag_colour
            )
            self.is_flagged = True
        else:
            self.cell_btn.configure(
                bg=settings.background_colour
            )
            self.is_flagged = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all_cells, settings.mine_amount
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
