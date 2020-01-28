import gridgenerator as gg
import pygame
import os
import camera

from camera import make_camera, Camera
from os import path
from essentials import *
from gridgenerator import Grid, camera_to_grid_space

#################
## P Y G A M E ##
#################

def get_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    return False

pygame.init()

KEYBINDS = {
    "move_left": pygame.K_a or pygame.K_LEFT,
    "move_right": pygame.K_d or pygame.K_RIGHT,
    "move_up": pygame.K_w or pygame.K_UP,
    "move_down": pygame.K_s or pygame.K_DOWN,
    "select": pygame.K_q
}

screen_size = (1024, 576)
screen = pygame.display.set_mode(screen_size)

#################
## C A M E R A ##
#################

camera: Camera = make_camera(y=(32*12), x_min=0, x_max=512, y_min=0, y_max=192)

#################
## P L A Y E R ##
#################

import playermaker
from playermaker import *

PlayerObject = Player(0, 0, 32, 32, "resources/sprites/player.png")

#############
## G R I D ##
#############

grid: Grid = gg.make_grid(48, 32)

for e in range(10):
    for k in lrange(grid.y_list[e]):
        grid.y_list[len(grid.y_list) - 11 + e][k] = 0

g_data = gg.save_grid_data(grid)
loaded_grid = gg.load_grid_data(g_data)

#############
## M A P S ##
#############

BG_COLOR = (200, 200, 250)
maps = [loaded_grid]

###############
## T I L E S ##
###############

ROOT_TILE_DIRECTORY = "resources/tiles/"

GAME_ESSENTIAL_TILES = {
    -1: ROOT_TILE_DIRECTORY + "blank",
    0: ROOT_TILE_DIRECTORY + "grass",
    1: ROOT_TILE_DIRECTORY + "wall"
}

GAME_TILE_IMAGES: dict = {}

def load_images():
    for key in GAME_ESSENTIAL_TILES.keys():
        if path.isfile(os.curdir + "/" + GAME_ESSENTIAL_TILES[key] + ".png"):
            print("Found file:", GAME_ESSENTIAL_TILES[key] + ".png")
            GAME_TILE_IMAGES[key] = pygame.image.load(os.curdir + "/" + GAME_ESSENTIAL_TILES[key] + ".png")
        else:
            print("Did not find file at:", os.curdir + "/" + GAME_ESSENTIAL_TILES[key] + ".png")

load_images()

TILE_GRASS, TILE_WOOD = 0, 1

def select_tile():
    a = input()
    if int(a) in GAME_TILE_IMAGES:
        return int(a)
    else:
        return false

#######################
## R E N D E R I N G ##
#######################

current_map = maps[0]
COMMON_CELL_SIZE = 32

def draw_map():
    global current_map, GAME_TILE_IMAGES, COMMON_CELL_SIZE

    for y_index in lrange(current_map.y_list):
        current_y_list = current_map.y_list[y_index]

        for x in lrange(current_y_list):
            if current_y_list[x] in GAME_TILE_IMAGES:
                screen.blit(GAME_TILE_IMAGES[current_y_list[x]], ((x * COMMON_CELL_SIZE) - camera.x, (y_index * COMMON_CELL_SIZE) - (camera.y * 2)))

#################
## S C R E E N ##
#################

running = True
selected_tile = 1

while running:
    camera.moveto((PlayerObject.x - (0.5 * 1024), PlayerObject.y - (0.5 * 576)))

    # player_camera_difference = get_distance((camera.x, camera.y), (PlayerObject.x, PlayerObject.y))
    # camera.move("right", player_camera_difference[0])
    # camera.move("up", player_camera_difference[1])

    for key in get_keys(KEYBINDS):
        if key == "move_left":
            PlayerObject.move("left", 4)
        elif key == "move_right":
            PlayerObject.move("right", 4)
        elif key == "move_up":
            PlayerObject.move("up", 4)
        elif key == "move_down":
            PlayerObject.move("down", 4)

    if "select" == get_keydown(KEYBINDS):
        if selected_tile == -1:
            selected_tile = 1
        else:
            selected_tile = -1

    if get_mouse_down():
        mouse_pos = get_mouse_position()
        points = camera_to_grid_space(camera, grid, mouse_pos)
        current_map.set_tile(points[1], selected_tile)

    if get_exit():
        running = False
        pygame.quit()
        continue

    current_map.get_grid_collisions(pygame.Rect(PlayerObject.x, PlayerObject.y, PlayerObject.width, PlayerObject.height), camera)

    screen.fill(BG_COLOR)
    draw_map()
    PlayerObject.draw(screen, camera)

    pygame.display.update()
