import time
import sshkeyboard

from ftpython import ftpython

z_axis = ftpython.Motor(22,23)
y_axis = ftpython.Motor(24,25)
x_axis = ftpython.Motor(20,21)
g_axis = ftpython.Motor(12,13)

def press(key):
    if key == "a":
        x_axis.left(65)
    if key == "d":
        x_axis.right(65)
    
    if key == "s":
        y_axis.right(100)
    if key == "w":
        y_axis.left(100)

    if key == "f":
        z_axis.right(100)
    if key == "r":
        z_axis.left(100)

    if key == "t":
        g_axis.right(100)
    if key == "g":
        g_axis.left(100)

    if key == "c":
        
        z_axis.stop()
        y_axis.stop()
        x_axis.stop()
        g_axis.stop()
        ftpython.Shutdown()
        exit()

def release(key):
    print("Stopping for: ", key)
    if key == "a" or key == "d":
        x_axis.stop()
    
    if key == "s" or key == "w":
        y_axis.stop()

    if key == "f" or key == "r":
        z_axis.stop()

    if key == "t" or key == "g":
        g_axis.stop()


sshkeyboard.listen_keyboard(
    on_press=press,
    on_release=release,
    delay_second_char=0.1,
    delay_other_chars=0.1,
)