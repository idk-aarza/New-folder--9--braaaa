import pygame
BLUE= pygame.Color("blue")
LIGHTBLUE= pygame.Color("lightblue")
DARKBLUE= pygame.Color("darkblue")
YELLOW=pygame.Color("yellow")
MAGENTA=pygame.Color("magenta")
ORANGE=pygame.Color("orange")
WHITE=pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Sprite, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
sp1=Sprite(WHITE, 20, 30)
screen=pygame.display.set_mode([500, 400])
pygame.display.set_caption("SPRITESSS")
bg_color=BLUE
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill(bg_color)
    screen.blit(sp1.image, sp1.rect)
    pygame.display.flip()