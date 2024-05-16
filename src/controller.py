import pygame
from src.classes import gamestate, testScreen, startMenu, pauseS 
width = 800 
height = 500
timer = pygame.time.Clock()
typed = 'sample text'
typecomplete = ''
begin = True
paused = False
char = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y','Z','.',',',':',';','!']




        
class controller:
    
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.backround = pygame.Surface((width,height))
        self.timer = pygame.time.Clock()
        self.fps = 60
        pygame.display.set_caption('Typing Test')
        self.screen.fill('black')
        self.timer.tick(self.fps)

        self.gamestate = gamestate('startMenu')
        self.testScreen = testScreen(self.screen, self.gamestate)
        self.startMenu = startMenu(self.screen, self.gamestate)
        self.pauseS = pauseS(self.screen, self.gamestate)

        self.states = {'testScreen':self.testScreen, 'startMenu':self.startMenu, 'pauseS':self.pauseS}
        
    def mainloop(self):




        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            L = self.states[self.gamestate.check()].run()
            if L == "quit":
                pygame.quit()
            if L: #probably wrong
                paused = True
                pass


            pygame.display.flip()
        pygame.quit()






        




        