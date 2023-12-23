import random
from collections import deque
import numpy as np
import pygame
from card.base_card import BaseCard


class CardGroups(pygame.sprite.Group):

    def add(
            self, *sprites
    ):
        super().add(*sprites)

    def draw(self, surface, bgsurf=None, special_flags=0):
        super().draw(surface, bgsurf=bgsurf, special_flags=special_flags)
        for card in self.spritedict:
            surface.blit(card.card_txt, card.get_txt_rect())

    def get_list(self):
        ls = []
        for card in self.spritedict:
            ls.append(card)
        return ls


class CardRules:
    def __init__(self):
        self.card_num = 10
        self.card_name = "ABCDEFGHIJ"
        self.card_random_id_ls = random.sample(range(self.card_num), k=self.card_num)
        # self.cards = {BaseCard(self.card_name[i], x_offset=i) for i in range(self.card_num)}
        self.us_cards_id = set(random.sample(self.card_random_id_ls, k=self.card_num // 2))
        self.other_cards_id = set(self.card_random_id_ls) - self.us_cards_id
        self.us_cards = CardGroups()
        self.other_cards = CardGroups()
        self.has_raise_cards = deque()

    def load_us_card(self):
        for i, x in zip(self.us_cards_id, range(self.card_num // 2)):
            sp = BaseCard(self.card_name[i], x_offset=x)
            self.us_cards.add(sp)
        return self.us_cards

    def load_other_card(self):
        for i, x in zip(self.other_cards_id, range(self.card_num // 2)):
            self.other_cards.add(BaseCard(self.card_name[i], x_offset=x, is_front=False))
        return self.other_cards

    def to_cos(self, center_card):
        us_card_len = len(self.us_cards)
        print(f"index: {center_card}")
        # 0
        # 0-5
        # 1
        # -1 - 4
        # 2
        # -2 - 3
        pre = -center_card

        x = np.array(range(pre, us_card_len + pre), np.float32)
        print(f"x: {x}")
        return 10 * np.cos(0.5 * x) + 10

    def to_gas(self, center_card):
        sig = 1
        miu = 0
        us_card_len = len(self.us_cards)
        # print(f"index: {center_card}")
        # 0
        # 0-5
        # 1
        # -1 - 4
        # 2
        # -2 - 3
        pre = -center_card

        x = np.array(range(pre, us_card_len + pre), np.float32)
        # print(f"x: {x}")
        return np.multiply(
            np.power(
                np.sqrt(
                    2 * np.pi) * sig, -1),
            np.exp(-np.power(x - miu, 2) / 2 * sig ** 2)) * 40

    def to_raise_cards(self, card):
        self.has_raise_cards.append(card)
        # print("raise")
        self._move_card(card)

    def to_drop_cards(self):
        # print("drop")
        if len(self.has_raise_cards) > 0:
            card = self.has_raise_cards.popleft()
            self._move_card(card, direction=1)

    def _move_card(self, card, direction=-1):
        card_ls = self.us_cards.get_list()
        cur_card_index = card_ls.index(card)
        # print(f"cur card: {card}")
        offset_arr = self.to_gas(cur_card_index)
        # print(f"cur offset: {offset_arr}")
        for card, y_offset in zip(card_ls, offset_arr):
            # card.rect.y += direction*np.floor(y_offset)
            if direction == 1:
                card.down_speed = 1
                card.up_speed = 0
            else:
                card.up_speed = 1
                card.down_speed = 0
            # expect_dis = np.floor(y_offset)
            card.mov_distance = np.floor(y_offset)
            # print(card.mov_distance)
