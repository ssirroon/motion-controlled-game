from character import Character
from game import game
import pytest
import pygame
import model


def test_fight_result1():
    # Test case for if player and enemy both use attack
    assert model.fight_result("attack", "attack") == \
        (["cheems", "enemy"], "attack")


def test_fight_result2():
    # Test case for if player attacks and the enemy defends
    assert model.fight_result("attack", "defend") == \
        (["cheems"], "defend")


def test_fight_result3():
    # Test case for if player uses magic and enemy defends
    assert model.fight_result("magic", "defend") == \
        (["enemy"], "magic")


def test_damage_dealt():
    # Test case to make sure Cheems has taken the correct amount of damage
    test_game = model.Model()
    test_game.damage_dealt("cheems")
    assert test_game.current_health() == [10, 20]


def test_damage_dealt2():
    # Test case to make sure the enemy has taken the correct amount of damage
    test_game = model.Model()
    test_game.damage_dealt("enemy")
    assert test_game.current_health() == [20, 10]


def test_deal_damage_loss():
    # Test case for a lost game
    test_game = model.Model()
    test_game.damage_dealt("cheems")
    ending = test_game.deal_damage(["cheems"])
    assert ending == "lose"


def test_deal_damage_win():
    # Test case for a won game
    test_game = model.Model()
    test_game.damage_dealt("enemy")
    ending = test_game.deal_damage(["enemy"])
    assert ending == "win"
