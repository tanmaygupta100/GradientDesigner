# ColorExtractor.py
    # Holds the extractDominantColors function, to be called by MainWindow.py

import numpy as np
from sklearn.cluster import KMeans

def extractDominantColors(image, num_colors = 5):
    # Reshape the image to be a list of pixels:
    # pixels = image.reshape((-1,3)) # finds all varrying colors rather than dominant.
    pixels = image.reshape((-1, image.shape[-1])) # testing for a different image array.
        # The image is resized because the kmeans clustering algorithm is computationally expensive.
        # Reducing the number of pixels makes the clustering process faster.
        # -1 is a placeholder for NumPy to automatically determine the size based on total pixels.
        # 3 is for each row in the reshaped array containing 3 elements (RGB).

    # Use KMeans Clustering to find the dominant colors:
    kmeans = KMeans(n_clusters=num_colors, n_init=10)
        # n_init was set to 10 so the kmeans algorithm runs with different starting points.
        # done to find a more reliable set of clusters.
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers (dominant colors):
    dominant_colors = kmeans.cluster_centers_[:, :3] # [:, :3] added for 3 columns in output.

    # Convert the colors to integer values:
    dominant_colors = dominant_colors.round().astype(int)

    return dominant_colors
