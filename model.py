"""
A class that contains our character moves and associated methods.
file containing model class (decision making and game logic)
"""
import character


class Model():
    """
    Class containing Cheems and enemy moves and attack/defense/magic points.

    Attributes:
        cheems: An instance of a character class called "Cheems that the player
        can control.
        enemy: An instance of a character class that has randomly generated
        moves.
    """

    def __init__(self):
        moveset = ["attack", "defend", "magic"]
        self.cheems = character.Character(20, moveset)  # (40, moveset)
        self.enemy = character.Character(20, moveset)  # (40, moveset)

    def enemy_move(self):
        """
        returns the randomly chosen enemy move
        """
        return self.enemy.current_move()

    def current_health(self):
        """
        returns a list of both cheems and enemy's current health to
        determine end game conditions
        """
        return [self.cheems.current_hp(), self.enemy.current_hp()]

    def damage_dealt(self, fighter):
        """
        decreases the respective hp of the fighter

        Args:
            fighter: the chracter being dealt damage

        returns:
            none
        """
        if fighter == "cheems":
            self.cheems.decrease_hp(10)
        elif fighter == "enemy":
            self.enemy.decrease_hp(10)

    def deal_damage(self, damage_list):
        """
        deals damage to a list of characters using a certain move
        doesnt return anything until end game conditions are met
        one of the characters reaching 0 hp

        Args:
            damage_list: list of characters to be damaged

        returns:
            none unless end conditions are met then it returns
            condition: a string containing the end condition
                "win" or "lose"
        """
        # if len(list) == 1:
        #     self.damage_dealt(list[0])
        #     print("Cheems has " + str(self.cheems.current_hp())+" hp.")
        #     print("Enemy has " + str(self.enemy.current_hp())+" hp.")
        #     print("turn end")
        # else:
        for elem in damage_list:
            self.damage_dealt(elem)
        enemy_hp = self.enemy.current_hp()
        cheems_hp = self.cheems.current_hp()
        # if enemy_hp > 0 and cheems_hp > 0:
        if enemy_hp > 0 and cheems_hp > 0:
            print("Cheems has " + str(cheems_hp) + " hp.")
            print("Enemy has " + str(enemy_hp) + " hp.")
            print("End of turn.")
        elif cheems_hp == 0:
            condition = "lose"
            return condition
        elif enemy_hp == 0:
            condition = "win"
            return condition
        return None


def fight_result(cheems_move, enemy_move):
    """
    returns the result of a fight using both moves

    defend beats attack, attack beats magic, magic beats defend

    Args:
        cheems_move: a string that says the move cheems uses
            out of attack magic or defend
        enemy_move: a string that says the move enemy uses
            out of attack magic or defend

    returns a list of character who are being damaged and
    what move they are damaged by
    """
    #enemy_move = self.enemy.current_move()
    # enemy_move="attack"
    if cheems_move == enemy_move:
        return (["cheems", "enemy"], cheems_move)
    if cheems_move == "attack":
        if enemy_move == "defend":
            target = ["cheems"]
            move = enemy_move
        else:
            target = ["enemy"]
            move = cheems_move
    if cheems_move == "defend":
        if enemy_move == "attack":
            target = ["enemy"]
            move = cheems_move
        else:
            target = ["cheems"]
            move = enemy_move
    if cheems_move == "magic":
        if enemy_move == "attack":
            target = ["cheems"]
            move = enemy_move
        else:
            target = ["enemy"]
            move = cheems_move
    return (target, move)
