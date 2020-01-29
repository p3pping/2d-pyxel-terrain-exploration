import pyxel
from world import World

width = 160
height = 120

pyxel.init(width, height)

world = World(int(width/2), int(height/2))


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(0)
    world.draw()


pyxel.run(update, draw)
