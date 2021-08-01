import numpy as np
from PIL import Image
import pyautogui
import time
   

def get_screen():
    """
    return:
    - window (PIL.Image): Full Screen
    - game (PIL.Image): Cropped screen without interface
    """
    img = pyautogui.screenshot()
    game_img = img.crop((884, 6, 1910, 677))
    return img.convert('RGB'), game_img.convert('RGB')
  

if __name__ == '__main__':
    time.sleep(2)
    _, img = get_screen()
    print(img.size)
    img.save('temp/game.png')