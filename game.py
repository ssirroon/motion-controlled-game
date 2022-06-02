"""
Integrated file of model, view and controller of the game.
"""
import time
import random
import pygame
import model
import controller
import view
import sound


def game(size, bg_path, enemy_path, hp_full_path, game_sound,
         vector_cheems, vector_enemy, scale_enemy, enemy_name):
    """
    script of final game

    Args:

    Returns:
    """

    game_1 = model.Model()

    cheems_hp_path = enemy_hp_path = hp_full_path

    background = view.Background(bg_path, size)
    background.start_screen()

    view.main(background, enemy_path, [0, 0], [0, 0],
              scale_enemy, "", "", hp_full_path, hp_full_path)
    sound.init_music(game_sound)  # initializing in-game music
    sound.loop_music()  # start in-game music

    while 1:
        swipe_detection_1 = controller.SwipeDetection()
        time.sleep(1)
        enemy_move = game_1.enemy_move()
        vector_enemy = swipe_detection_1.move_to_pos(enemy_move)

        view.main(background, enemy_path, [0, 0], vector_enemy,
                  scale_enemy, "", "", cheems_hp_path,
                  enemy_hp_path)

        cheems_move = swipe_detection_1.determine_move()

        if cheems_move == "end":
            swipe_detection_1.quit()
            pygame.display.quit()
            pygame.mixer.music.stop()
            break

        vector_cheems = swipe_detection_1.move_to_pos(cheems_move)

        fight = model.fight_result(cheems_move, enemy_move)
        result = game_1.deal_damage(fight[0])

        health_list = game_1.current_health()
        cheems_health = int(health_list[0])
        cheems_hp_path = view.hp_to_path(cheems_health)

        enemy_health = health_list[1]
        enemy_hp_path = view.hp_to_path(enemy_health)

        fight_text_cheems = view.print_to_disp("Cheems",
                                               cheems_move)
        fight_text_enemy = view.print_to_disp(enemy_name,
                                              enemy_move)

        view.main(background, enemy_path, vector_cheems,
                  [0, 0], scale_enemy, fight_text_cheems, fight_text_enemy,
                  cheems_hp_path, enemy_hp_path)

        if result == "lose":
            if random.randrange(1, 10) > 6:
                sound.init_music("Sound/big_loss.mp3")
                sound.loop_music()
                time.sleep(2.5)
            else:
                sound.init_music("Sound/loss.mp3")
                sound.loop_music()
                time.sleep(4)
            swipe_detection_1.quit()
            pygame.display.quit()
            pygame.mixer.music.stop()
            break
        if result == "win":
            sound.init_music("Sound/win.mp3")
            sound.loop_music()
            time.sleep(2.5)
            swipe_detection_1.quit()
            pygame.display.quit()
            pygame.mixer.music.stop()
            break
    swipe_detection_1.quit()
