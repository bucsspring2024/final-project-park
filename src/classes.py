
import pygame
import string
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize
import random

HEIGHT = 500
WIDTH = 800

CHAR = ['a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z','A',
'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W','X','Y','Z','.',',',':',';','!', ' ']

class sentence_generator:
        '''
        descrip: this class reads text from a text file, tokenizes the whole thing into sentences
        using nltk, chooses sentences at random of a certain length and modifies their length,
        punctuation, and capitlization. (ideally).
        attributes:
        punc = given True or False representing whether or not the finished sentence will have punctuation
        cap = True or False for captilizaiton. 
        methods:
        generate: the file reading, tokenizing, and modification happens in this method. 
        '''
        def __init__(self, punc,cap):
            self.punc = punc
            self.cap = cap
        def generate(self):
            with open('assets/maninthehighcastle.txt') as file:
                rawtext = file.read()
            sentencelist = sent_tokenize(rawtext)
            sortedlist = []
            for i in sentencelist:
                if len(i) > 60:
                    sortedlist.append(i)

            sentence = random.choice(sortedlist)
            if self.punc == False:
                remove_punct = str.maketrans("", "", string.punctuation)
                sentence = sentence.translate(remove_punct)
                sentence = sentence.translate(remove_punct)
                dashremove = sentence.split("â€”")
                sentence = " ".join(dashremove)
            
            if self.cap == False:
                sentence = sentence.lower()
            else:
                sentence = sentence.capitalize()

            wordlist = word_tokenize(sentence)
            sent1 = " ".join(wordlist[:10])
            # sent2 =" ".join(wordlist[11:20])
            # sent3 = " ".join(wordlist[21:31])

            return sent1


class buttons:
    '''
    description: this class draws buttons on the screen and is able to return whether or not theyre
    in the "up" or "down" state. 
    
    attributes:
    x = x coordinate for top left of button
    y = y coordinate for top left of button
    type = there are two types used in this program, this value corresponds to the area of the button
    font = the font used on the button, only one is used
    text = the text that will be blitted upon the button
    surface = the surface the buttons will be blit onto, the screen. 
    
    methods:
    draw: draws the buttons, changes color if hovered or click
    btnclick: returns whether the button is in the up or down state
    cstat: returns whether the button has been clicked since last draw()
    erase: erases from screen 


    '''
    def __init__(self, x, y, type, font, text, surface): #take state parameter out of button calls
        self.x = x
        self.y = y
        self.text = font.render(text, True, (0,0,0))
        self.state = "up"
        self.surface = surface
        if type == "rect_1":
            self.type = (100,50)
        elif type == "rect_2":
            self.type = (400,60) 
        self.clicked = False

    def draw(self):
        xcenter_var = (self.type[0]-self.text.get_rect()[2])/2
        ycenter_var = (self.type[1]-self.text.get_rect()[3])/2
        self.change0 = self.state
        self.rec = pygame.draw.rect(self.surface, "red", (self.x,self.y, self.type[0], self.type[1]))
        if self.rec.collidepoint(pygame.mouse.get_pos()):
            buttons = pygame.mouse.get_pressed()
            if buttons[0] and self.state == "up":
                
                self.rec = pygame.draw.rect(self.surface, "black", (self.x,self.y, self.type[0], self.type[1]))
                self.state = "down"
                return True
            else:
                self.rec = pygame.draw.rect(self.surface, "darkred", (self.x,self.y, self.type[0], self.type[1]))
                self.state = "up"
        else:
            self.rec=pygame.draw.rect(self.surface, "red", (self.x,self.y, self.type[0], self.type[1]))
            self.state = "up"
        pygame.draw.rect(self.surface, "black", (self.x,self.y, self.type[0], self.type[1]),1)
        self.surface.blit(self.text, (self.x+xcenter_var, self.y+ycenter_var))
        self.change1 = self.state
        return self.state
    def cstat(self):
        if self.change0 != self.state:
            
            return "clicked"
            
        else:
            return "not"

    def btnclick(self):
        return self.state
    def erase(self):
        pygame.draw.rect(self.surface, "black", (self.x,self.y, self.type[0], self.type[1]))

class testScreen:
    '''
    description: this is the gamestate on which the main game takes place. this state 
    draws a screen with buttons, generates sentences, and contains the event loop for typing on the screen.
     
    arguments:
    screen: the screen
    state: the gamestate

    methods:run
    draws the screen, buttons, generates sentences, blits them on screen, manages events for 
    typing 
    '''
    def __init__(self, screen, state):
        self.state = state
        self.screen = screen
        self.pause = True
        self.running = True
        self.font = pygame.font.SysFont('mspgothic', 16)
 

    def run(self):

        #drawing the screen 
        self.screen.fill('black')
        
        pygame.draw.rect(self.screen,"darkblue",(650, 0, 150,HEIGHT) )
        pygame.draw.rect(self.screen,"grey",(650, 0, 150,HEIGHT),2)
        pygame.draw.rect(self.screen,"darkblue",(0, 400, 650,100) )
        pygame.draw.rect(self.screen,"grey",(0, 400, 650,100), 2)
    
        #creating the buttons
        self.pausebtn = buttons(675, 100,"rect_1", self.font, "PAUSE MENU", self.screen)
        self.puncbtn = buttons(675, 170,"rect_1", self.font, "PUNCTUATION", self.screen)
        self.capbtn = buttons(675, 250,"rect_1", self.font, "CAPITALS", self.screen)
        self.length = buttons(675, 330,"rect_1", self.font, "LENGTH", self.screen)
        self.savebtn = buttons(675, 400,"rect_1", self.font, "SAVE SCORE", self.screen)
        self.startbtn = buttons(300,200, "rect_1",self.font, "start", self.screen)
        self.lisb = [self.startbtn, self.pausebtn, self.puncbtn, self.capbtn, self.length,self.savebtn ]
        
        #function to update all
        def draw_all():
            '''description: this funciton updates the buttons within the above list
            it uses the draw method from the buttons class. 
            '''
            for i in self.lisb:
                i.draw()

        #function to update what the user has typed  
        def typedblit(self, typed):
            '''description: this draws what the user has typed on the blue lower part of the screen 
            args:
            typed: a string containing what the user has typed, updated for every keydown event.
            '''
            pygame.draw.rect(self.screen,"darkblue",(0, 400, 650,100) )
            pygame.draw.rect(self.screen,"grey",(0, 400, 650,100), 2)
            self.screen.blit(self.font.render(typed, True, "green"), (200-(len(typed)),440))
        
        #function to blit the random sentence along with what the user has correctly typed
        def lineblit(self, newline, typed):
            '''description: this blits the generated line on the screen, and controls what color
            it is by comparing it to what the user has typed. 
            args:
            newline, the line generated generate sentnces class 
            typed: what the user has typed

            '''
            xvar = 54
            yvar = 180 
            len_typed = len(typed)

            text = self.font.render(newline, True, "white" )
            self.screen.blit(text, (xvar, yvar )) 
            
            
            text = self.font.render(newline[:len_typed], True, "red" )
            self.screen.blit(text, (xvar, yvar ))
            len_typed = len(typed)

            if typed == newline[:len_typed]:
                var = newline[:len_typed]
                text = self.font.render(var,True, "green" )
                self.screen.blit(text, (xvar, yvar))
                return var
            
            


            






        draw_all()

        pygame.display.update()
        
        #variables 
        pausecon = False
        quit = False
        incomp = False
        queue = True
        starttoggle = False
        gameplaytoggle = False
        punc = True
        cap = False
        typed = ''
        lastclick = pygame.time.get_ticks()
 
        

        while self.running:

            if queue:

                    newline = sentence_generator(punc, cap)
                    newline = newline.generate()
                    queue = False
            
            if starttoggle:
                
                incomp = True
                if len(self.lisb) == 6:
                    self.lisb.remove(self.startbtn)
                self.startbtn.erase()  # Clear the start button from the screen
                lineblit(self, newline, typed)
              

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True
                    self.running = False
                if incomp and event.type == pygame.KEYDOWN: 

                    pygame.draw.rect(self.screen, "black",(300,100,180,40))
                    starttoggle = False
                    lineblit(self, newline, typed)

                    
                    if event.unicode in CHAR:
                        #should start the timer here 
                        typed += event.unicode
    
                    elif event.key == pygame.K_BACKSPACE and len(typed) > 0:
                        len_typed = len(typed)
                        if typed != newline[:len_typed]:
                            typed = typed[:-1]

                    elif typed == newline:
                        typed = ''
                        incomp = False
                        queue = True
                    lineblit(self, newline, typed)
                    
                    typedblit(self,typed)
                    pygame.display.update()
                

            
            if self.pausebtn.btnclick() == "down":
                pausecon = True
                break
    
            if self.startbtn.btnclick() == "down":
                starttoggle = True

            time = pygame.time.get_ticks()
            if self.capbtn.btnclick() == 'down' and time - lastclick >= 200:
                lastclick = time
                if cap:
                    cap = False
                else:
                    cap = True
            
            if self.puncbtn.btnclick() == 'down' and time - lastclick >= 200:
                lastclick = time
                if punc:
                    punc = False
                else:
                    punc = True

           
            
            draw_all()
            pygame.display.update()
        
        #while loop break conditions:
        if pausecon:
            self.state.change('pauseS')
        if quit:
            run = False()



class startMenu:
    ''' description: this is a gamestate class which draws a screen and buttons and can be used 
    to get to the testscreen and exit the game
    
    args: 
    screen: the screen
    state: the gamestate
    
    methods:
    run: this draws the screen with buttons that quit the game or navigate to the test screen 
    '''
    def __init__(self, screen, state):
        self.state = state
        self.screen = screen
        
    def run(self):
        self.screen.fill('grey')
        self.font = pygame.font.SysFont('mspgothic', 16)
        startbtn = buttons(200, 140,"rect_2", self.font, "START", self.screen)
        startbtn.draw()
        statsbtn = buttons(200, 220,"rect_2", self.font, "STATS", self.screen)
        statsbtn.draw()
        quitbtn = buttons(200, 300,"rect_2", self.font, "EXIT", self.screen)
        quitbtn.draw()

        if startbtn.btnclick() == "down":
            self.state.change('testScreen')
        if quitbtn.btnclick() == "down":
            run = False()

class pauseS:
    '''description: this is the gamestate that draws a screen which has buttons. can restart the game
    from here or navigate to the main menu.
    args: 
    screen = the screen
    state = current gamestate
    
    methods: 
    run: draws screen, button, switces states'''
    def __init__(self, screen, state):
        self.screen = screen   
        self.state = state
    def run(self):
        self.screen.fill('grey')
        self.font = pygame.font.SysFont('mspgothic', 16)
        resumebtn = buttons(200, 140,"rect_2", self.font, "RESTART",  self.screen)
        resumebtn.draw()

        menubtn = buttons(200, 220,"rect_2", self.font, "MAIN MENU",  self.screen)
        menubtn.draw()

        if resumebtn.btnclick() == "down":

            self.state.change('testScreen')

        if menubtn.btnclick() == "down":

            self.state.change('startMenu')


class gamestate:
    '''description: the gamestate manager. it can return the current state or change the current state
    args:
    state: the current statae
    methods:
    check: returns current state
    change: changes the current state'''
    def __init__(self, state):
        self.state = state
    def check(self):
        return self.state
    def change(self, new_state):
        self.state = new_state