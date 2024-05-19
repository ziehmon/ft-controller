import RPi.GPIO as GPIO

class Motor:

    pwm_freq = 10

    def __init__(self, gpio_l, gpio_r):
        GPIO.setup(gpio_l,GPIO.OUT)
        GPIO.setup(gpio_r,GPIO.OUT)
        GPIO.output(gpio_l,GPIO.LOW)
        GPIO.output(gpio_r,GPIO.LOW)

        self.power_l = GPIO.PWM(gpio_l, self.pwm_freq)
        self.power_r = GPIO.PWM(gpio_r, self.pwm_freq)

        self.power_l.start(0) # PWM init
        self.power_r.start(0) # PWM init

    def left(self, power):
        
        self.power_r.stop(power) # PWM init
        self.power_l.start(power) # PWM init

    def stop(self):

        self.power_l.stop()
        self.power_r.stop()

    def right(self, power):

        self.power_l.stop(power)
        self.power_r.start(power)

def Shutdown():
    GPIO.cleanup()