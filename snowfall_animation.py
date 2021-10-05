import random
import math
import arcade

Width = 800
Height = 600
Title = "Snowfall"


class snow_fall:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def reset_snow(self):

        # reset snowflake to a random position above the screen
        self.y = random.randrange(Height, Height + 100)
        self.x = random.randrange(Width)
    

class snowfall(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def start_snowfall(self):
        self.snowfall_list = []
        for _i in range(50):

            # create snowfall instance
            snowfall = snow_fall()

            # randomly position the snowfall
            snowfall.x = random.randrange(Width)
            snowfall.y = random.randrange(Height + 200)

            # other variables for the snowfall
            snowfall.size = random.randrange(8)
            snowfall.speed = random.randrange(20, 40)
            snowfall.angle = random.uniform(math.pi, math.pi * 2)

            # add snowflake to snowfall list
            self.snowfall_list.append(snowfall)
        

    def on_draw(self):
        arcade.start_render()

        # draw the current position of each snowfall
        for snowfall in self.snowfall_list:
            arcade.draw_circle_filled(snowfall.x, snowfall.y, snowfall.size, arcade.color.WHITE)
    
        def _on_update(self, delta_time):

            # animate all the snowfall falling
            for snowfall in self.snowfall_list:
                snowfall.y -= snowfall.speed * delta_time

                # check if snowfall is below the screen
                if snowfall.y < 0:
                    snowfall.reset_snow()
            
                # makes snowfall move side to side
                snowfall.x += snowfall.speed * \
                    math.cos(snowfall.angle) * delta_time
                snowfall.angle += 1 * delta_time

        # set the background color
        arcade.set_background_color(arcade.color.BLUE)


screen = snowfall(800, 600, "Snow")
screen.start_snowfall()
arcade.run()
