import pygame

# button class
class Button():
    def __init__(self, player_index, stone_pos, name, x, y, image, image_hover, width_scale, height_scale):
        self.player_index = player_index
        self.stone_pos = stone_pos
        self.name = name
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*width_scale), int(height*height_scale)))
        self.image_hover = pygame.transform.scale(image_hover, (int(width*width_scale), int(height*height_scale)))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.clicked = False
        self.hovered = False
    
    def draw(self, surface):
        action = False
        self.hovered = False
        
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.hovered = True
            # check if clicked
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        

        # if button is not clicked - goes back to false
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        if self.hovered:
            surface.blit(self.image_hover, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action