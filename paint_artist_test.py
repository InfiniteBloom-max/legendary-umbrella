# This code is the same from the code.py with ammendments to test it directly in the windows 11 PC
# This is the Local Test Version using pyautogui


# import section

import pyautogui
import time
import math 
import random 


# adding a saftey feature to abort the process if anything becomes different from what is expected 
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

def open_paint():
    pyautogui.press('win')
    time.sleep(0.5)

    pyautogui.write('paint', interval=0.05)
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(3)

    print("Paint Opened!")

def heart_x(t):
    return 16 * math.sin(t) **3

def heart_y(t):
    return -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))

def select_pencil_tool():
    print('selecting pencil tool...')
    time.sleep(0.5)

    pyautogui.hotkey('alt', 'h')
    time.sleep(0.3)
    pyautogui.press('p')
    time.sleep(0.5)
    print("Pencil tool selected")


def draw_sparkly_heart():
    print("Starting to draw Sparkly heart...")

    screen_width, screen_height = pyautogui.size()

    center_x = screen_width// 2 
    center_y = screen_height//2

    print(f"Mocing to canvas center : ({center_x , center_y})")

    pyautogui.moveTo(center_x, center_y , duration = 1)
    time.sleep(0.5)

    print("Activating canvas")
    pyautogui.click(center_x, center_y)
    time.sleep(0.5)

    scale = 8

    num_particles = 300

    print(f"Drawing from center positiion : ({center_x} {center_y})")
    print("Drawing sparkly particles...")


    for i in range (num_particles):
        t = (i / num_particles) * 2 * math.pi
        noise = random.uniform(-1.5, 1.5)

        x = heart_x(t) * scale + noise * 3 
        y = heart_y(t) * scale + noise * 3

        target_x = center_x + int(x)
        target_y = center_y + int(y)

        pyautogui.click(target_x, target_y)
        time.sleep(0.01)

        if random.random() < 0.3 :
            offset_x = random.randint(-15, 15)
            offset_y = random.randint(-15, 15)
            pyautogui.click(target_x + offset_x, target_y + offset_y)
            time.sleep(0.01)

        if( i + 1 ) % 50 == 0:
            print(f"Progress : {i + 1}/ {num_particles} particles drawn")

    print("Sparkly heart completed !")

def add_signature():
    print("Adding signature...")
    time.sleep(0.5)

    current_pos = pyautogui.position()
    sig_x = current_pos[0] - 100
    sig_y = current_pos[1] + 150

    pyautogui.moveTo(sig_x, sig_y)
    time.sleep(0.3)

    pyautogui.mouseDown()

    # to customized
    moves =[

    ]

    for dx , dy in moves:
        new_x = pyautogui.position()[0] + dx
        new_y = pyautogui.position()[1] + dy
        pyautogui.moveTo(new_x, new_y, duration=0.1)

    pyautogui.mouseUp()
    print("Signature added!")

def clear_canvas():
    print("Clearing canvas...")
    time.sleep(0.3)

    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)

    pyautogui.press('delete')
    time.sleep(0.3)

    print("Canvas Cleared!")

def main():
    print("=" * 50)
    print("USB Mouse Artist")
    print("=" * 50)

    try : 
        time.sleep(5)
        open_paint()

        select_pencil_tool()

        draw_sparkly_heart()

        add_signature()

    except KeyboardInterrupt:
        print("Stopped by user")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()
    

    
    