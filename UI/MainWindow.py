# MainWindow.py inside the "UI" folder
    # Meant to be the core user-interface for inserting images and saving the the "User Images" folder for further analysis.

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import shutil

# Function for adding empty lines:
def emptyline(root):
    empty_space = ttk.Label(root, text='')
    empty_space.pack()


# Function to handle file selection:
    # Saves it to a new folder, "User Images"
def add_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        print(f"Selected file: {file_path}")
        # Get the filename and extension:
        file_name = os.path.basename(file_path)
        # Create the "User Images" folder if it doesn't exist:
        user_images_folder = "User Images"
        os.makedirs(user_images_folder, exist_ok=True)
        # Construct the destination path in the "User Images" folder:
        destination_path = os.path.join(user_images_folder, file_name)
        # Copy the selected file to the "User Images" folder:
        shutil.copy2(file_path, destination_path)
        print(f"Image saved to: {destination_path}")
            # If an image exists in the folder with the same name, it gets replaced.


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
    file="/YourFilePathTo/vaporwaveFlower.png")
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
