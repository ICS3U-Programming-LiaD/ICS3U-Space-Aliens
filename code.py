#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 15th, 2022
# A version of Space Aliens on PyBadge

# imported some libraries
import ugame
import stage


def game_scene():

    # imported an image and put it into a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # grid of an image background
    background = stage.Grid(image_bank_background, 10, 8)
    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    print("Dogs vs Cats")

    while True:

        pass


if __name__ == "__main__":
    game_scene()
