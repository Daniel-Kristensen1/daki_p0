import cv2 as cv
import numpy as np
import os
import pandas as pd

# Global list to store HSV data
hsv_data = [] # dataset 
# Main function containing the backbone of the program
def main(img_num):
    print(img_num)
    print("+-------------------------------+")
    print("| King Domino points calculator |")
    print("+-------------------------------+")
    #image_path = r"C:\Users\Daniel K\OneDrive\Desktop\DAKI\1. Semester\daki_p0\KDD\57.jpg"
    image_path= fr"/Users/daniel_kristensen/DAKI/opgaver/DAKI-opg/daki_p0/KDD/{img_num}.jpg"

    if not os.path.isfile(image_path):
        print("Image not found")
        return
    image = cv.imread(image_path)
    tiles = get_tiles(image) 
    #print(tiles[0])
    print(len(tiles))
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            print(f"Tile ({x}, {y}):")
            print(get_terrain(tile, x, y, img_num))
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

def get_terrain(tile,tile_x ,tile_y, image_number):
    hsv_tile = cv.cvtColor(tile, cv.COLOR_BGR2HSV)

    edge_list = []
    for row_index, row in enumerate(hsv_tile):
        if 14 < row_index < 85:
            for col_index, hsv in enumerate(row):
                if col_index<15 or col_index>84:
                    edge_list.append(hsv.tolist()) #1164 values
        else: 
            for col_index, hsv in enumerate(row):
                edge_list.append(hsv.tolist())

    print(f"edge_list: {len(edge_list)}")

    hue, saturation, value = np.median(edge_list, axis=(0)) # Consider using median instead of mean
    hue = round(hue, 5)
    saturation = round(saturation, 5)
    value = round(value, 5)
    #hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
    print(f"H: {hue}, S: {saturation}, V: {value}")
    hsv_data.append({"Image number": f"{image_number-1}","Coordinate_x": f"{tile_x}","Coordinate_y": f"{tile_y}", "Hue": hue, "Saturation": saturation, "Value": value}) #Adds data to the dataset
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
    pic= [1, 2, 3, 12, 13, 14, 23, 24, 25, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 55, 56, 57, 65, 66, 67]
    for i in pic:
        main(i)




 
    # Create DataFrame from hsv_data after main() has executed
    df = pd.DataFrame(hsv_data)
    
    # Save to Excel
    df.to_excel('image_hsv_data.xlsx', index=False)
    print("Excel file created successfully.")