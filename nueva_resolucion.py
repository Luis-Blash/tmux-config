from pyautogui import write, press, hotkey, alert

def main():
    write('xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync')
    press('enter')
    write("xrandr --addmode DP-2 1920x1080_60.00")
    press('enter')
    write("xrandr --output DP-2 --mode 1920x1080_60.00")
    press('enter')

if __name__ == '__main__':
    main()