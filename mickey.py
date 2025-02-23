import pygame
import random
#Initialize pygame
pygame
#Custom event IDs for color change events
SPRITE_CHANGE_EVENT=pygame.USEREVENT + 1
BACKGROUND_CHANGE_EVENT=pygame.USEREVENT + 2
#Define basic colors using pygame.Color
#Background colors
BLUE= pygame.Color("blue")
LIGHTBLUE= pygame.Color("lightblue")
DARKBLUE= pygame.Color("darkblue")
#Sprite colors
YELLOW=pygame.Color("yellow")
MAGENTA=pygame.Color("magenta")
ORANGE=pygame.Color("orange")
WHITE=pygame.Color("white")
#Spirte class representing the movie object
class Sprite(pygame.sprite.Sprite):
    #Constructor method 
     def __init__(self, color, width, height):
        #Call the parent class (Sprite) constructor
        super(Sprite, self).__init__()
        #Create the sprite"s surface with dimensions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Get the sprites rect defini g its position and size
        self.rect = self.image.get_rect()
        #set initial velocity with random direction 
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]
        #Method to update the sprite"s position
        self.rect.move_ip(self.velocity)
        #Flag to track if the sprite is moving
        boundary_hit=False
        #Check for collision with left or right boundaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit=True
        #Check for collision with top or bottom boundaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit=True
        #If the boundary has a hit, post events to change it's color
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_CHANGE_EVENT))
        #Method to change the sprite"s color
     def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
#Method to change the background color
def change_background_color():
    global bg_color 
    bg_color=(random.choice([BLUE, LIGHTBLUE, DARKBLUE]))
#Create a group to hold the sprite
all_sprites_list=pygame.sprite.Group()
#Instantiate the sprite
sp1=Sprite(WHITE, 20, 30)
#Randomly position the sprite
sp1.rect.x=random.randint(0, 480)
sp1.rect.y=random.randint(0, 380)
#Add the sprite to the group
all_sprites_list.add(sp1)
#Create the game window
screen=pygame.display.set_mode([500, 400])
#Set the window title
pygame.display.set_caption("Mickey")
#Set the background color
bg_color=BLUE
#Apply the background color
screen.fill(bg_color)
#Game loop control flag
exit=False
#Create a clock object to control the frame rate
clock=pygame.time.Clock()
#Main game loop
clock=pygame.time.Clock()
#Main game loop
while not exit:
    #Event handaling loop
    for event in pygame.event.get():
        #Check if the user has quit the game
        if event.type == pygame.QUIT:
            exit=True
        #Check if the sprite change event was triggered
        elif event.type == SPRITE_CHANGE_EVENT:
            sp1.change_color()
            #Iterate over all sprites in the group
        elif event.type==BACKGROUND_CHANGE_EVENT:
          change_background_color
                #Change the sprite"s color
        #Check if the background change event was triggered
        if event.type == BACKGROUND_CHANGE_EVENT:
            change_background_color()
    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()