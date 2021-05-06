from pynput.mouse import Listener
import asyncio
import logging
from datetime import datetime

print('Logging has been started, make sure this window stay open through the whole recording proccess')

logging.basicConfig(filename=f"mouse_log.txt", level=logging.DEBUG, format='%(message)s')

movement = []

def on_move(x, y):
    movement.append(x + y)
    logging.info(f"Mouse moved to {x}, {y}")
    print(f"Mouse moved to {x}, {y}")

def on_click(x, y, button, pressed):             
    if pressed:
        logging.info(f"Mouse clicked to {x}, {y} with {button}")

with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

          