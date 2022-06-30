window_width = 1000
window_height = 600
grid_size = 6
cell_amount = grid_size ** 2
mine_amount = cell_amount // 4

button_width = 12
button_height = 4

background_colour = '#4287f5'
foreground_colour = '#ddf0f0'
mine_colour = '#f54242'
flag_colour = '#f5a742'
button_colour = 'SystemButtonFace'


def height_pc(pc):
    return (window_height / 100) * pc


def width_pc(pc):
    return (window_width / 100) * pc

