import pygame

# button class
class Button():
    def __init__(self, x, y, image, width_scale, height_scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*width_scale), int(height*height_scale)))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        
        # if button is not clicked - goes back to false
        if pygame.mouse.get_pressed()[0]== 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action