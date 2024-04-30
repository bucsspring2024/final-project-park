import pygame
from classes import buttons
width = 800 
height = 500
timer = pygame.time.Clock()
paused = False


class controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.backround = pygame.Surface((width,height))
        self.timer = pygame.time.Clock()
        self.fps = 60
        #pygame.draw.rect can provide a rectangle on which letters can go semi transparently, draw lines, screen.blit(for text)
        pygame.display.set_caption('Typing Test')
        self.screen.fill('black')
        self.timer.tick(self.fps)

        #draw screen details, call button functions for buttons 
   




    def mainloop(self):
        def drawscreen(self):
            timer.tick(60)
            pygame.init()
            pygame.draw.rect(self.screen,"darkblue",(650, 0, 150,height) )
            pygame.draw.rect(self.screen,"grey",(650, 0, 150,height),2)
            pygame.draw.rect(self.screen,"darkblue",(0, 400, width,100) )
            pygame.draw.rect(self.screen,"grey",(0, 400, width,100),2 )
            font = pygame.font.SysFont('mspgothic', 16)
            #__init__x, y, type, font, text, state, surface
            button1 = buttons(675, 20,"rect_1", font, "test button", "pressed", self.screen)
            button1.draw()

        run = True
        while run:
            
            status = drawscreen(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if not paused:
                        

            pygame.display.flip()
        pygame.quit()




        
