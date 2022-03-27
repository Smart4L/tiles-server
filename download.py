import os
import sys
import requests
from time import sleep
import math

class Tile:
    def __init__(self, z, x, y):
        self.z = z
        self.x = x
        self.y = y

def latLngToTileXYForZoom(lat, lng, z):
    n = math.pow(2, z)
    x = n * ((lng + 180) / 360)
    latRad = lat * 2 * math.pi /360
    y = n * (1 - (math.log(math.tan(latRad) + 1 / math.cos(latRad)) / math.pi)) / 2
    return [math.floor(x), math.floor(y)]

def list_tiles(left, bottom, right, top, zoom_min, zoom_max):
    tiles = []

    for z in range(zoom_min, zoom_max + 1 , 1):
        coords1 = latLngToTileXYForZoom(top, left, z)
        coords2 = latLngToTileXYForZoom(bottom, right, z)
        if coords1[0] == coords2[0]:
            coords2[0] +1
        
        if coords1[1] == coords2[1]:
            coords2[1] +1

        x1 = min([coords1[0], coords2[0]])
        x2 = max([coords1[0], coords2[0]])
        y1 = min([coords1[1], coords2[1]])
        y2 = max([coords1[1], coords2[1]])

        for x in range(x1, x2 + 1 , 1):
            for y in range(y1, y2 + 1, 1):
                tile = Tile(z, x, y)
                tiles.append(tile)

    print(f'Numbers of tiles: {len(tiles)}')
    return tiles


def download_tile(left, bottom, right, top, zoom_min, zoom_max):
    for tile in list_tiles(left, bottom, right, top, zoom_min, zoom_max):

        if(os.path.isfile(f'tiles/{tile.z}-{tile.x}-{tile.y}.png')):
            print(f'File already exists: {tile.z}-{tile.x}-{tile.y}')
        
        else:
            sleep(0.2)
            img_data = requests.get(f'https://tile.openstreetmap.org/{tile.z}/{tile.x}/{tile.y}.png').content
            with open(f'tiles/{tile.z}-{tile.x}-{tile.y}.png', 'wb') as handler:
                handler.write(img_data)
                print(f'Tile {tile.z}-{tile.x}-{tile.y}.png')



input_left = float(sys.argv[1])
input_bottom = float(sys.argv[2])
input_right = float(sys.argv[3])
input_top = float(sys.argv[4])
input_min_zoom = int(sys.argv[5])
input_max_zoom = int(sys.argv[6])

download_tile(input_left, input_bottom, input_right, input_top, input_min_zoom, input_max_zoom)