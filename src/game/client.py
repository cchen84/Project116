import pygame
from src.game.network import Network

display_width = 642
display_height = 600
width = 500
height = 500


BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
COBALT = (61, 89, 171)

background = pygame.image.load("bg.jpg")

win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Shootaz")

clientNumber = 0


class attack():


    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 20 * direction
        self.radius = radius
        self.direction = direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Player():

    def __init__(self, color):
        self.x = 10
        self.y = 10
        self.width = 20
        self.height = 20
        self.color = color
        self.vel = 3
        self.left = False
        self.right = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        pygame.display.update()


    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    str = str.split(",")
    return int(str[0]),int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    win.blit(background, (0,0))
    player.draw(win)
    player2.draw(win)

    for bullet in bullets:
        bullet.draw(win)


    pygame.display.update()


bullets = []

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(RED)
    p2 = Player(COBALT)

    clock = pygame.time.Clock()

    while run:


        clock.tick(100)
        p2pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        for bullet in bullets:
            if bullet.x < display_width and bullet.x > 0:
                bullet.x += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet)) #bullet gone from screen when hits boundary

        keys = pygame.key.get_pressed()



        if keys[pygame.K_LEFT]:
            p.x -= p.vel

        if keys[pygame.K_RIGHT]:
            p.x += p.vel

        if keys[pygame.K_UP]:
            p.y -= p.vel

        if keys[pygame.K_DOWN]:
            p.y += p.vel
        if p.x < 0:
            p.x = 0

        if keys[pygame.K_SPACE]:
            if p.left:
                direction = -1
            else:
                direction = 1

            if len(bullets) < 1:
                bullets.append(
                    attack(round(p.x + p.width // 2), round(p.y + p.height // 2), 3, WHITE, direction))

        if p.x > display_width - p.width:
            p.x = display_width - p.width

        if p.y < 0:
            p.y = 0

        if p.y > display_height - p.height:
            p.y = display_height - p.height


        redrawWindow(win, p, p2)

main()