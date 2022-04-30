class MockStartWindow:
    def __init__(self):
        self.render_called = False
        self.step_animation_called = False

    def render(self):
        self.render_called = True

    def step_animation(self):
        self.step_animation_called = True
