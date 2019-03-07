import pygame


width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Card Race")

clientNumber = 0
win_condition = False



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

        self.rect = (self.x, self.y, self.width, self.height)
        pygame.display.update()

# Function to move character left, right, up, down
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

#Setting game boundaries

        if self.x < 0:
            self.x = 0

        if self.x > width - self.width:
            self.x = width - self.width

        if self.y < 0:
            self.y = 0

        if self.y > height - self.height:
            self.y = height - self.height





    def winner(self):
        run = True
        while run:
            pygame.init()
            win = pygame.display.set_mode((750, 750))
            winner_font = pygame.font.Font(None, 70)
            winner_text = winner_font.render("WINNER", True, (0, 0, 0))
            win.blit(winner_text, (60, 384))
            pygame.display.flip()




def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()
 
#GAME LOOP
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

