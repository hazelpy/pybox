import camera

from essentials import *
from camera import Camera

class Grid:
    y_list: list
    cell_width: float
    cell_height: float

    def __init__(self, width: int=10, height: int=10, cell_width=32, cell_height=32):
        self.cell_width, self.cell_height = cell_width, cell_height
        self.y_list = []

        for y in range(height):
            self.y_list.append([])

            for x in range(width):
                self.y_list[y].append(-1)

    def print_x(self):
        result = ""

        for value in self.y_list:
            for x in value:
                result += str(x) + " "

            result += "\n"

        print(result)

    def replace_all(self, a: int, b: int):
        for y in range(len(self.y_list)):
            for x in range(len(self.y_list[y])):
                if self.y_list[y][x] is a:
                    self.y_list[y][x] = b

    def set_tile(grid, position, tile):
        grid.y_list[position[1]][position[0]] = tile
        return True

    def get_grid_collisions(self, rect, camera):
        for y in lrange(self.y_list):
            for x in lrange(self.y_list[y]):
                tile_at_position = self.y_list[y][x]

                camera_space = grid_to_camera_space(camera, self, (x, y))
                if rect.colliderect(pygame.Rect(camera_space[0], camera_space[1], self.cell_width, self.cell_height)):
                    if self.y_list[y][x] != -1:
                        return (x, y)

def make_grid(width: int=10, height: int=10):
    return Grid(width, height)

def camera_to_grid_space(camera, grid, position):
    x, y = position[0], position[1]

    camera_x_difference = camera.x_min - camera.x
    camera_y_difference = camera.y_min - camera.y

    absolute_x = x - camera_x_difference
    grid_x = absolute_x / grid.cell_width

    absolute_y = y - camera_y_difference
    grid_y = absolute_y / grid.cell_height

    absolute_x, absolute_y, grid_x, grid_y = int(absolute_x), int(absolute_y), int(grid_x), int(grid_y)
    return ((absolute_x, absolute_y), (grid_x, grid_y))

def grid_to_camera_space(camera, grid, space):
    camera_pos = (camera.x, camera.y)
    grid_x = grid.cell_width * space[0]
    grid_y = grid.cell_height * space[1]

    absolute_x, absolute_y = grid_x - camera_pos[0], grid_y - camera_pos[1]
    return (absolute_x, absolute_y)

def save_grid_data(grid):
    data = ""

    for y in range(len(grid.y_list)):
        for x in range(len(grid.y_list[y])):
            data += str(grid.y_list[y][x])
            if x != len(grid.y_list[y]) - 1:
                data += ";"
        if y != len(grid.y_list) - 1:
            data += ":"

    return data

def load_grid_data(data):
    y_data = data.split(":")

    height = len(list(find_all(data, ":"))) + 1
    width = len(list(find_all(y_data[0], ";"))) + 1

    grid = Grid(width, height)

    for value in lrange(y_data):
        for x in lrange(y_data[value].split(";")):
            grid.y_list[value][x] = int(y_data[value].split(";")[x])

    return grid
