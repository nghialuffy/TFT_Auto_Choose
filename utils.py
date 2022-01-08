from pathlib import Path
import pyautogui
import time
import pywinauto
import cv2
import numpy as np


def screenshot():
    size = pyautogui.size()
    bottom_screen_height = int(size[1]/2)
    background = pyautogui.screenshot(
        # region=(0, bottom_screen_height, size[0], bottom_screen_height)
    )
    background.save('./tmp/screenshot.png')

def locate_on_screen(img_path):
    screenshot()
    img_rgb = cv2.imread('./tmp/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(img_path, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        return (pt[0], pt[1],  w , h)
    return None

# read all paths from folder img
def read_paths(folder):
    paths = []
    for img in Path(folder).glob('*'):
        paths.append(str(img))
    return paths

def click_on_img(img_path):
    if not img_path:
        return
    location = locate_on_screen(img_path)
    if location:
        x = int(location[0] + location[2] / 2)
        y = int(location[1] + location[3] / 2)
        print(f"Img = {img_path.lower()}: x = {x}, y ={y}")
        pywinauto.mouse.move((x, y))
        pyautogui.click()
