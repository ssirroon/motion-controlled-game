"""
View module contains functions used to display sprites, background, hp, and
text to PyGame window.
"""

import pygame
from PIL import Image


class Sprite(pygame.sprite.Sprite):
    """
    Creates our character sprites
    Functions: update, calcnewpos
    Attributes:
        screen: Screen object
        vector: Inputted vector list
        sprite: Private sprite object containing path to .png and scaling
        rect: determining Cheems' start location
        clock: keeping in game time used to determine FPS cap
    """

    def __init__(self, cheems_path, vector, scale,
                 start_pos):
        pygame.sprite.Sprite.__init__(self)
        window_size = 500, 500  # width, height
        self.screen = pygame.display.set_mode(window_size)
        im_cheems = Image.open(cheems_path)  # returns a tuple
        self._sprite = add_character(cheems_path, tuple(ti/scale for ti in
                                                        im_cheems.size))
        self.vector = vector
        # Determine Cheems start location in window
        self.rect = self._sprite.get_rect(topleft=start_pos)
        # Initialise clock
        self.clock = pygame.time.Clock()

    def draw(self):
        """
        Draws sprite to given location on screen.
        """
        self.screen.blit(self._sprite, (self.rect.x, self.rect.y))

    def update(self):
        """
        Calculates new position of sprites.
        Returns tuple of two numbers representing new x and y coordinates.
        """
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        """
        Calculates new position of sprite.
        Args:
            rect: rectangular surface of sprite
            vector: list containing vertical and horizontal change
        Returns:
            New rectangular surface of moved sprite.
        """
        (d_x, d_y) = (vector[0], vector[1])
        return rect.move(d_x, d_y)


class Background():
    """
    Class containing screen and background.
    Functions: update, calcnewpos
    Attributes:
        screen: PyGame display
        background: surface of background image we are using
    """

    def __init__(self, bg_path, window_size):
        self.screen = pygame.display.set_mode(window_size)
        background = pygame.transform.scale(
            pygame.image.load(bg_path).convert_alpha(), window_size)
        # pygame.Surface(self.screen.get_size())
        self.background = background.convert()

    def start_screen(self):
        """
        Blit everything to the screen.
        """
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


def add_character(image, size):
    """
    Adds sprite onto display.
    Args:
        image: .png of sprite image
        size: tuple containing desired size of sprite
    Returns:
        Sprite object
    """
    sprite = pygame.image.load(image).convert_alpha()
    sprite = pygame.transform.scale(sprite, (size))
    sprite = pygame.transform.flip(
        sprite, True, False)  # surface, xbool, ybool
    return sprite


def print_to_disp(character1, move1):
    """
    Creates string representing what character used what move.
    Args:
        character1: string representing character name
        move1: string representing move name
    Returns:
        A string stating what character used what move.
    """
    text_str = character1 + " used the move " + move1
    return text_str


def main(background, enemy_path, vector_cheems, vector_enemy, scale_enemy,
         fight_text_1, fight_text_2, hp_path_cheems=None, hp_path_enemy=None):
    """
    Main function ran to display screen, sprites, background, text, and hp.
    Args:
        background: Background class
        enemy_path: file path to enemy sprite image
        vector_cheems: list of desired movement of Cheems
        vector_enemy: list containing desired movement of enemy
        scale_enemy: integer containing enemy scaling factor
        fight_text_1: string containing winning message
        fight_text_2: string containing losing message
        hp_path_cheems: file path to hp image
        hp_path_enemy: file path to hp image
    """
    # [initiate game environment here]
    # Initialise screen
    cheems_path = 'Images/samurai_cheems.png'
    scale_cheems = 7    # Cheems scaling factor
    start_pos_cheems = (15, 300)
    start_pos_enemy = (300, 100)
    # Create new instance of sprite class
    cheems = Sprite(cheems_path,
                    vector_cheems, scale_cheems, start_pos_cheems)
    enemy = Sprite(enemy_path,
                   vector_enemy, scale_enemy, start_pos_enemy)

    black = (0, 0, 0)
    white = (255, 255, 255)

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('PressStart2P-vaV7.ttf', 12)
    font_rules = pygame.font.Font('PressStart2P-vaV7.ttf', 8)

    font_fight = pygame.font.Font('PressStart2P-vaV7.ttf', 10)

    text1 = font.render('Up: Magic', True, black)
    text2 = font.render('Left: Attack', True, black)
    text3 = font.render('Right: Defense', True, black)
    text4 = font.render('Down : Quit', True, black)
    text5 = font_rules.render('Magic > Defense > Attack > Magic', True, black)
    text_fight_1 = font_fight.render(fight_text_1, True, white)
    text_fight_2 = font_fight.render(fight_text_2, True, white)
    # create a rectangular object for the
    # text surface object
    text_rect1 = text1.get_rect()
    text_rect2 = text2.get_rect()
    text_rect3 = text3.get_rect()
    text_rect4 = text4.get_rect()
    text_rect5 = text5.get_rect()
    fight_rect_1 = text_fight_1.get_rect()
    fight_rect_2 = text_fight_2.get_rect()
    # set the center of the rectangular object.
    text_rect1.topleft = (0, 45)
    text_rect2.topleft = (0, 60)
    text_rect3.topleft = (0, 75)
    text_rect4.topleft = (0, 90)
    text_rect5.topleft = (0, 105)
    fight_rect_1.center = (350, 400)
    fight_rect_2.center = (350, 370)
    # creating sprites representing character hps
    cheems_health = Sprite(hp_path_cheems, [0, 0], 8, (0, 0))
    enemy_health = Sprite(hp_path_enemy, [0, 0], 8, (350, 0))
    pygame.display.set_caption('Cheems Game!')

    time_counter = 0
    while time_counter < 50:
        time_counter += 1
        cheems.screen.blit(background.background, (0, 0))
        cheems.screen.blit(text1, text_rect1)  # Up movement info
        cheems.screen.blit(text2, text_rect2)  # Left movement info
        cheems.screen.blit(text3, text_rect3)  # Right movement info
        cheems.screen.blit(text4, text_rect4)  # Down movement info
        cheems.screen.blit(text5, text_rect5)  # Down movement info
        cheems.screen.blit(text_fight_1, fight_rect_1)
        cheems.screen.blit(text_fight_2, fight_rect_2)
        cheems.draw()
        enemy.draw()
        # if hp_path_cheems:
        cheems_health.draw()
        # if hp_path_enemy:
        enemy_health.draw()
        time_end = 0
        if hp_path_cheems == 'Images/health_empty.png':
            while time_end < 50:
                cheems.screen.fill((0, 0, 0))
                font = pygame.font.Font('PressStart2P-vaV7.ttf', 16)
                text = font.render('Game Omver', True, (225, 225, 225))
                text_rect = text.get_rect()
                text_rect.center = (250, 250)
                cheems.screen.blit(text, text_rect)
                time_end += 1
        if hp_path_enemy == 'Images/health_empty.png':
            while time_end < 50:
                cheems.screen.fill((255, 255, 224))
                font = pygame.font.Font('PressStart2P-vaV7.ttf', 16)
                text = font.render('You Wimn!', True, (100, 225, 100))
                text_rect = text.get_rect()
                text_rect.center = (250, 250)
                cheems.screen.blit(text, text_rect)
                time_end += 1
        pygame.display.flip()
        # [call ball's update function]
        cheems.update()
        enemy.update()
        # Determine fps cap
        cheems.clock.tick(60)


def hp_to_path(health):
    """
    Contains paths to varying health bars.
    Args:
        health: integer representing sprite health
    Returns:
        String containing path to image
    """
    hp_full_path = 'Images/health_full.png'
    hp_half_path = 'Images/health_half.png'
    hp_empty_path = 'Images/health_empty.png'

    hp_path = hp_full_path
    if health == 10:
        hp_path = hp_half_path
    elif health == 0:
        hp_path = hp_empty_path
    return hp_path
