import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """显示得分信息得类"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game=ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.perp_ships()

    def prep_score(self):
        """将得分转化为一副渲染的图像"""
        # score_str = str(self.stats.score)
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 1250
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.score_rect.centerx
        self.high_score_rect.top = self.score_rect.top+50

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """将等级渲染为图像"""
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.settings.bg_color)

        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+60

    def perp_ships(self):
        """显示还余下多少艘飞船"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
