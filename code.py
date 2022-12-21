#!/usr/bin/env python3
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 15th, 2022
# A version of Space Aliens on PyBadge

# imported some libraries
import ugame
import stage
import constants


def game_scene():

    # imported an image and put it into a variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # grid of an image background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    bird = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # The display that will show up and refreshing it with 60 hertz
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [bird] + [background]
    game.render_block()

    while True:
        # get user input i.e buttons click
        keys = ugame.buttons.get_pressed()
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

        # redraw Bird
        game.render_sprites([bird])
        game.tick()

        pass


if __name__ == "__main__":
    game_scene()
