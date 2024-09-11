import cv2 as cv
import numpy as np
import os

# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    #image_path = r"C:\Users\Daniel K\OneDrive\Desktop\DAKI\1. Semester\daki_p0\KDD\1.jpg" 
    image_path= r"/Users/daniel_kristensen/DAKI/opgaver/DAKI-opg/daki_p0/KDD/1.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image) 
    #print(f"Tiles:{tiles}")
    print(len(tiles))
    for y, row in enumerate(tiles):
        #print(f"y, row: {y}, {row}")
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile))
            print("=====")

# Break a board into tiles
# Returns a list of ??
def get_tiles(image):
    tiles = []
    for y in range(5):
        tiles.append([])
        for x in range(5):
            tiles[-1].append(image[y*100:(y+1)*100, x*100:(x+1)*100]) 
    return tiles

# Determine the type of terrain in a tile
# Returns a string
def get_terrain(tile):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.mean(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Field"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Forest"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Lake"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Grassland"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Swamp"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Mine"
    if 0 < hue < 0 and 0 < saturation < 0 and 0 < value < 0:
        return "Home"
    return "Unknown"

if __name__ == "__main__":
    main()