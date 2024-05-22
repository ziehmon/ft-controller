button_pins = [5, 6, 16, 17, 18, 19, 26, 27]
buttons = [gpiozero.Button(pin) for pin in button_pins]

while(True):
    for button in buttons:
        print("Button {} is pressed: {}".format(button_pins[buttons.index(button)], button.is_pressed))
    time.sleep(0.5)
    print("\n\n")
