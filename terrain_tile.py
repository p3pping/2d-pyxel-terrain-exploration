import pyxel


class TerrainTile:

    def __init__(self, x, y, width, height, area):
        self.area = area
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @staticmethod
    def area_types():
        return {
            '~': 1,
            '/': 10,
            '#': 3,
            '^': 5,
            '%': 6
        }

    def set_type(self, area_type):
        self.area = area_type

    def draw(self):
        x_position = self.x*self.width
        y_position = self.y*self.height
        terrain_color = TerrainTile.area_types()[self.area]
        pyxel.rect(x_position, y_position, x_position+self.width, y_position+self.height, terrain_color)
