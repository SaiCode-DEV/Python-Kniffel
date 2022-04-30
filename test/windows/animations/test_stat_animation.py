# pylint: disable=C
# pylint: disable=protected-access
from kniffel import common
from test.windows.window_test import WindowTest
from kniffel.windows.animations.start_animation import StartAnimation


class StartAnimationTest(WindowTest):

    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.start_animation: StartAnimation = None

    def setUp(self):
        super().setUp()
        self.start_animation = StartAnimation(self.window)

    def tearDown(self) -> None:
        del self.window

    def get_max_yx(self):
        return StartAnimation.get_required_size()

    def test_game_card_render(self):
        for loading in [*common.LOADING, common.LOGO]:
            self.start_animation.render()
            actual = self.get_screen_value()

            if len(actual) != len(loading):
                raise AssertionError("Expected and actual differ in length")
            iteration = 0
            for line in loading:
                self.assertEqual(
                    line.rstrip(),
                    actual[iteration].rstrip(),
                    f"did either not advance animation or did not render correctly error in line {iteration + 1}")
                iteration += 1
            self.start_animation.step_animation()
