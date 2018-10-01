import pygame

import pygame.sysfont


class Start:
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
        self.speed = 5  # Starts off on easy

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

        # Play up to:
        self.play = self.medium.render("Play to:", True, self.white)
        self.play_btn = self.play.get_rect()
        self.play_btn.centerx = screen.get_rect().centerx - 120
        self.play_btn.centery = screen.get_rect().centery + 80

        # 5
        self.five = self.medium.render("5", True, self.red)
        self.five_btn = self.five.get_rect()
        self.five_btn.centerx = screen.get_rect().centerx - 20
        self.five_btn.centery = screen.get_rect().centery + 80
        self.score = 5  # starts off at 5 points

        # 10
        self.ten = self.medium.render("10", True, self.white)
        self.ten_btn = self.ten.get_rect()
        self.ten_btn.centerx = screen.get_rect().centerx + 40
        self.ten_btn.centery = screen.get_rect().centery + 80

        # 15
        self.fif = self.medium.render("15", True, self.white)
        self.fif_btn = self.fif.get_rect()
        self.fif_btn.centerx = screen.get_rect().centerx + 100
        self.fif_btn.centery = screen.get_rect().centery + 80

        # Start button
        self.start = self.medium.render("Start", True, self.white)
        self.start_btn = self.hard.get_rect()
        self.start_btn.centerx = screen.get_rect().centerx
        self.start_btn.centery = screen.get_rect().centery + 200

    def start_blit(self, screen):
        # Blit text
        screen.blit(self.pong, self.pong_btn)
        screen.blit(self.sub, self.sub_btn)
        screen.blit(self.dl, self.dl_btn)
        screen.blit(self.easy, self.easy_btn)
        screen.blit(self.med, self.med_btn)
        screen.blit(self.hard, self.hard_btn)
        screen.blit(self.start, self.start_btn)
        screen.blit(self.play, self.play_btn)
        screen.blit(self.five, self.five_btn)
        screen.blit(self.ten, self.ten_btn)
        screen.blit(self.fif, self.fif_btn)
        pygame.display.flip()

    def start_update(self, ball):
        # if mouse collides with easy
        if self.easy_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.red)
                    self.med = self.medium.render("Medium", True, self.white)
                    self.hard = self.medium.render("Hard", True, self.white)
                    self.speed = 5

        # if mouse click medium
        if self.med_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.white)
                    self.med = self.medium.render("Medium", True, self.red)
                    self.hard = self.medium.render("Hard", True, self.white)
                    self.speed = 10

        # if mouse click hard
        if self.hard_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy = self.medium.render("Easy", True, self.white)
                    self.med = self.medium.render("Medium", True, self.white)
                    self.hard = self.medium.render("Hard", True, self.red)
                    self.speed = 20

        # if mouse click 5
        if self.five_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.five = self.medium.render("5", True, self.red)
                    self.ten = self.medium.render("10", True, self.white)
                    self.fif = self.medium.render("15", True, self.white)
                    self.score = 5

        # if mouse click 10
        if self.ten_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.five = self.medium.render("5", True, self.white)
                    self.ten = self.medium.render("10", True, self.red)
                    self.fif = self.medium.render("15", True, self.white)
                    self.score = 10

        # if mouse click 15
        if self.fif_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.five = self.medium.render("5", True, self.white)
                    self.ten = self.medium.render("10", True, self.white)
                    self.fif = self.medium.render("15", True, self.red)
                    self.score = 15

        # if mouse click start
        if self.start_btn.collidepoint(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball.start_active = False
                    ball.game_active = True
