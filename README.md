# GradientDesigner
Transform your pictures into abstract artworks! Welcome to the "Gradiator"...

This project uses image processing and graphics programming techniques with a Perlin Noise algorithm to create heat-map designs and gradient artwork. Allows users to upload images, from which the dominant colors are extracted and used to create art.


Home screen and test-input image:

<div style="display: flex; justify-content: space-between;">
    <img width="30%" src="https://i.imgur.com/529kcW3.png" />
    <img width="30%" src="https://i.imgur.com/uwvF9y6.png" />
</div>

<br/>

Outputs (Perlin heat-map and gradient art):

<div style="display: flex; justify-content: space-between;">
    <img width="30%" src="https://i.imgur.com/Y755ckp.png" />
    <img width="30%" src="https://i.imgur.com/n6twBLT.png" />
</div>

<br/>


Project Phases:
- Phase 1: Complete the UI design and logic.
- Phase 2: Work on the color extractions into text file.
- Phase 3: Design the Perlin Noise Algorithm.
- Phase 4: Unite all the programs to work in tandem.
- Phase 5: Final design work in testing rendered artworks to output.


Gradiator Program layout:
- UI
  - MainWindow.py  -  (Manages the main application window, user interactions, and file selection)
- ImageProcessing
  - ColorExtractor.py  -  (Extracts the 5 most dominant colors from an image and saves the RGB values to a text file)
  - ColorReader.py  -  (Converts human-friendly RGB values (from ColorExtractor.py) to computer-friendly RGB values (for PerlinNosieGenerator.py))
  - PerlinNoiseGenerator.py  -  (Generates Perlin noise patterns for the heat map design, as well as creates a gradient design, based on the RGB text)
- color_values.txt  -  (Initially written by ColorExtractor.py, then rewritten by ColorReader.py)

<br/>

Tested Progress of testing rendering techniques:

Phases 5.1, 5.2, & 5.3 of testing: Refining the brush strokes, color selections, and design complexity

<div style="display: flex; justify-content: space-between;">
    <img width="30%" src="https://i.imgur.com/Pb6RC0C.png" />
    <img width="30%" src="https://i.imgur.com/SC9lOGK.png" />
    <img width="30%" src="https://i.imgur.com/Wl711FW.png" />
</div>

<br/>

Phase 5.4: Finalizing the code and increasing output time-efficiency and costliness

<div style="display: flex; justify-content: space-between;">
    <img width="30%" src="https://i.imgur.com/3nzDqV6.png" />
    <img width="30%" src="https://i.imgur.com/adM7zyQ.png" />
</div>

<br/>

Libraries used:
- NumPy - For numerical operations and array handling.
- OpenCV - For image processing (computer vision tasks).
- scikit-learn - For machine learning algorithms (such as KMeans clustering).
- Pillow (PIL) - For Image processing (basic image handling).
