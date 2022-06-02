"""
Module runs our Cheems game
"""
import pygame
import game

pygame.init()
size = width, height = 500, 500
BG_PATH = 'Images/pokemon_b.png'
ENEMY_PATH = 'Images/stronk_doge.png'
HP_FULL_PATH = 'Images/health_full.png'
GAME_SOUND = "Sound/Pokemon_Ruby.mp3"
vector_cheems = [0, 0]
vector_enemy = [0, 0]
SCALE_ENEMY = 8
ENEMY_NAME = "Doge"

game.game(size, BG_PATH, ENEMY_PATH, HP_FULL_PATH, GAME_SOUND,
          vector_cheems, vector_enemy, SCALE_ENEMY, ENEMY_NAME)
