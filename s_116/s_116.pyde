# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
from berin.grids import *
from random import choice
from collections import namedtuple


WHITE = color(235)
BLACK = color(27, 27, 27)
RED = color(212, 32, 10)


def setup():
    size(900, 900)
    strokeWeight(2)
    noFill()
    frameRate(2)
    rectMode(CENTER)
    stroke(WHITE)
    noFill()
    smooth()


def small_rect():
    rectMode(CORNER)
    rect(-20, -20, 20, 20)
    rectMode(CENTER)


FUNCTIONS = [
    (ellipse, 0, 0, 40, 40),
    (rect, 0, 0, 40, 40),
    (triangle, -20, -20, 20, 20, -20, 20),
    (line, -20, -20, 20, 20),
    (arc, 0, 0, 40, 40, 0, PI, PIE),
    (triangle, -20, -20, 0, 0, 20, -20),
    (arc, 0, 0, 40, 40, 0, HALF_PI, PIE),
    (small_rect,),
    (ellipse, 0, -10, 20, 20),
    (line, -20, -20, 0, 0),
]


def draw_random_function(function_i, angle=0):
    half_size = 25
    with pushMatrix():
        translate(half_size, half_size)
        rotate(angle)
        data = FUNCTIONS[function_i]
        func, args = data[0], data[1:]
        func(*args)


def random_internal_grid():
    elem_size = 50
    num_rows = int(random(3, 7))
    grids = [
        VirtualGrid(0, 0, num_rows, elem_size),
        EvenColumnsGrid(0, 0, num_rows, elem_size),
        OddLinesGrid(0, 0, num_rows, elem_size),
        DiagonalsOnlyGrid(0, 0, num_rows, elem_size),
        RandomPositioningGrid(0, 0, num_rows, elem_size, percent=0.82),
    ]
    colors = [
        WHITE,
        color(255, 255, 0),
        #color(255 / 2, 255, 0),
        #color(255, 255 / 2, 0),
        #color(255 / 2, 255 / 2, 0),

        color(255, 0, 255),
        #color(255, 0, 255 / 2),
        #color(255 / 2, 0, 255),
        #color(255 / 2, 0, 255 / 2),

        color(0, 255, 255),
        #color(0, 255, 255 / 2),
        #color(0, 255 / 2, 255),
        #color(0, 255 / 2, 255 / 2),
    ]
    index = int(random(len(FUNCTIONS)))
    if index < len(FUNCTIONS) / 2.0 + 1:
        stroke(BLACK)
    else:
        stroke(RED)

    angle = choice([0, HALF_PI, PI, 3 * HALF_PI])

    grid = choice(grids)
    grid.draw(draw_random_function, index, angle)


def draw():
    background(WHITE)

    elem_size = 50
    num_rows = width / elem_size + 1
    main_grid = RandomPositioningGrid(0, 0, num_rows, elem_size, percent=0.9)
    main_grid.draw(random_internal_grid)

    print(frameCount)
    saveFrame("######.png")
    noLoop()


def keyPressed():
    if key == 'n':
        redraw()
