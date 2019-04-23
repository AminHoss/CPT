import arcade


WIDTH = 1366
HEIGHT = 768


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    loading_screen(WIDTH/3, HEIGHT/3)


def loading_screen(x, y):
    #OPTIONS BUTTON
    arcade.draw_xywh_rectangle_filled(x,y, WIDTH/3, HEIGHT/ 12, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text("OPTIONS", )


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Zombie Apocalypse")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()