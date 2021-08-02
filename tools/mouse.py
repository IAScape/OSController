import pyautogui
   

def move_mouse(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration, tween=pyautogui.easeInOutQuad)

def move_and_click(x, y, duration=0.5):
    move_mouse(x, y, duration)
    pyautogui.click()