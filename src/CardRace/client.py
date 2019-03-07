import pygame
from tkinter import *
from tkinter import messagebox

width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Card Race")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

# Function to move character left, right, up, down (boundaries included)
    def move(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_LEFT]

        if left:
            self.x -= self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

#Function to set boundaries
    def boundaries(self):
        if self.x < 0:
            self.x = 0

        if self.x > width - self.width:
            self.x = width - self.width

        if self.y < 0:
            self.y = 0

        if self.y > height - self.height:
            self.y = height - self.height

# Draws Winner message to screen
        def drawWinner():
            pygame.font.init()
            font = pygame.font.SysFont("arial", 30, True)
            textSurface = font.render("Winner", 1, (0, 0, 0))
            win.blit(textSurface, (375, 375))
            pygame.display.update()


#Checks for Winner
        if self.x == 0:
            drawWinner()





        self.rect = (self.x, self.y, self.width, self.height)
        pygame.display.update()


def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()
 

def main():
    run = True
    p = Player(50,50,100,100,(0,255,0))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)

main()

