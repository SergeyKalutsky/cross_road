import os
import pgzrun
from random import randint, choice


TITLE = 'CROSS THE ROAD'
WIDTH = 480
HEIGHT = 700

# Загрузка изображений
roads = [Actor('road', topleft=(80, 0)), Actor('road', topleft=(240, 0))]
grasses = [Actor('grass', topleft=(0, 0)), Actor('grass', topleft=(400, 0))]
chicken = Actor('chicken', (43, 650))
cars = ['car_white', 'car_blue', 'big_track', 'track',
        'car_yellow', 'car_red', 'car_cyan', 'car_grey']

car = Actor(choice(cars), (43+40*randint(1, 4), 650))

def draw():
    for grass in grasses:
        grass.draw()
    for road in roads:
        road.draw()
    chicken.draw()
    car.draw()


def update(dt):
    if keyboard.UP:
        if chicken.y > 40:
            chicken.y -= 5
    if keyboard.DOWN:
        if chicken.y < HEIGHT - 40:
            chicken.y += 5
    car.y -= 6
    if car.bottom < 0:
        car.x = 43+80*randint(1, 4)
        car.top = 700
        car.image = choice(cars)


def on_mouse_down(button, pos):
    pass


def on_mouse_up(button, pos):
    pass


def on_mouse_move(pos):
    pass


def on_key_down(key):
    if key == keys.RIGHT:
        if chicken.x < WIDTH - 43:
            chicken.x += 80
    if key == keys.LEFT:
        if chicken.x > 43:
            chicken.x -= 80


def on_key_up(key):
    pass


pgzrun.go()
