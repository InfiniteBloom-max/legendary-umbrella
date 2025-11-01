"""
USB Mouse Artist Sparkly Heart Drawer And Motivates You !

"""

# import setion 

import time 
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard import Keycode
from adafruit_hid.mouse import Mouse 
import math 
import random 

# Initialize HID Devices
kbd = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

# function sections arranged carefully :

def press_key(Keycode):
    """ press and releases a key"""
    kbd.press(keycode)
    time.sleep(0.05)
    kbd.release_all()
    time.sleep(0.1)


def open_paint():
    print("Opening MS Paint...")

    # Press Windows Key 
    kbd.press(Keycode.GUI)
    time.sleep(0.1)
    kbd.release_all()
    time.sleep(0.5)

    #Type "paint"
    kbd.send(Keycode.P)
    time.sleep(0.05)
    kbd.send(Keycode.A)
    time.sleep(0.05)
    kbd.send(Keycode.I)
    time.sleep(0.05)
    kbd.send(Keycode.N)
    time.sleep(0.05)
    kbd.send(Keycode.T)
    time.sleep(1)


    # Press Enter to Open Paint 
    press_key(Keycode.ENTER)
    time.sleep(3) # to wait until paint opens up 


    print("Paint Opened!")


def move_mouse_Smooth(dx, dy , steps=10):
    step_x = dx / steps
    step_y = dy / steps


    for _ in range(steps):
        mouse.move(int(step_x), int(step_y))
        time.sleep(0.01)



def click():
    mouse.click(Mouse.Left_Button)
    time.sleep(0.05)


def heart_x(t):
    return 16*math.sin(t)**3

def heart_y(t):
    return -(13 * math.cos(t) -5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t))

def select_pencil_tool():
    print("Selecting Pencil Tool...")
    time.sleep(0.5)

    kbd.press(Keycode.ALT)
    kbd.press(Keycode.H)
    time.sleep(0.05)
    kbd.release_all()
    time.sleep(0.3)

    press_key(Keycode.p)
    time.sleep(0.5)
    print("Pencil Tool Selected")

# function to draw the heart with the pencil clicks
def draw_sparkly_heart():
    print("Starting to draw sparkly heart")
    print("Moving to canvas center...")


    # getting the cursor to the middle approximately
    center_offset_x = 400
    center_offset_y = 300

    move_mouse_Smooth(center_offset_x, center_offset_y, steps=30)
    time.sleep(0.8)


    print("Activating Canvas...")
    click()
    time.sleep(0.5)

    # scale factor of the heart
    scale = 8 

    # number of particles used to make the heart sprakling
    num_particles = 300

    print("Drawing the Sparkly Particles ")

    for i in range(num_particles):
        t = (i/num_particles) * 2 * math.pi
        noise - random.uniform(-1.5, 1.5)

        x = heart_x(t) * scale + noise * 3
        y = heart_y(t) * scale + noise * 3

        target_x = int(x)
        target_y = int(y)

        move_mouse_Smooth(target_x, target_y, steps=3)
        click()
        time.sleep(0.02)

        move_mouse_Smooth(-target_x, - target_y , steps=2)

        if random.random() < 0.3 :
            center_offset_x = random.randint(-15, 15)
            center_offset_y =  random.randint(-15,15)
            move_mouse_Smooth(target_x + offset_x , target_y + offset_y, steps=2)
            click()
            time.sleep(0.02)
            move_mouse_Smooth(-(target_x + offset_x), -(target_y + offset_y), steps=2)
    print("Sparkly Heart completed")


def add_signature():
    print("Adding a Signature")

    move_mouse_Smooth(100, 250, steps=15)
    time.sleep(0.3)

    # to be customized
    signature_moves = [

    ]

    mouse.press(Mouse.LEFT_BUTTON)
    for dx , dy in signature_moves:
        move_mouse_Smooth(dx , dy , steps=3)
    mouse.release_all()


    print("signature added!")


def main():
    # Main Program 
    print("=== USB Mouse Artist ===")
    print("Preparing to draw Sparkly Heart")

    time.sleep(2)

    open_paint()

    select_pencil_tool()

    draw_sparkly_heart()

    add_signature()

    print("Masterpiece Complete!")
    print("Check out your Sparkly Heart in MS Paint")

if __name__ == "__main__":
    main()
