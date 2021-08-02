from .tools import _get_screen, _move_mouse, _move_and_click

   
class InterfaceController():
    def __init__(self, account_name=None, account_pass=None):
        self.account_name = account_name
        self.account_pass = account_pass

    def get_screen(self):
        return _get_screen()

    def move_mouse(self, x, y, duration=0.5):
        _move_mouse(x, y, duration)

    def move_and_click(self, x, y, duration=0.5):
        _move_and_click(x, y, duration)