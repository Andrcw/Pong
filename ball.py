import pygame


class Ball():

    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # speed
        self.dx = 8
        self.dy = 8

        # score
        self.left_score = 0
        self.right_score = 0

    def update(self):
        """Idk"""

    def blitme(self):
        self.screen.blit(self.image, self.rect)