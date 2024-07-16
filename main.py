import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50 # radius of planet
OBJECT_SIZE = 5 # radius of ship
VEL_SCALE = 100 # velociity scale


background = "Orbital-Mechanics-Simulator/slingshot tutorial/background.jpg"
planet = "Orbital-Mechanics-Simulator/slingshot tutorial/jupiter.png"

BG = pygame.transform.scale(pygame.image.load(background), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load(planet), (PLANET_SIZE*2, PLANET_SIZE*2))

WHITE  = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
    
    def draw(self):
        pygame.draw.circle(win, )

def main():
    # Want game to running 
    running = True
    # Want game to running at same clock speeds for all types of hardware
    clock = pygame.time.Clock()
    
    objects = []
    # initial position of ship set to None aka doesn't exist (for now)
    temp_obj_pos = None
    # Want game to be running forever until user quits
    while running:
        # Have clock tick at the set FPS
        clock.tick(FPS)
        
        mouse_pos = pygame.mouse.get_pos() # get users mouse position
        for event in pygame.event.get():
            # Change running to false to stop forever loop
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks mouse button temp position is the mouses position
                temp_obj_pos = mouse_pos
            
        # Draw background        
        win.blit(BG, (0,0))
        
        if temp_obj_pos: # if temp position exists, draw a circle aka the ship
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJECT_SIZE)
            
        
        # Update pygames display
        pygame.display.update()
    # Quit pygame    
    pygame.quit()




if __name__ == "__main__":
    main()