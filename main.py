#Petit test

import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        pass

    def setup(self):
        pass

    def on_draw(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
