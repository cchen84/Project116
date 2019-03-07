import pygame

pygame.init()

# Window dimension
display_width = 600
display_height = 700

# Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
COBALT = (61, 89, 171)



screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()



# Game set up
def game_init():


    pygame.display.set_caption("Card Race")
    screen.fill(WHITE)



# PLAYER CLASS
class Player():


    # INITIALIZE PLAYER'S COORDINATES, SIZE, COLOR
    def __init__(self, color):
        self.color = color
        self.velocity = 3
        self.x = 10
        self.y = 10
        self.left = False
        self.right = False
        self.width = 50
        self.height = 50

    # DRAW THE CHARACTER
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()


class attack():


    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 10
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)




#Drawing on screen
def drawWindow(screen, player):
    screen.fill(BLACK)
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()




# GAME LOOP
player1 = Player(COBALT)
bullets = []
def game_loop():

    run_game = True

    while run_game:

        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        for bullet in bullets:
            if bullet.x < display_width and bullet.x > 0:
                bullet.x += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet)) #bullet gone from screen when hits boundary


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player1.x -= player1.velocity

        elif keys[pygame.K_RIGHT]:
            player1.x += player1.velocity

        elif keys[pygame.K_UP]:
            player1.y -= player1.velocity

        elif keys[pygame.K_DOWN]:
            player1.y += player1.velocity

        if keys[pygame.K_SPACE]:

            if len(bullets) < 3:
                bullets.append(attack(round(player1.x + player1.width//2), round(player1.y + player1.height//2), 6 , RED))


        # SETTING BOUNDARIES
        if player1.x < 0:
            player1.x = 0

        if player1.x > display_width - player1.width:
            player1.x = display_width - player1.width

        if player1.y < 0:
            player1.y = 0

        if player1.y > display_height - player1.height:
            player1.y = display_height - player1.height



        drawWindow(screen, player1)



    pygame.display.quit()
    pygame.quit()


def main():
    game_init()
    game_loop()



if __name__ == '__main__':
    main()







