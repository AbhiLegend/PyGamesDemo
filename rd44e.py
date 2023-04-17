from rdkit import Chem
from rdkit.Chem import Draw
import pygame
import random
import time
import sys
from io import BytesIO

# Initialize pygame
pygame.init()

# Set window dimensions
width, height = 800, 600

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 48)

# Set up the screen
screen = pygame.display.set_mode((width, height))

# Set up the camera
camera_position = [width//2, height//2]
camera_zoom = 1.0
camera_rotation = 0.0

# Set up the game variables
score = 0
time_left = 90

# Set up the molecule
mol = Chem.MolFromSmiles(random.choice(["C1CCCCC1", "CC(C)C1CCC1", "CC(C)C1CCCC1", "CC1=CC=CC=C1", "CCCCCCCCCCCC", "CC(C)CC(C)(C)C", "C1=CC=NC=C1", "C1CCC(CC1)C(=O)O", "C(CN)O", "CC(C)COC(=O)C", "C1=CC=C(C=C1)Cl", "CCN(CC)CC"]))

img = Draw.MolToImage(mol, size=(400, 300))
img_bytes = BytesIO()
img.save(img_bytes, format="PNG")
img_bytes.seek(0)
img_surface = pygame.image.load(img_bytes)

# Set up the game loop
while True:

    # Clear the screen
    screen.fill((255, 255, 255))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                camera_rotation += 5.0
            elif event.key == pygame.K_RIGHT:
                camera_rotation -= 5.0
            elif event.key == pygame.K_UP:
                camera_zoom += 0.1
            elif event.key == pygame.K_DOWN:
                camera_zoom -= 0.1
            elif event.key == pygame.K_SPACE:
                #mol = Chem.MolFromSmiles(random.choice(["C1CCCCC1", "CC(C)C1CCC1", "CC(C)C1CCCC1"]))
                mol = Chem.MolFromSmiles(random.choice(["C1CCCCC1"]))
                img = Draw.MolToImage(mol, size=(400, 300))
                img_bytes = BytesIO()
                img.save(img_bytes, format="PNG")
                img_bytes.seek(0)
                img_surface = pygame.image.load(img_bytes)

    # Get the mouse position and adjust for camera
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x -= camera_position[0]
    mouse_y -= camera_position[1]
    mouse_x /= camera_zoom
    mouse_y /= camera_zoom
    mouse_x, mouse_y = pygame.math.Vector2(mouse_x, mouse_y).rotate(-camera_rotation)
    mouse_x += camera_position[0]
    mouse_y += camera_position[1]

    # Handle mouse events
    if pygame.mouse.get_pressed()[0]:
        camera_position[0] -= pygame.mouse.get_rel()[0]
        camera_position[1] -= pygame.mouse.get_rel()[1]

    # Draw the molecule
    img_rotated = pygame.transform.rotate(img_surface, camera_rotation)
    img_scaled = pygame.transform.scale(img_rotated, (int(img_rotated.get_width() * camera_zoom), int(img_rotated.get_height() * camera_zoom)))
    img_rect = img_scaled.get_rect()
    img_rect.center = camera_position
    screen.blit(img_scaled, img_rect)

    # Check if molecule is clicked
    if pygame.mouse.get_pressed()[0]:
       if img_rect.collidepoint(pygame.mouse.get_pos()):
        score += 1
        mol = Chem.MolFromSmiles(random.choice(["C1CCCCC1", "CC(C)C1CCC1", "CC(C)C1CCCC1", "CC1=CC=CC=C1", "CCCCCCCCCCCC", "CC(C)CC(C)(C)C", "C1=CC=NC=C1", "C1CCC(CC1)C(=O)O", "C(CN)O", "CC(C)COC(=O)C", "C1=CC=C(C=C1)Cl", "CCN(CC)CC"]))
        img = Draw.MolToImage(mol, size=(400, 300))
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        img_surface = pygame.image.load(img_bytes)

   


# Draw the score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw the time left
    time_left_text = font.render("Time: " + str(int(time_left)), True, (0, 0, 0))
    mol_name_text = font.render("Molecule: " + Chem.MolToSmiles(mol), True, (0, 0, 0))
    screen.blit(mol_name_text, (10, 50))

    screen.blit(time_left_text, (width - 10 - time_left_text.get_width(), 10))

    # Update the camera
    camera_position[0] += (mouse_x - camera_position[0]) * 0.1
    camera_position[1] += (mouse_y - camera_position[1]) * 0.1


    # Update the timer
    dt = clock.tick(60) / 1000.0
    time_left -= dt
    if time_left <= 0:
      time_left = 0
      game_over_text = font.render("GAME OVER", True, (255, 0, 0))
      screen.blit(game_over_text, (width//2 - 100, height//2))
      pygame.display.update()
      time.sleep(2)
      pygame.quit()
      sys.exit()
    # Update the display
    pygame.display.update()

