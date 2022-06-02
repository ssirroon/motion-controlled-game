"""
Unit tests for character class
"""
from character import Character

# test_cheems = Character(20, ["attack", "defend", "magic"])
# test_enemy = Character(20, ["attack", "defend", "magic"])


def test_current_hp():
    """
    Test case ensuring cheems's current hp can be returned
    """
    test_cheems = Character(20, ["attack", "defend", "magic"])
    assert test_cheems.current_hp() == 20


def test_decrease_hp():
    """
    Test case where cheems has taken 10 damage
    """
    test_cheems = Character(20, ["attack", "defend", "magic"])
    assert test_cheems.decrease_hp(10) == 10
