# MainWindow.py inside the "UI" folder
    # Meant to be the core user-interface for inserting images and saving the the "User Images" folder for further analysis.

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

# Directory path to root:
import sys
sys.path.append("/FilePathToTheRootFolderOfProject")

# Function for adding empty lines:
def emptyline(root):
    empty_space = ttk.Label(root, text='')
    empty_space.pack()


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
        print("Dominant Colors: ")
        print(dominant_colors)


# Create a canvas object:
canvas= tk.Canvas(width= 500, height= 500, bg="SteelBlue3")

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
    file="/TheFilePathTo/vaporwaveFlower.png")
# Resize the image (subsample by a factor of 4 in both dimensions):
smaller_image = image.subsample(4, 4)
# Display the resized image:
canvas.create_image(375, 375, anchor=tk.NW, image=smaller_image)

# Add a button to add a file:
add_file_button = tk.Button(
    canvas, text="Transform your image", command=add_file, fg="black", highlightbackground="SteelBlue2", height = 2, width = 14)
button_window = canvas.create_window(170, 400, anchor=tk.NW, window=add_file_button)

canvas.pack()


# Run's the program's main loop:
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
