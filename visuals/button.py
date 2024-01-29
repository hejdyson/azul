import pygame


# button class
class Line():
    def __init__(self, player_index, stone_pos, name, limit, x, y, image, image_hover, width_scale, height_scale):
        self.player_index = player_index
        self.stone_pos = stone_pos
        self.name = name
        self.limit = limit
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*width_scale), int(height*height_scale)))
        self.image_hover = pygame.transform.scale(image_hover, (int(width*width_scale), int(height*height_scale)))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.clicked = False
        self.hovered = False
        self.stones = []
    
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

        return



class Underlying():
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
        # list for stones on underlying
        self.stones = []
    
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

        return
    


class Stone():
    # placement - object where its now placed -> underlying, line or table right
    def __init__(self, value, placement, name, x, y, image, image_hover, width_scale, height_scale):
        self.value = value
        self.placement = placement
        self.name = name
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*width_scale), int(height*height_scale)))
        self.image_hover = pygame.transform.scale(image_hover, (int(width*width_scale), int(height*height_scale)))

        self.clicked = False
        self.hovered = False
    

    def draw(self, surface):
        self.rect = self.image.get_rect()
        self.rect.topright = (self.x, self.y)

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # check if clicked
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
        

        # if button is not clicked - goes back to false
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return


class BoardVisual():
    def __init__(self, round, list_of_tables, list_of_underlyings, bag_of_tiles, possible_to_click_on_stones, player_index):
        self.round = round
        self.list_of_tables = list_of_tables
        self.list_of_underlyings = list_of_underlyings
        self.bag_of_tiles = bag_of_tiles
        self.possible_to_click_on_stones = possible_to_click_on_stones
        self.player_index = player_index
        self.empty = False
        self.underlying_to_clear = None
        self.to_line = []
        self.to_the_middle = []
        self.middle_remove = []
        self.player_list = []