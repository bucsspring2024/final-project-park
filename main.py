import pygame

from src.controller import controller

def main():
    pygame.init()
    x = controller()
    x.mainloop()
if __name__ == '__main__':
    main()
