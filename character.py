"""
Contains character class that determines character name, moves, and hp and is
used to save and update character-related data.
"""
import random

class Character():
    """
    Class for setting characters

    Attributes:
        health: how much hp a character has (max hp)
        moveset: a list of moves a character could use

    """

    def __init__(self, health, moveset):
        self._current_hp = health
        self._moveset = moveset

    def current_hp(self):
        """
        returns current hp
        """
        return self._current_hp

    def current_move(self):
        """
        determine the move randomly out of a set of moves

        returns a string of the move selected
        """
        return random.choice(self._moveset)

    def decrease_hp(self, damage):
        """
        decreases hp by a certain amount

        Args:
            damage: an int that indicates the amount of damage

        Returns:
            current_hp: an int indicating the character's current hp
        """
        self._current_hp -= damage
        return self._current_hp
