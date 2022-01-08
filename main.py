from utils import read_paths, click_on_img
import sys, time
import signal
from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        sys.exit()
    try:
        k = key.char
    except:
        k = key.name
    if str(k).lower() == "d":
        print("Searching...")
        process()
    
def process():
    paths = read_paths('img')
    for path in paths:
        click_on_img(path)
    time.sleep(1)


if __name__ == '__main__':
    print("Start...")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()