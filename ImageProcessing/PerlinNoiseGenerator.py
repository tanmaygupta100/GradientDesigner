# PerlinNoiseGenerator.py

import numpy as np
from PIL import Image
import noise
import random
from scipy.ndimage import gaussian_filter

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

# Function to generate the Perlin noise-based image
def generate_perlin_image():
    # Read color values from the text file
    color1, color2, color3, color4, color5 = read_color_values()

    # Function to generate the Perlin noise-based world
    def generate_world(size, scale, seed):
        random.seed(seed)
        world = np.zeros(size)

        # Loop through each pixel in the world
        for i in range(size[0]):
            for j in range(size[1]):
                # Generate Perlin noise value for the current pixel
                world[i][j] = noise.pnoise2(i/scale, j/scale, octaves=8, persistence=0.6, lacunarity=2.0, repeatx=1024, repeaty=1024, base=seed)
        return world

    # Function to assign colors to different terrain based on the Perlin noise values
    def add_color(world):
        color_world = np.zeros(world.shape + (3,))

        # Loop through each pixel in the world
        for i in range(1, world.shape[0] - 1):
            for j in range(1, world.shape[1] - 1):
                # Assign color based on the Perlin noise value of the current pixel
                if world[i][j] < -0.2:
                    color_world[i][j] = color3
                elif world[i][j] < -0.1:
                    color_world[i][j] = color5
                elif world[i][j] < 0.0:
                    color_world[i][j] = color2
                elif world[i][j] < 0.125:
                    color_world[i][j] = color4
                else:
                    color_world[i][j] = color1

                # Apply brush stroke effect
                brush_intensity = 0.075  # Adjust the brush stroke intensity
                color_world[i][j] = (
                    color_world[i][j] +
                    brush_intensity * (color_world[i+1][j] + color_world[i-1][j] + color_world[i][j+1] + color_world[i][j-1] - 4 * color_world[i][j])
                )

        return color_world

    # Adjust the size of the world array
    world_size = (500, 500)
    world_scale = 150.0  # Adjust the scale for different patterns
    seed = random.randint(0, 1000)  # Use a random seed

    # Create a larger image by duplicating each pixel in the world
    world = generate_world(world_size, world_scale, seed)
    enlarged_world = np.kron(world, np.ones((1, 1))) # Adjust the factor for smaller pixels

    # Assign colors based on the Perlin noise values
    color_world = add_color(enlarged_world)


    Image.fromarray(np.uint8(color_world)).show()

    # Apply Gaussian blur to the color world
    sigma = 25.0  # Adjust the sigma parameter for different blur intensity
    blurred_color_world = gaussian_filter(color_world, sigma=(sigma, sigma, 0))

    # Convert the array to an image and display it
    Image.fromarray(np.uint8(blurred_color_world)).show()
    

# Uncomment the next line to test generating the image directly from this module
# generate_perlin_image()
