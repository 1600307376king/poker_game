import pygame
from collections import deque
from common.base_config import WIN_WIDTH, WIN_HEIGHT
from game_rules.card_rules import CardRules


class CardCtrl:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg = (127,) * 3
        self.card_rules = CardRules()
        self.us_cards = self.card_rules.load_us_card()
        self.other_cards = self.card_rules.load_other_card()
        self.select_card_deq = deque()
        self.card_be_select_span = 20
        # print(self.us_cards)
        # print(self.other_cards)

    def update_cards_pos(self):
        for card in self.us_cards:
            # print(f"mov_distance: {card.mov_distance}")
            card.update_pos()

        for card in self.other_cards:
            card.update_pos()

    def display(self):
        self.screen.fill(self.bg)
        self.us_cards.draw(self.screen)
        self.other_cards.draw(self.screen)

    def select_card(self, card):
        if card in self.select_card_deq:
            return
        # if self.select_card_deq:
        #     self.reset_card_pos()
        # card.rect.y -= self.card_be_select_span
        self.card_rules.to_raise_cards(card)
        self.select_card_deq.append(card)

    def reset_card_pos(self):
        if self.select_card_deq:
            self.select_card_deq.popleft()
            # pop_card.rect.y += self.card_be_select_span
            self.card_rules.to_drop_cards()

    def click_event(self, mouse):

        collide_obj = pygame.sprite.spritecollideany(mouse, self.us_cards)
        if collide_obj:
            # print(f"card: {collide_obj} and mouse is collide!")
            self.select_card(collide_obj)

    def touch_event(self, mouse):
        collide_obj = pygame.sprite.spritecollideany(mouse, self.us_cards)
        if collide_obj:
            # print(f"card: {collide_obj} and mouse is collide!")
            self.select_card(collide_obj)
        else:
            self.reset_card_pos()
