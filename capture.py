import pygame
import random
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Capture")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FPS = 60
VEL = 5

RED_WID, RED_HEI = 50, 50
red = pygame.Rect(425, 225, RED_WID, RED_HEI)

circleRadiusTimer = 0
circleRadius = 25
circleX = float(random.randint(25, WIDTH - 25))
circleY = float(random.randint(25, HEIGHT - 25))


def draw(circleX, circleY, circleRadius):
    WIN.fill(WHITE)
    pygame.draw.circle(WIN, BLUE, (circleX, circleY), circleRadius)
    pygame.draw.rect(WIN, RED, red)
    pygame.display.update()


def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + RED_WID < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y - VEL + RED_HEI < HEIGHT - 10:
        red.y += VEL


def circle_size(circleRadius, circleRadiusTimer):
    if circleRadiusTimer >= 1000:
        circleRadius = circleRadius - 6.25
        circleRadiusTimer = 0

    return circleRadius, circleRadiusTimer


def score(circleX, circleY, circleRadius):
    if red.x < circleX < red.x + 50 and red.y < circleY < red.y + 50:
        circleX = float(random.randint(25, WIDTH - 25))
        circleY = float(random.randint(25, HEIGHT - 25))
        circleRadius = 25

    return circleX, circleY, circleRadius


def text():
    FONT = pygame.freetype.SysFont("Arial", 100, True, False)
    FONT.render_to(WIN, (100, 200), "YOU LOST! :(", (0, 0, 0))
    pygame.display.flip()


def main():
    global circleRadiusTimer, circleRadius, circleX, circleY

    clock = pygame.time.Clock()
    run = True
    while run:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        red_move(keys_pressed, red)

        circleRadiusTimer += dt
        circleRadius, circleRadiusTimer = circle_size(circleRadius, circleRadiusTimer)

        if circleRadius != 0:
            circleX, circleY, circleRadius = score(circleX, circleY, circleRadius)

        else:
            text()
            pygame.time.wait(3000)
            run = False

        draw(circleX, circleY, circleRadius)
    pygame.quit()


if __name__ == "__main__":
    main()
