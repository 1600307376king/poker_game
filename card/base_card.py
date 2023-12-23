import pygame
from pygame.sprite import Sprite, Group
from common.base_config import BLACK, WHITE


class BaseCard(pygame.sprite.Sprite, pygame.sprite.Group):
    def __init__(self, name, x_offset=0, y_offset=0, is_front=True):
        # Sprite.__init__(self)
        super().__init__()
        Group.__init__(self)
        self.name = name
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.is_front = is_front
        self.card_span = 10
        self.right_speed = 0
        self.left_speed = 0
        self.down_speed = 0
        self.up_speed = 0
        self.mov_distance = 0
        self.us_card_bottom = 576
        self.card_img_file = "img/card/card_model.png" if self.is_front else "img/card/back_card_model.png"
        self.card_img = pygame.image.load(self.card_img_file)
        self.image = self.card_img.convert_alpha()
        self.rect = self.image.get_rect()
        self.card_txt = None
        self._width = self.image.get_width()
        self._height = self.image.get_height()

        self.set_card_pos()
        self.set_card_font()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __bool__(self):
        if self is None:
            return False
        else:
            return True

    def set_card_pos(self):
        init_pos_x = 450
        init_pos_y = 640 if self.is_front else 120

        self.rect.center = init_pos_x + self.x_offset * (self.rect.width + self.card_span), init_pos_y

    def set_card_font(self):
        font = pygame.font.SysFont("Arial", 36)
        font_color = BLACK if self.is_front else WHITE
        self.card_txt = font.render(self.name, True, font_color)

    def update_card_pos(self, x, y):
        self.rect.center = x, y

    def get_txt_rect(self):
        rect = self.rect
        txt_rect = rect.center[0] - self.card_txt.get_width() // 2, rect.center[1] - self.card_txt.get_height() // 2
        return txt_rect

    def update_pos(self):
        # pass
        self.rect.x += self.right_speed - self.left_speed
        if self.rect.y + self.down_speed < self.us_card_bottom:
            self.rect.y += self.down_speed
        if self.rect.y - self.up_speed > self.us_card_bottom - self.mov_distance:
            self.rect.y -= self.up_speed

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
