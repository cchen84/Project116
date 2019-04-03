import pygame

pygame.init()

# Window dimension

display_width = 642
display_height = 600

# Colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
COBALT = (61, 89, 171)

background = pygame.image.load("bg.jpg")

screen = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

lives = 3

# Game set up
def game_init():


    pygame.display.set_caption("Shootaz")
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
        self.width = 10
        self.height = 10
        # added lives
        self.lives = 3

    # DRAW THE CHARACTER
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.display.update()


class attack():


    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 10 * direction
        self.radius = radius
        self.direction = direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)




#Drawing on screen
def drawWindow(screen, player):
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    player.draw(screen)

    livesshown = font.render('Lives: ' + str(lives),1,(0,0,0))
    screen.blit(livesshown, (390,10))
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.update()




# GAME LOOP
player1 = Player(RED)
font = pygame.font.SysFont('comicsans', 30, True)
bullets = []
def game_loop():

    run_game = True

    while run_game:

        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run_game = False

        for bullet in bullets:
            if bullet.x < display_width and bullet.x > 0:
                bullet.x += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet)) #bullet gone from screen when hits boundary

# TEST THESE KEYS
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player1.x -= player1.velocity
            player1.left = True
            player1.right = False

        elif keys[pygame.K_RIGHT]:
            player1.x += player1.velocity
            player1.right = True
            player1.left = False

        elif keys[pygame.K_UP]:
            player1.y -= player1.velocity
            player1.left = False
            player1.right = False

        elif keys[pygame.K_DOWN]:
            player1.y += player1.velocity
            player1.left = False
            player1.right = False

        if keys[pygame.K_SPACE]:
            if player1.left:
                direction = -1
            else:
                direction = 1

            if len(bullets) < 1:
                bullets.append(attack(round(player1.x + player1.width//2), round(player1.y + player1.height//2), 3, RED, direction))


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







