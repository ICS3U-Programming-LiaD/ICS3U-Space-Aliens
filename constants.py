#!/usr/bin/env python3
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Dec 15th, 2022
# This is the constants file for the Space Aliens like game

# Screen size is 160 x 128
SCREEN_X = 160
SCREEN_Y = 128

SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8

# Sprites are 16 x 16
SPRITE_SIZE = 16
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# States of the Button
button_state = {
    "button up": "up",
    # Only state where we want sound to happen
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still_pressed",
    "button_released": "released",
}
