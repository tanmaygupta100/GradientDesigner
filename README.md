# GradientDesigner
New project in progress! Transform your pictures into gradient artworks! Welcome to the "Gradiator"...

This project uses image processing and graphics programming techniques with algorithmically-designed Perlin Noise to create gradient artworks. Allows users to upload images, then extracts dominant colors, generates gradient artwork, and applies a generated heat-map layout for fantastic artworks.

Project Phases:
- Phase 1: Complete the UI design and logic.
- Phase 2: Working on the image processing and color extractions.
- Phase 3: Designing the Perlin Noise Algorithm.
- Phase 4: Rendering artworks and outputting.
- Phase 5: Final design work on UI and outputs.


Gradiator Program layout:
- UI
  - MainWindow.py  -  (Manages the main application window, user interactions, and file selection)
- ImageProcessing
  - perlin_noise_generator.py  -  (Generates Perlin/Simplex noise patterns to serve as the base for the heat map designs)
- Rendering
  - gradient_blending.py  -  (Handles the gradienting, blending, or blurring of the Perlin noise pattern, creating the final artwork)
- User Images  -  (Folder to store user-uploaded imeages for processing)
- main.py  -  (Entry point of program, organizing collaboration between the different modules, running the main event loop)

<img width="25%" src="https://i.imgur.com/529kcW3.png" align="left" />