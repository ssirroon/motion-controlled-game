"""
This file is designed to test the functionality of view.py
"""
from pathlib import Path
from view import Sprite, print_to_disp
import view


def test_calcnewpos():
    """
    Test movement in a certain direction
    """
    test_sprite=Sprite(f"{Path.home()}/cheems-game/cheems.jpg", [10,10],\
         7, (15,300))
    test_sprite_final_pos=Sprite(f"{Path.home()}/cheems-game/cheems.jpg",\
         [10,10], 7, (25,310))
    test_sprite.rect= test_sprite.get_rect(topleft=(15,300))

    new_postion=test_sprite.calcnewpos(test_sprite.rect,[10,10])
    assert new_postion==test_sprite_final_pos.get_rect(topleft=(25,310))
def test_calcnewpos2():
    """
    Test movement in the negative direction
    """
    test_sprite=Sprite(f"{Path.home()}/cheems-game/cheems.jpg", [10,10],\
         7, (15,300))
    test_sprite_final_pos=Sprite(f"{Path.home()}/cheems-game/cheems.jpg",\
         [10,10], 7, (5,290))
    test_sprite.rect= test_sprite.get_rect(topleft=(15,300))

    new_postion=test_sprite.calcnewpos(test_sprite.rect,[-10,-10])
    assert new_postion==test_sprite_final_pos.get_rect(topleft=(5,290))
def test_print_to_disp():
    """
    Test print is operational
    """
    text=print_to_disp("cheems","attack")
    assert text=="cheems used the move attack"

def test_hp_to_path():
    """
    Test that full health is displayed correctly
    """
    path=view.hp_to_path(20)
    assert path == 'Images/health_full.png'

def test_hp_to_path2():
    """
    Test that half health is displayed correctly
    """
    path=view.hp_to_path(10)
    assert path == 'Images/health_half.png'

def test_hp_to_path3():
    """
    Test that full health is displayed correctly
    """
    path=view.hp_to_path(0)
    assert path == 'Images/health_empty.png'
