import arcade
import random

SPRITE_SCALING_SNAKE = 0.2

SPRITE_SCALING_APPLE = 0.15

APPLE_COUNT = 1

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 650

SNAKE_SPEED_X = 5

SNAKE_SPEED_Y = 5

colour = (arcade.color.RED,arcade.color.GREEN, arcade.color.BLUE, arcade.color.PURPLE, arcade.color.YELLOW, arcade.color.BLACK)

class Snake(arcade.Sprite):
    def update(self):
        self.center_x = self.center_x + self.change_x
        self.center_y = self.center_y + self.change_y

        if self.right <= 0:
            self.left = SCREEN_WIDTH

        elif self.left >= SCREEN_WIDTH:
            self.right = 0

        elif self.top <= 0:
            self.bottom = SCREEN_HEIGHT

        elif self.bottom >= SCREEN_HEIGHT:
            self.top = 0
class Apple(arcade.Sprite):

    def update(self):
        self.center_y = self.center_y
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


    def draw(self):
        """NOTHING IN YET"""


class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        #Variables that hold sprite list
        self.snake_list = None
        self.apple_list = None

        # Player info
        self.snake_sprite = None
        self.score = 0
        self.texture1 = None
        self.texture2 = None
        self.texture3 = None
        self.texture4 = None
        self.texture5 = None
        self.texture6 = None
        self.texture7 = None
        self.texture8 = None
        self.texture9 = None
        self.texture10 = None
        self.texture11 = None
        self.texture12 = None

        self.set_mouse_visible(False)

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, random.choice(colour))

        arcade.set_background_color(arcade.color.GREEN)

    def setup(self):
        self.snake_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()

        self.score = 0

        self.snake_sprite = Snake("Snake.png", SPRITE_SCALING_SNAKE)

        self.snake_sprite.center_x = SCREEN_WIDTH / 2
        self.snake_sprite.center_y = SCREEN_HEIGHT / 2

        self.snake_list.append(self.snake_sprite)

        name = "Snake.png"
        self.texture1 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 1.25)
        self.snake_sprite.append_texture(self.texture1)
        self.texture2 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 1.4)
        self.snake_sprite.append_texture(self.texture2)
        self.texture3 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 1.55)
        self.snake_sprite.append_texture(self.texture3)
        self.texture4 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 1.70)
        self.snake_sprite.append_texture(self.texture4)
        self.texture5 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 1.85)
        self.snake_sprite.append_texture(self.texture5)
        self.texture6 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2)
        self.snake_sprite.append_texture(self.texture6)
        self.texture7 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.15)
        self.snake_sprite.append_texture(self.texture7)
        self.texture8 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.3)
        self.snake_sprite.append_texture(self.texture8)
        self.texture9 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.45)
        self.snake_sprite.append_texture(self.texture9)
        self.texture10 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.6)
        self.snake_sprite.append_texture(self.texture10)
        self.texture11 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.75)
        self.snake_sprite.append_texture(self.texture11)
        self.texture12 = arcade.load_texture(name, 0, 0, 0, 0, False, False, 2.9)
        self.snake_sprite.append_texture(self.texture12)

        print(self.snake_sprite.get_texture())




        for i in range(APPLE_COUNT):
            apple = Apple("Apple.png", SPRITE_SCALING_APPLE)

            apple.center_x = random.randint(50, SCREEN_WIDTH - 50)
            apple.center_y = random.randint(50, SCREEN_HEIGHT - 50)

            self.apple_list.append(apple)
    def on_draw(self):
        arcade.start_render()
        self.apple_list.draw()
        self.snake_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.snake_sprite.change_y = SNAKE_SPEED_Y
            self.snake_sprite.change_x = 0
            self.snake_sprite.angle = 90

        elif key == arcade.key.LEFT:
            self.snake_sprite.change_x = -SNAKE_SPEED_X
            self.snake_sprite.change_y = 0
            self.snake_sprite.angle = 180

        elif key == arcade.key.DOWN:
            self.snake_sprite.change_y = -SNAKE_SPEED_Y
            self.snake_sprite.change_x = 0
            self.snake_sprite.angle = 270

        elif key == arcade.key.RIGHT:
            self.snake_sprite.change_x = SNAKE_SPEED_X
            self.snake_sprite.change_y = 0
            self.snake_sprite.angle = 0




            #snake = Snake("Snake_copy.png", 0.8)
            #snake.angle = 90


        #if key == arcade.key.LEFT:
            #snake = Snake("Snake_copy.png", 0.8)
            #snake.angle = 180


        #if key == arcade.key.DOWN:
            #snake = Snake("Snake_copy.png", 0.8)
            #snake.angle = 270

        #if key == arcade.key.RIGHT:
            #snake = Snake("Snake_copy.png", 0.8)
            #snake.angle = 0

    def update(self, delta_time):

        self.apple_list.update()
        self.snake_list.update()

        hit_list = arcade.check_for_collision_with_list(self.snake_sprite, self.apple_list)
        snake_hit_list = arcade.check_for_collision_with_list(self.snake_sprite, self.snake_list)

        for apple in hit_list:
            self.score = self.score + 1
            apple.center_x = random.randint(50, SCREEN_WIDTH - 50)
            apple.center_y = random.randint(50, SCREEN_HEIGHT - 50)


        for apple in hit_list:
            if self.score == 5:
                self.snake_sprite.set_texture(1)

        for apple in hit_list:
            if self.score == 10:
                self.snake_sprite.set_texture(2)

        for apple in hit_list:
            if self.score == 15:
                self.snake_sprite.set_texture(3)

        for apple in hit_list:
            if self.score == 20:
                self.snake_sprite.set_texture(4)

        for apple in hit_list:
            if self.score == 25:
                self.snake_sprite.set_texture(5)

        for apple in hit_list:
            if self.score == 30:
                self.snake_sprite.set_texture(6)

        for apple in hit_list:
            if self.score == 35:
                self.snake_sprite.set_texture(7)

        for apple in hit_list:
            if self.score == 40:
                self.snake_sprite.set_texture(8)

        for apple in hit_list:
            if self.score == 45:
                self.snake_sprite.set_texture(9)

        for apple in hit_list:
            if self.score == 50:
                self.snake_sprite.set_texture(10)

        for apple in hit_list:
            if self.score == 55:
                self.snake_sprite.set_texture(11)

        for apple in hit_list:
            if self.score == 60:
                self.snake_sprite.set_texture(12)






        for snake in snake_hit_list:
            snake.kill()







def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()