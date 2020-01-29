from terrain_tile import TerrainTile
from noise import snoise3
import random
from datetime import datetime


class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = []
        self.__generate_tiles(50)

    def __generate_tiles(self, frequency):
        random.seed(datetime.now())
        seed = random.random()
        base_map = self.__generate_base_map(frequency, seed)
        detail_map = self.__generate_detail_map(frequency, seed)
        for y in range(self.height):
            for x in range(self.width):
                index = (y*self.width)+x
                tile_value = (base_map[index]+detail_map[index])/2
                tile_type = ' '
                if tile_value < 0:
                    tile_type = '~'
                elif 0 < tile_value < 0.1:
                    tile_type = '/'
                elif 0.1 < tile_value < 0.6:
                    tile_type = '#'
                elif 0.6 < tile_value < 0.8:
                    tile_type = '^'
                else:
                    tile_type = '%'
                self.tiles.append(TerrainTile(x, y, 2, 2, tile_type))


    def __generate_base_map(self, frequency, seed):
        base_map = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                tile_value = snoise3(x / frequency, y / frequency, seed)
                base_map.append(tile_value)
        return base_map

    def __generate_detail_map(self,frequency, seed):
        detail_frequency = frequency/4
        detail_map = []
        for y in range(0, self.height):
            for x in range(0, self.width):
                tile_value = snoise3(x / detail_frequency, y / detail_frequency, seed+(seed/frequency))
                detail_map.append(tile_value)
        return detail_map

    def draw(self):
        [tile.draw() for tile in self.tiles]
