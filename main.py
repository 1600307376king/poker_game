import sys

import pygame
from card_ctrol import CardCtrl
from game_mouse import GameMouse


def run_game():
    pygame.init()
    # screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("poker game")
    card_ctrl = CardCtrl()
    mouse = GameMouse()
    fps_count = 0
    while True:
        try:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pos = pygame.mouse.get_pos()
                #     mouse.set_pos(pos)
                #     print(f"GameMouse: {mouse.rect}")
                #     print("x = {}, y= {}".format(*pos))
                #     card_ctrl.click_event(mouse)
            pos = pygame.mouse.get_pos()
            mouse.set_pos(pos)
            card_ctrl.touch_event(mouse)
            card_ctrl.update_cards_pos()
            card_ctrl.display()
            # screen.fill(bg)
            # screen.blit(card_img, rect)
            # screen.blit(txt_surf, txt_rect)
            pygame.display.update()
            fps_count += 1
        except Exception as e:
            print(e)
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()
