# ColorReader.py

# Directory path to root:
import sys
sys.path.append("/Users/tanmaygupta/Desktop/Image Art Processor")


# Assuming the ColorExtractor.py is in the same directory
from ImageProcessing.ColorExtractor import extractDominantColors
import numpy as np

# Call the ColorExtractor function to get the dominant colors
# You might want to replace this image_array with the actual image array
image_array = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)  # Replace this line
dominant_colors = extractDominantColors(image_array, num_colors=5)

# Write to a text file
with open('color_extractor_output.txt', 'w') as file:
    for color in dominant_colors:
        file.write(','.join(map(str, color)) + '\n')

# PerlinNoiseGenerator reads the text file
with open('color_extractor_output.txt', 'r') as file:
    lines = file.readlines()

# Assign colors to variables
color1 = list(map(int, lines[0].strip().split(',')))
color2 = list(map(int, lines[1].strip().split(',')))
color3 = list(map(int, lines[2].strip().split(',')))
color4 = list(map(int, lines[3].strip().split(',')))
color5 = list(map(int, lines[4].strip().split(',')))

# Display the assigned colors
print("Color 1:", color1)
print("Color 2:", color2)
print("Color 3:", color3)
print("Color 4:", color4)
print("Color 5:", color5)
