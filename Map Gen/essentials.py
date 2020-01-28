import os
import pygame

from os import path

def lrange(a):
    return range(len(a))

def get_keys(keybinds):
    keys = pygame.key.get_pressed()
    keys_down = []

    for key in keybinds.keys():
        if keys[keybinds[key]]:
            keys_down.append(key)

    return keys_down

def get_keydown(keybinds):
    key_down = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            for key in keybinds.keys():
                if keybinds[key] == event.key:
                    key_down = key

    return key_down

def get_mouse_position():
    return pygame.mouse.get_pos()

def get_mouse_down():
    if pygame.mouse.get_pressed()[0]:
        return True
    else:
        return False

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def get_distance(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])
