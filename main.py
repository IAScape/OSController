from .tools import _get_screen, _move_mouse

   
class InterfaceController():
    def __init__(self, account_name=None, account_pass=None):
        self.account_name = account_name
        self.account_pass = account_pass

    def get_screen(self):
        return _get_screen()

    def move_mouse(self, x, y):
        return _move_mouse(x, y)