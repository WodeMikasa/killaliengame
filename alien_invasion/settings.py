class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        # self.ship_speed = 1.5
        self.ship_limit = 1
        # self.bullet_speed = 1.0
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 55
        # 外星人设置
        # self.alien_speed = 1.0
        self.fleet_drop_speed = 45
        # 加快游戏节奏速度
        self.speedup_scale = 1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        # fleet_direction为1向右，-1向左
        # self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed=1.5
        self.bullet_speed=3.0
        self.alien_speed=1.0
        self.alien_points=50

        self.fleet_direction=1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
