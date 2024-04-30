# these will be imported into the controller
import pygame
class text:

    def __init__(self, position, state, cap, punc):
        '''
        Initializes the text which will appear on the screen to be typed
        args:
        - position : will indicated where in the string each letter will appear
        - state : whether or not the letter has been typed by the user yet
        - cap : Whether there will be capitilization
        - punc : whether there will be punctuation
        '''

class buttons:
    def __init__(self, x, y, type, font, text, state, surface):
        self.x = x
        self.y = y
        self.text = font.render(text, True, (0,0,0))
        self.state = state
        self.surface = surface
        if type == "rect_1":
            self.type = (100,50)
        else:
           self.type = (100,50) 

    def draw(self):
        xcenter_var = (self.type[0]-self.text.get_rect()[2])/2
        ycenter_var = (self.type[1]-self.text.get_rect()[3])/2

        rec = pygame.draw.rect(self.surface, "red", (self.x,self.y, self.type[0], self.type[1]))
        if rec.collidepoint(pygame.mouse.get_pos()):
            buttons = pygame.mouse.get_pressed()
            if buttons[0]:
                pygame.draw.rect(self.surface, "darkred", (self.x,self.y, self.type[0], self.type[1]))
                self.state = "clicked"
            else:
                pygame.draw.rect(self.surface, "darkred", (self.x,self.y, self.type[0], self.type[1]))
        pygame.draw.rect(self.surface, "black", (self.x,self.y, self.type[0], self.type[1]),1)
        self.surface.blit(self.text, (self.x+xcenter_var, self.y+ycenter_var))

