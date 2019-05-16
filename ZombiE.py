import arcade

WIDTH = 1366
HEIGHT = 768


class Player:
    def __init__(self, x=400, y=125, width=20):
        self.x = x
        self.y = y
        self.width = width



    # def draw_player(self, x, y, width):
    #     height = width * 2
    #     radius = width / 2
    #     arm_width = width / 4
    #     # torso
    #     arcade.draw_xywh_rectangle_filled(x, y, width, height, arcade.color.BLUE)
    #     # head
    #     arcade.draw_circle_filled(x + radius, y + height + radius, radius, arcade.color.YELLOW)
    #     # legs
    #     arcade.draw_xywh_rectangle_filled(x, y - height, radius - 1, height, arcade.color.RED)
    #     arcade.draw_xywh_rectangle_filled(x + radius + 1, y - height, radius - 1, height, arcade.color.RED)
    #     # arms
    #     arcade.draw_xywh_rectangle_filled(x - arm_width, y + height * 0.2, arm_width, height * 0.8, arcade.color.RED)
    #     arcade.draw_xywh_rectangle_filled(x + width, y + height * 0.2, arm_width, height * 0.8, arcade.color.RED)


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    ground()
    # loading_screen(WIDTH/3, HEIGHT/3)


def ground():
    arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT, arcade.color.GREEN)


def loading_screen(x, y):
    # TITLE
    arcade.draw_text("ZombiE", 380, 575, arcade.color.YELLOW, 120)
    # START GAME BUTTON
    arcade.draw_xywh_rectangle_filled(x, y + 200, WIDTH / 3, HEIGHT / 12, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text("NEW  GAME", 540, 475, arcade.color.BLACK, 40, font_name="TIMES NEW ROMAN")
    # CONTINUE GAME BUTTON
    arcade.draw_xywh_rectangle_filled(x, y + 100, WIDTH / 3, HEIGHT / 12, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text(" CONTINUE ", 545, 375, arcade.color.BLACK, 40, font_name="TIMES NEW ROMAN")
    # OPTIONS BUTTON
    arcade.draw_xywh_rectangle_filled(x, y, WIDTH / 3, HEIGHT / 12, arcade.color.BATTLESHIP_GREY)
    arcade.draw_text("OPTIONS", 575, 275, arcade.color.BLACK, 40, font_name="TIMES NEW ROMAN")


def on_key_press(self, key, modifiers):
    if key == arcade.key.UP:
        self.change_y = 5
    elif key == arcade.key.DOWN:
        self.change_y = -5
    if key == arcade.key.RIGHT:
        self.change_x = 5
    elif key == arcade.key.LEFT:
        self.change_x = -5

    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
