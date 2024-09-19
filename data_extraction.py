import cv2 as cv
import numpy as np
import os
import pandas as pd

# Global list to store HSV data
hsv_data = [] # dataset 
# Main function containing the backbone of the program
def main():
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    #image_path = r"C:\Users\Daniel K\OneDrive\Desktop\DAKI\1. Semester\daki_p0\KDD\57.jpg"
    image_path= r"/Users/daniel_kristensen/DAKI/opgaver/DAKI-opg/daki_p0/KDD/55.jpg"
    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image) 
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile, x, y))
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
hsv_data = []
def get_terrain(tile,x ,y):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)
    hue, saturation, value = np.median(hsv_tile, axis=(0,1)) # Consider using median instead of mean
    print(f"H: {hue}, S: {saturation}, V: {value}")
    hsv_data.append({"Coordinate": f"{x},{y}", "Hue": hue, "Saturation": saturation, "Value": value}) #Adds data to the dataset
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



 
    # Create DataFrame from hsv_data after main() has executed
    df = pd.DataFrame(hsv_data)
    
    # Save to Excel
    df.to_excel('image_hsv_data.xlsx', index=False)
    print("Excel file created successfully.")