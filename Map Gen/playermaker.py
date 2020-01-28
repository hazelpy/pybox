import gridgenerator
import essentials
import pygame
import os

from os import path

up, down, left, right = "up", "down", "left", "right"
class Player:
    x, y, width, height = 0, 0, 0, 0

    def __init__(self, x, y, width, height, sprite_path):
        self.x, self.y, self.width, self.height = x, y, width, height

        if path.isfile(sprite_path):
            self.sprite = pygame.image.load(sprite_path)

    def draw(self, screen, camera):
        screen.blit(self.sprite, (self.x - camera.x, self.y - camera.y))

    def move(self, dir, speed):
        if dir == right:
            self.x += speed
        elif dir == left:
            self.x -= speed
        elif dir == up:
            self.y -= speed
        elif dir == down:
            self.y += speed
