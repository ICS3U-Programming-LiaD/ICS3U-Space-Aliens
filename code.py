#!/usr/bin/env python3
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
        keys = ugame.buttons.get_pressed()
        if keys and ugame.K_K:
            print("A")
        if keys and ugame.K_O:
            print("B")
        if keys and ugame.K_START:
            print("Start")
        if keys and ugame.K_SELECT:
            print("Select")
        if keys and ugame.K_RIGHT:
            bird.move(bird.x + 1, bird.y)
        if keys and ugame.K_LEFT:
            bird.move(bird.x - 1, bird.y)
        if keys and ugame.K_UP:
            bird.move(bird.x, bird.y - 1)
        if keys and ugame.K_DOWN:
            bird.move(bird.x, bird.y + 1)

        # Update game Logic

        # redraw Bird
        game.render_sprites([bird])
        game.tick()

        pass


if __name__ == "__main__":
    game_scene()
