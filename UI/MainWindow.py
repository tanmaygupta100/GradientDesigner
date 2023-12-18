# MainWindow.py inside the "UI" folder
# Meant to be the core user-interface for inserting images and saving the "User Images" folder for further analysis.

# Directory path to root:
import sys
sys.path.append("/Users/tanmaygupta/Desktop/Image Art Processor")

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np
from ImageProcessing.ColorExtractor import extractDominantColors


# Function to read color values from the text file
def read_color_values():
    with open('color_values.txt', 'r') as file:
        lines = file.readlines()

    # Assign colors to variables
    color1 = list(map(int, lines[0].strip().split(',')))
    color2 = list(map(int, lines[1].strip().split(',')))
    color3 = list(map(int, lines[2].strip().split(',')))
    color4 = list(map(int, lines[3].strip().split(',')))
    color5 = list(map(int, lines[4].strip().split(',')))

    return color1, color2, color3, color4, color5

# Function to handle file selection:
def add_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        print(f"Selected file: {file_path}")

        # Open the image using PIL:
        pil_image = Image.open(file_path)

        # Convert the PIL image to NumPy array:
        image_array = np.array(pil_image)

        # Extract dominant colors using ColorExtractor.py:
        dominant_colors = extractDominantColors(image_array, num_colors=5)

        # Write the dominant colors to a text file
        with open('color_values.txt', 'w') as file:
            for color in dominant_colors:
                file.write(','.join(map(str, color)) + '\n')

        # Call PerlinNoiseGenerator to generate the image
        generate_perlin_image()

# Function to call PerlinNoiseGenerator and generate the image
def generate_perlin_image():
    # Import PerlinNoiseGenerator
    from ImageProcessing.PerlinNoiseGenerator import generate_perlin_image

    # Call the function to generate the image
    generate_perlin_image()

# Create a canvas object:
canvas = tk.Canvas(width=500, height=500, bg="SteelBlue3")

# Add a text in Canvas:
canvas.create_text(49, 25, text="Make art", fill="black", font=('Helvetica 17 bold'))
canvas.create_text(47, 40, text="Make ar", fill="black", font=('Helvetica 17 bold')) #-2
canvas.create_text(43, 55, text="Make a", fill="black", font=('Helvetica 17 bold')) #-4
canvas.create_text(36, 70, text="Make", fill="black", font=('Helvetica 17 bold')) #-7
canvas.create_text(32, 85, text="Mak", fill="black", font=('Helvetica 17 bold')) #-4
canvas.create_text(27, 100, text="Ma", fill="black", font=('Helvetica 17 bold')) #-5
canvas.create_text(22, 115, text="M", fill="black", font=('Helvetica 17 bold')) #-5

canvas.create_text(250, 200, text='"GRADIATOR"', fill="black", font=('Helvetica 40 bold'))

# Loading an image:
image = tk.PhotoImage(
    file="/Users/tanmaygupta/Desktop/Image Art Processor/vaporwaveFlower.png")
# Resize the image (subsample by a factor of 4 in both dimensions):
smaller_image = image.subsample(4, 4)
# Display the resized image:
canvas.create_image(375, 375, anchor=tk.NW, image=smaller_image)

# Add a button to add a file:
add_file_button = tk.Button(
    canvas, text="Transform your image", command=add_file, fg="black", highlightbackground="SteelBlue2", height=2, width=14)
button_window = canvas.create_window(170, 400, anchor=tk.NW, window=add_file_button)

canvas.pack()

# Run the program's main loop:
tk.mainloop()


'''
SAMPLE OUTPUT:
________________
Dominant Colors: 
[[171  86 227]
 [  0   0   0]
 [ 42 161 246]
 [ 27   6 129]
 [211 196 207]]
________________
'''
