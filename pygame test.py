import pygame

class Score(object):
    def __init__(self, bg, score=100):
        self.score = score
        self.score_rect = pygame.Rect((10,0), (200,50))
        self.bg = bg

    def update(self):
        screen = pygame.display.get_surface() 

        WHITE = (255, 255, 255)
        BG = (10, 10, 10)

        score = "Score: " + str(self.score)
        text = font.render(score, True, WHITE, BG)
        text.set_colorkey(BG)

        screen.blit(
        self.bg, 
        self.score_rect)

        screen.blit(text, 
        self.score_rect)


def main():
    pygame.init()

    #initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Score Window')

    #initialize background
    bg = pygame.Surface((screen.get_size())).convert()
    bg.fill((30, 30, 30))
    screen.blit(bg, (0, 0))

    #initialize scoreboard
    score_board = Score(bg)

    while True:
        score_board.update()
        pygame.display.flip()

main()
