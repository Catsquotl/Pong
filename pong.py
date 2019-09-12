"""
Platformer Game
"""
import arcade
import random
import math

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pong"

class Ball(arcade.Sprite):
    pass



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.player_list = None
        self.ball_list = None

        self.Player1 = None
        self.player2 = None
        self.ball = None

        self.move = None


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()

        """ setup players """
        self.Player1 = arcade.Sprite("images/paddle_1.png")
        self.Player1.center_x = 0
        self.Player1.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.Player1)

        self.Player2 = arcade.Sprite("images/paddle_1.png")
        self.Player2.center_x = SCREEN_WIDTH
        self.Player2.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.Player2)

        """ setup ball """
        self.ball = Ball("images/ball.png", 0.25)
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball_list.append(self.ball)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Code to draw the screen goes here
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 2, 1000, [255,255,255])
        self.player_list.draw()
        self.ball_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.Player1.change_y = 5
        if key == arcade.key.S:
            self.Player1.change_y = -5
        if key == arcade.key.UP:
            self.Player2.change_y = 5
        if key == arcade.key.DOWN:
            self.Player2.change_y = -5
        if key == arcade.key.SPACE:
            self.ball.angle = 0
            self.ball.forward(3)
 
    def on_key_release(self, key, modiefiers):
        if key == arcade.key.W:
            self.Player1.change_y = 0
        if key == arcade.key.S:
            self.Player1.change_y = 0
        if key == arcade.key.UP:
            self.Player2.change_y = 0
        if key == arcade.key.DOWN:
            self.Player2.change_y = 0
        if key == arcade.key.SPACE:
            pass

    def update(self, delta_time):
            self.player_list.update()
            self.ball_list.update()
            hit = arcade.check_for_collision_with_list(self.ball, self.player_list)
            if len(hit) != 0:
                self.ball.stop()
                if self.ball.angle == 0:
                    self.ball.angle = 180
                else:
                    self.ball.angle = 0
                self.ball.forward(3)

def main():
    """ Main method """
    window = MyGame()
    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()
