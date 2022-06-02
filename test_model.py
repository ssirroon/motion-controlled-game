"""
This file is designed to test the functionality of model.py
"""
from model import Model
from model import fight_result


def test_fight_result1():
    """
    Test case for if player and enemy both use attack
    """
    assert fight_result("attack", "attack") == \
        (["cheems", "enemy"], "attack")


def test_fight_result2():
    """
    Test case for if player attacks and the enemy defends
    """
    assert fight_result("attack", "defend") == \
        (["cheems"], "defend")


def test_fight_result3():
    """
    Test case for if player uses magic and enemy defends
    """
    assert fight_result("magic", "defend") == \
        (["enemy"], "magic")


def test_damage_dealt():
    """
    Test case to make sure Cheems has taken the correct amount of damage
    """
    test_game = Model()
    Model.damage_dealt(test_game, "cheems")
    assert Model.current_health(test_game) == [10, 20]


def test_damage_dealt2():
    """
    Test case to make sure the enemy has taken the correct amount of damage
    """
    test_game = Model()
    Model.damage_dealt(test_game, "enemy")
    assert Model.current_health(test_game) == [20, 10]


def test_deal_damage_loss():
    """
    Test case for a lost game
    """
    test_game = Model()
    Model.damage_dealt(test_game, "cheems")
    Model.damage_dealt(test_game, "cheems")
    ending = Model.deal_damage(test_game, ["enemy"])
    assert ending == "lose"


def test_deal_damage_win():
    """
    Test case for a won game
    """
    test_game = Model()
    Model.damage_dealt(test_game, "enemy")
    Model.damage_dealt(test_game, "enemy")
    ending = Model.deal_damage(test_game, ["cheems"])
    assert ending == "win"
