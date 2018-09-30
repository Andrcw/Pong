import pygame

import pygame.sysfont


class Start():

    def __init__(self, screen):
        screen.fill((0, 0, 0))
        self.title = pygame.font.SysFont("monospace", 150)
        self.sub = pygame.font.SysFont("monospace", 80)
        self.medium = pygame.font.SysFont("monospace", 40)

        self.white = (255, 255, 255)
        self.green = (50, 255, 50)
        self.red = (255, 0, 0)

        # for pong
        self.pong = self.title.render("PONG", True, self.white)
        self.pong_btn = self.pong.get_rect()
        self.pong_btn.centerx = screen.get_rect().centerx
        self.pong_btn.centery = screen.get_rect().centery - 200

        # For Subtitle
        self.sub = self.sub.render("AI - NO WALLS", True, self.green)
        self.sub_btn = self.sub.get_rect()
        self.sub_btn.centerx = screen.get_rect().centerx
        self.sub_btn.centery = screen.get_rect().centery - 120

        # For difficulty level
        self.dl = self.medium.render("Difficulty Level:", True, self.white)
        self.dl_btn = self.dl.get_rect()
        self.dl_btn.centerx = screen.get_rect().centerx - 200
        self.dl_btn.centery = screen.get_rect().centery

        # Difficulty easy
        self.easy = self.medium.render("Easy", True, self.red)
        self.easy_btn = self.easy.get_rect()
        self.easy_btn.centerx = screen.get_rect().centerx - 10
        self.easy_btn.centery = screen.get_rect().centery

        # Difficulty medium
        self.med = self.medium.render("Medium", True, self.white)
        self.med_btn = self.med.get_rect()
        self.med_btn.centerx = screen.get_rect().centerx + 120
        self.med_btn.centery = screen.get_rect().centery

        # Difficulty hard
        self.hard = self.medium.render("Hard", True, self.white)
        self.hard_btn = self.hard.get_rect()
        self.hard_btn.centerx = screen.get_rect().centerx + 250
        self.hard_btn.centery = screen.get_rect().centery

    def start_blit(self, screen):
        # Blit text
        screen.blit(self.pong, self.pong_btn)
        screen.blit(self.sub, self.sub_btn)
        screen.blit(self.dl, self.dl_btn)
        screen.blit(self.easy, self.easy_btn)
        screen.blit(self.med, self.med_btn)
        screen.blit(self.hard, self.hard_btn)
        pygame.display.flip()

    def start_update(self, left, left_top):
        # if mouse collides with easy
        if self.easy_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.red)
                    self.med = self.medium.render("Medium", True, self.white)
                    self.hard = self.medium.render("Hard", True, self.white)
                    left.speed = 5
                    left_top.speed = 5
                    print(left.speed)

        # if mouse click medium
        if self.med_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.white)
                    self.med = self.medium.render("Medium", True, self.red)
                    self.hard = self.medium.render("Hard", True, self.white)
                    print(left.speed)

        # if mouse click hard
        if self.hard_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.white)
                    self.med = self.medium.render("Medium", True, self.white)
                    self.hard = self.medium.render("Hard", True, self.red)
                    left.speed = 10
                    left_top.speed = 10
                    print(left.speed)