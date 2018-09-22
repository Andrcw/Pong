import pygame

class Right():

    def __init__(self, screen):
        self.screen = screen

        # Load line image and get its rect
        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at certain location
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 10
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 10

    def blitme(self):
        self.screen.blit(self.image, self.rect)
