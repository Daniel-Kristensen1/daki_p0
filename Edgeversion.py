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
    #if x ==0 and y==0:
    edge_list = []
    for row_index, row in enumerate(hsv_tile):
        if 2 < row_index < 97:
            for col_index, hsv in enumerate(row):
                if col_index<3 or col_index>96:
                    edge_list.append(hsv.tolist())
        else: 
            for col_index, hsv in enumerate(row):
                edge_list.append(hsv.tolist())
        #row4.append(row.tolist())
    #vertical = hsv_tile[3:-3]
        #print(vertical[0][:3])
    #for index, row in enumerate(vertical):

        #row4.append(vertical[index][:3].tolist() + vertical[index][-3:].tolist())
        
        #row4.append(vertical[0][:3].tolist())
        #row4.append(vertical[0][-3:].tolist())
    #print(f"row4: {len(row4)}")
    #row4.append(hsv_tile[0].tolist())
    print(f"row4: {len(edge_list)}")
    #print(f"row4: {row4[:]}")
    #print(hsv_tile[0][0])
    #print(f"hsv: {hsv_tile[0]}")
    
        
        #del row4[3:-3]
        #row4.append(vertical[0][0:3].tolist())
        #row4[-1].append(vertical[0][-3:].tolist())
        #print(vertical[0][0:3])
        #print(vertical[0][-4:])
        #print(row4)
    '''
        horisontal = []
        for y, value in enumerate(vertical):
            #print(y)
            temp = []
            
            for x, hsv in enumerate(value):
               
               #print(f"{y}, {x}, {hsv}")
               if 3 > x:
                   #print(f"{y}, {x}, {hsv}")
                   temp.append(hsv.tolist())
            horisontal.append(temp)
            print(temp[0])
        #print(horisontal[0])
        clean_output = [hsv.tolist() for hsv in horisontal[0][:10]]
        #print(clean_output)
        #print(vertical)
        #print(hsv_tile[-4])
        #print(f"First three {hsv_tile[0:3]}") #Maybe works
        #print(f"Last three {hsv_tile[-3:]}") #Maybe works
        #print(f"test {hsv_tile[3:-4]}") #Not working
        #print(f"test {hsv_tile[0][-3:]}") #Not working
    '''

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