
#!/usr/bin/env python3
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 15th, 2022
# A version of Space Aliens on PyBadge

# imported some libraries
import constants
import stage
import ugame
import time
import random


def splash_scene():

    start_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(start_sound)

    # imported an image and put it into a variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background image to
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    background.tile(2, 2, 1)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 1)  # blank white

    background.tile(2, 3, 1)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 1)  # blank white

    background.tile(2, 4, 1)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 1)  # blank white

    background.tile(2, 5, 1)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 1)  # blank white

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [background]
    game.render_block()

    # game loop to repeat forever
    while True:
        # Wait 2 seconds
        time.sleep(2.0)
        # Go to the menu scene
        menu_scene()


def menu_scene():

    # imported an image and put it into a variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # The Text Objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.Red_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("Flying Bird")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.Red_PALETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("Press Start")
    text.append(text2)

    # grid of an image background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:

        # get user input i.e buttons click
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        game.tick()


def game_scene():

    # imported an image and put it into a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # grid of an image background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Adding in the Sprites
    bird = stage.Sprite(image_bank_sprites, 4, 75, 66)
    cloud = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # buttons to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Gets the Shooting Sound ready for use
    bird_sound = open("pew2.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [bird] + [cloud] + [background]
    game.render_block()

    while True:

        # get user input i.e buttons click
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_O != 0:
            # Changing the state of the A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

                # Doing nothing with the B button
            if keys & ugame.K_X:
                pass
            if keys & ugame.K_O:
                pass
            if keys & ugame.K_START:
                pass
            if keys & ugame.K_SELECT:
                pass

        if keys & ugame.K_RIGHT:
            # moves the sprite to the right
            if bird.x <= constants.SCREEN_X - 16:
                bird.move(bird.x + 1, bird.y)
            # makes sure the bird doesn't go off the right side of the screen
            else:
                bird.move(constants.SCREEN_X - constants.SPRITE_SIZE, bird.y)
        if keys & ugame.K_LEFT:
            # moves the sprite to the left
            if bird.x >= 0:
                bird.move(bird.x - 1, bird.y)
            # keep it at the 0 mark
            else:
                bird.move(0, bird.y)

        if keys & ugame.K_UP:
            #  moves the sprite up
            if bird.y >= 0:
                bird.move(bird.x, bird.y - 1)
            # Keeps the sprite at the 0 mark
            else:
                bird.move(bird.x, 0)

        if keys & ugame.K_DOWN:
            # moves the sprite down
            if bird.y <= constants.SCREEN_Y - 16:
                bird.move(bird.x, bird.y + 1)
            # keep the sprite from going past the bottom
            else:
                bird.move(bird.x, constants.SCREEN_Y - constants.SPRITE_SIZE)

            # Update game Logic
            # Plays the shooting sound when A is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(bird_sound)
        # redraw Bird
        game.render_sprites([bird] + [cloud])
        game.tick()

        pass


if __name__ == "__main__":
    splash_scene()
