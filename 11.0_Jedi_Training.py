import arcade
import random

"""
# 11.0 Jedi Training (50pts)  Name:Logan Mills



 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?
320, 240
2.) What are the variables dx and dy?
The velocity in the x and y directions
3.) How many pixels/sec does the ball move in the x-direction?
3
4.) How many pixels/sec does the ball move in the y-direction?
2
5.) Which method is run 60 times/second?
on_update (the parameter dt or delta time runs 60 times per second)
6.) What does this code do?   self.dx *= -1
Makes dx negative (Move backwards)
7.) What does this code do?  self.pos_y += self.dy
Takes the original y position and adds the number of pixels it needs to move
8.) What is the width of the window?
640
9.) What is this code checking?  self.pos_y > SH - self.rad:
If you're colliding with the ceiling (if y value is greater than one radius lower than the height to avoid clipping into the ceiling)
10.) What is this code checking? if self.pos_x < self.rad
If you're colliding with the left wall (If x value is less than one radius)
"""

"""
30 BOX BOUNCE PROGRAM (20pts)
---------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes
"""

SW = 600

SH = 600

box_num = 30


class Box:

    def __init__(self, x, y, dx, dy, side, col):

        self.x = x

        self.y = y

        self.dx = dx

        self.dy = dy

        self.side = side

        self.col = col

    def draw_box(self):

        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.col)

    def update_box(self):

        self.y += self.dy

        self.x += self.dx

        # Left
        if self.x <= 30 + self.side / 2:
            self.dx *= -1
            self.col = arcade.color.RED
        # Right
        if self.x >= SW - 30 - self.side / 2:
            self.dx *= -1
            self.col = arcade.color.YELLOW
        # Bottom
        if self.y <= 30 + self.side / 2:
            self.dy *= -1
            self.col = arcade.color.BLUE
        # Top
        if self.y >= SH - 30 - self.side / 2:
            self.dy *= -1
            self.col = arcade.color.NEON_GREEN



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.box_list = []

        for i in range(box_num):
            side = random.randint(10, 50)
            velocity_x = random.randint(-5, 5)
            velocity_y = random.randint(-5, 5)
            pos_x = random.randint(30 + int(side / 2), SW - 30 - int(side / 2))
            pos_y = random.randint(30 + int(side / 2), SH - 30 - int(side / 2))
            color = arcade.color.BLACK
            if velocity_x == 0 and velocity_y == 0:
                velocity_x += 1
                velocity_y += 1

            self.box = Box(pos_x, pos_y, velocity_x, velocity_y, side, color)
            self.box_list.append(self.box)

    def on_draw(self):

        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
        arcade.draw_rectangle_filled(15, SH/2, 30, SH-60, arcade.color.RED)
        arcade.draw_rectangle_filled(SW-15, SH / 2, 30, SH - 60, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(SW/2, 15, SW - 60, 30, arcade.color.BLUE)
        arcade.draw_rectangle_filled(SW/2, SH - 15, SW - 60, 30, arcade.color.NEON_GREEN)

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()


def main():

    window = MyGame(SW, SH, "30 Boxes")

    arcade.run()


if __name__ == "__main__":

    main()

"""
Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
"""

'''
SNOWFALL  (20pts)
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''

SW = 600

SH = 600


class Flake:

    def __init__(self, pos_x, pos_y, dy, rad, col):

        self.pos_x = pos_x

        self.pos_y = pos_y

        self.dy = dy

        self.rad = rad

        self.col = col

    def draw_flake(self):

        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_flake(self):

        self.pos_y += self.dy

        if self.pos_y < -self.rad:

            self.pos_x = random.randint(0, SW)
            self.pos_y = random.randint(SH, SH+100)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.flake_list = []

        for i in range(300):
            radius = random.randint(1, 3)
            velocity_y = random.randint(-4, -1)
            pos_x = random.randint(radius + 1, SW - radius - 1)
            pos_y = random.randint(radius + 1, SH - radius - 1)
            color = (255, 255, 255)
            if i == 10:
                color = (255, 0, 0)
            flake = Flake(pos_x, pos_y, velocity_y, radius, color)
            self.flake_list.append(flake)

    def on_draw(self):

        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()

        arcade.draw_rectangle_filled(SW/2, SH/2, SW, 10, arcade.color.DARK_BROWN)
        arcade.draw_rectangle_filled(SW/2, SH/2, 10, SH, arcade.color.DARK_BROWN)

    def on_update(self, dt):

        for flake in self.flake_list:
            flake.update_flake()


def main():

    window = MyGame(SW, SH, "Snowfall")

    arcade.run()


if __name__ == "__main__":

    main()
