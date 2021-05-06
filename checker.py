from pynput.mouse import Listener, Button, Controller
import time
import sys 


mouse = Controller()
filename = input("What file would you like to review:\n")
review_speed = input("How quickly would you like to review the file(quick, normal or slow?):\n")

docOpen = open(filename, "r").readlines()

for line in docOpen:
    if "clicked" in line:
        print (line)
        pass
    else:
        position = str(line).replace("Mouse moved to", "").replace(",","")
        mouse.position = (int(position.split(" ")[1]), int(position.split(" ")[2]))
        if review_speed == "quick":
            time.sleep(0.0001)
        elif review_speed == "normal":
            time.sleep(0.001)
        elif review_speed == "slow":
            time.sleep(0.01)


def on_click(x, y, button, pressed):             
    if pressed:
        sys.exit()

with Listener(on_click=on_click) as listener:
    listener.join()