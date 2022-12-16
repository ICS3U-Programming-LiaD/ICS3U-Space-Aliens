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
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # grid of an image background
    background = stage.Grid(image_bank_background, 10, 8)

    bird = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, 60)
    game.layers = [bird] + [background]
    game.render_block()

    while True:
        # get user input i.e buttons click

        # Update game Logic

        # redraw Bird
        game.render_sprites([bird])
        game.tick()

        pass


if __name__ == "__main__":
    game_scene()
