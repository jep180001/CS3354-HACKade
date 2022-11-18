import unittest
import arcade
import hackade

class winTests(unittest.TestCase):
    def test_win_4(self):
        game.score = 4
        assert game.has_won() != True, "player shouldn't win with too few points"
    def test_win_5(self):
        game.score = 5
        self.assertTrue(game.has_won()), "player should win with exact points"
    def test_win_6(self):
        game.score = 6
        assert game.has_won(), "player should win with extra points"
        
class moveTests(unittest.TestCase):
    def test_jump_start(self):
        game.on_key_press(game, arcade.key.UP)
        game.physics_engine.update()
        assert game.player_sprite.center_y > 96, "player should jump from on top of ground"
    def test_jump_air(self):
        game.player_sprite.center_y = 200
        game.on_key_press(game, arcade.key.UP)
        game.physics_engine.update()
        assert game.player_sprite.center_y < 200, "player shouldn't jump in air"
    def test_jump_box(self):
        game.player_sprite.center_x = 256
        game.player_sprite.center_y = 192
        game.on_key_press(game, arcade.key.UP)
        game.physics_engine.update()
        assert game.player_sprite.center_y > 192, "player should jump from on top of box"

    def test_left_start(self):
        game.player_sprite.center_y = 96
        game.player_sprite.center_x = 64
        game.on_key_press(game, arcade.key.LEFT)
        game.physics_engine.update()
        assert game.player_sprite.center_x < 64, "player should move left on unobstructed ground"
    def test_left_air(self):
        game.player_sprite.center_y = 200
        game.player_sprite.center_x = 64
        game.on_key_press(game, arcade.key.LEFT)
        game.physics_engine.update()
        assert game.player_sprite.center_x < 64, "player should move left in unobstructed air"
    def test_left_box(self):
        game.player_sprite.center_x = 314
        game.on_key_press(game, arcade.key.LEFT)
        game.physics_engine.update()
        assert not (game.player_sprite.center_x < 314), "player shouldn't move left into obstruction"

    def test_right_start(self):
        game.player_sprite.center_y = 96
        game.player_sprite.center_x = 64
        game.on_key_press(game, arcade.key.RIGHT)
        game.physics_engine.update()
        assert game.player_sprite.center_x > 64, "player should move right on unobstructed ground"
    def test_right_air(self):
        game.player_sprite.center_y = 200
        game.player_sprite.center_x = 64
        game.on_key_press(game, arcade.key.RIGHT)
        game.physics_engine.update()
        assert game.player_sprite.center_x > 64, "player should move right in unobstructed air"
    def test_right_box(self):
        game.player_sprite.center_x = 208
        game.on_key_press(game, arcade.key.RIGHT)
        game.physics_engine.update()
        assert not (game.player_sprite.center_x > 208), "player shouldn't move right into obstruction"
    

if __name__ == "__main__":
    game = hackade.MyGame()
    game.setup()
    unittest.main() # run all tests
