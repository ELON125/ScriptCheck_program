from pynput.mouse import Listener
import asyncio
import logging
from datetime import datetime

print('Logging has been started, make sure this window stay open through the whole recording proccess\nWhen you have started you screen recording please click 10 times while holding your mouse up so we can easily sync the 2 recordings')

logging.basicConfig(filename=f"mouse_log.txt", level=logging.DEBUG, format='%(asctime)s:%(message)s')

movement = []

def on_move(x, y):
    movement.append(x + y)
    logging.info(f"Mouse moved to {x}, {y}")

def on_click(x, y, button, pressed):             
    if pressed:
        logging.info(f"Mouse clicked to {x}, {y} with {button}")

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

          