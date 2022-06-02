# Cheemsy Memes: A Cheems Game

This repository contains a motion-controlled Cheems game that uses MVC structure. Created by Shamama Sirroon, Jaclyn Ho, and Jack Levitsky.

### Game Overview

The objective of this game is to correctly respond to the enemy's moves and swipe in the correct direction for Cheems to win the battle.

### Installation and Setup

The following packages will need to be installed to run the game:

```
pip install pygame
pip install mediapipe
pip install utilidades
pip install Pillow
```
To run the unit tests, run `pip install pytest`.

### File Structure

The following .py files contain our game functions:

* `run_game.ipynb` and `run_game.py`: Either can be run to play our game.
* `game.py`: This file contains the integration between our model, view, and controller classes.
* `model.py`: Contains our characters' moves, respective hps, and the damage points associated with each move.
* `view.py`: Contains our sprite class and display class, as well a main function that displays our desired information to our window.  
* `controller.py`: Uses the MediaPipe API to create a SwipeDetection class that can determine desired move based on the direction of a swipe.
* `character.py`: Contains our class that sets characters by creating atributes containing their attacks, health, and action choices.
* `sprites.py`: Contains a Cheems class that has the cheems     .png object, and functions to calculate the new positions of the sprite as they move.
* `sound.py`: Contains functions to play in-game music.

### Static Files

`/Images` contains the images we use for our sprites and background. `/Sound` contains the .mp3 files we use for our sounds. Paths to these files are hard-coded, so when downloading all the files ensure the file structure remains the same.

### Website
Our website can be accessed at [here](https://bookish-disco-d0f14f98.pages.github.io/). Our presentation is linked [here](https://drive.google.com/file/d/1MV2sFGLHtfv1iMcCYdEDy_kpfPEYFoUT/view?usp=sharing).

### References
We used the [MediaPipe API](https://google.github.io/mediapipe/) for our hand tracking: https://google.github.io/mediapipe/.

To implement our view module, we used [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.

We used an [online font](https://www.fontspace.com/press-start-2p-font-f11591) to create our 8-bit typography.

For our visuals, we used the following references:

* [Health Bar](https://www.kindpng.com/imgv/owbTmm_health-bar-png-game-health-bar-png-transparent/)
* [Pokemon Background](https://www.pokecommunity.com/showthread.php?t=302401)
* [Stronk Doge](https://steamcommunity.com/app/1383720)
* [Cheems](https://www.reddit.com/r/dogelore/comments/e76g65/revisited_full_body_cheems_png_color_corrected/)

For our music, we used [Pokemon battle music](https://www.youtube.com/watch?v=LaAGsbtETIg&t=76s&ab_channel=Pokeli) that we used a [YouTube to mp3](https://getx.topsandtees.space/EpA8Aen4kK) converter to convert to a usable mp3 file. For our winning and losing sound effects, the sounds can be found at the following links:

* [Winning](https://www.youtube.com/watch?v=Ad204YupWhc&ab_channel=RCMS)
* [Losing](https://www.myinstants.com/instant/sad-violin-the-meme-one/)
* [Losing Easter Egg](https://www.youtube.com/watch?v=ekL881PJMjI&ab_channel=GamingSoundFX)