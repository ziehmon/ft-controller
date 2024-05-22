import time
import sshkeyboard
import gpiozero 


z_axis = gpiozero.Motor(22,23)
y_axis = gpiozero.Motor(24,25)
x_axis = gpiozero.Motor(20,21)
g_axis = gpiozero.Motor(12,13)

def press_key(key):
    print(key, "pressed")
    if key == "a":
        x_axis.forward(1)
    if key == "d":
        x_axis.backward(1)
    
    if key == "s":
        y_axis.backward(1)      
    if key == "w":
        y_axis.forward(1)
        
    if key == "f":
        z_axis.backward(1)
    if key == "r":
        z_axis.forward(1)

    if key == "t":
        g_axis.backward(1)
        
    if key == "g":
        g_axis.forward(1)

    if key == "c":      
        z_axis.stop()
        y_axis.stop()
        x_axis.stop()
        g_axis.stop()
        exit()

def release_key(key):
    print(key, "released")

    if key == "a" or key == "d":
        x_axis.stop()
    
    if key == "s" or key == "w":
        y_axis.stop()

    if key == "f" or key == "r":
        z_axis.stop()

    if key == "t" or key == "g":
        g_axis.stop()


sshkeyboard.listen_keyboard(
     on_press=press_key,
     on_release=release_key,
     delay_second_char=0.15,
     delay_other_chars=0.1,
 )
