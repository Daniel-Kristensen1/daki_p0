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
    image_path = r"C:\Users\Daniel K\OneDrive\Desktop\DAKI\1. Semester\daki_p0\KDD\57.jpg"
    #image_path= r"/Users/daniel_kristensen/DAKI/opgaver/DAKI-opg/daki_p0/KDD/55.jpg"
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
    #if x ==0 and y==0:
    row4 = []
    for y, row in enumerate(hsv_tile):
        if 2 < y < 97:
            for x, hsv in enumerate(row):
                if x<3 or x>96:
                    row4.append(hsv.tolist())
        else: 
            for x, hsv in enumerate(row):
                row4.append(hsv.tolist())
        #row4.append(row.tolist())
    vertical = hsv_tile[3:-3]
        #print(vertical[0][:3])
    #for index, row in enumerate(vertical):

        #row4.append(vertical[index][:3].tolist() + vertical[index][-3:].tolist())
        
        #row4.append(vertical[0][:3].tolist())
        #row4.append(vertical[0][-3:].tolist())
    #print(f"row4: {len(row4)}")
    #row4.append(hsv_tile[0].tolist())
    print(f"row4: {len(row4)}")
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

    hue, saturation, value = np.mean(row4, axis=(0)) # Consider using median instead of mean
    #hue, saturation, value = np.mean(hsv_tile, axis=(0,1))
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