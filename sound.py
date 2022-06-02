"""
Handling Pygame soundtrack.
"""
import pygame


def init_music(path):
    """
    This method loads the music and initializes the mixer for PyGame.
    Inputs:
        path: string containing path to sound file
    Returns:
        Music object
    """
    pygame.mixer.init()
    music = pygame.mixer.music.load(path)
    return music


def loop_music():
    """
    This function loops the music. No inputs or arguments.
    """
    pygame.mixer.music.play(-1)
