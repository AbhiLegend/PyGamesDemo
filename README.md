# PyGamesDemo

RDKit Molecule Game
This is a simple game written in Python using the RDKit library and Pygame. The goal of the game is to click on as many molecules as possible within a given time limit.

Requirements
RDKit (version 2021.03.3 or later)
Pygame (version 2.0.1 or later)
Usage
To play the game, simply run the script rd44e.py using Python 3. The game window will appear, and you can use the arrow keys to rotate the camera and the up/down arrow keys to zoom in/out. Click on the molecules to increase your score. The game will automatically end after 90 seconds.

The molecules used in the game are randomly selected from a pre-defined list. You can modify this list by editing the mol_list variable in the script.

Credits
This game was created by ChatGPT using the RDKit library and Pygame.

License
This game is released under the MIT License. See the LICENSE file for more information.


What is the code doing

The code is a Python program that uses the RDKit library to generate and display random molecular structures in a Pygame window. The user can interact with the molecules by adjusting the camera position and zoom level, and can click on them to increase their score. The program starts by importing the necessary libraries, including RDKit, Pygame, and the io module.

The Pygame window is initialized and the dimensions of the window are set to 800x600. A clock is set up to keep track of the game loop timing, and a font is initialized for drawing text on the screen. The camera position, zoom, and rotation are set to their initial values, and the game variables "score" and "time_left" are initialized to 0 and 90, respectively.

The program generates a random molecule from a list of SMILES strings using the RDKit function Chem.MolFromSmiles(), and then converts it to a Pygame image using the RDKit function Draw.MolToImage(). The image is saved to an in-memory bytes buffer using the io module, and then loaded into a Pygame surface using pygame.image.load(). The image is then drawn onto the Pygame screen using Pygame's blit() function.

The program enters a game loop that runs until the user quits the program. The game loop handles events such as mouse and keyboard input, and updates the screen with the current score, time remaining, and the name of the current molecule. The camera position, zoom level, and rotation are adjusted based on keyboard input, and the mouse position is adjusted for the camera before handling mouse input. If the user clicks on the current molecule, their score is incremented and a new random molecule is generated.

Overall, the program generates random molecules and displays them in a Pygame window, allowing the user to interact with them and score points by clicking on them.











