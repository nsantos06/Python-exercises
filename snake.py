import pygame, random
from pygame.locals import * 

def on_grind_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2 
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Cobra')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grind_random()
apple = pygame.Surface((10, 10))
apple.fill((255,0,0))

lsd_pos = on_grind_random()
lsd = pygame.Surface((10, 10))
lsd.fill((0, 191, 255))

my_direction = LEFT 
pontos = 0
fonte = pygame.font.SysFont('cambria', 15, bold = True, italic = True)

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    screen.fill((0,0,0))

    msg = f'Pontos: {pontos}' 
    txt = fonte.render(msg, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grind_random()
        snake.append((0,0))
        pontos = pontos + 1

    if collision(snake[0], lsd_pos):
        lsd_pos = on_grind_random()
        pontos = pontos - 1
        

        
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    
    
    
    screen.blit(apple,apple_pos)
    screen.blit(lsd, lsd_pos)
    screen.blit(txt, (450,40))
    
    for pos in snake:
        screen.blit(snake_skin,pos)
    

    pygame.display.update()
