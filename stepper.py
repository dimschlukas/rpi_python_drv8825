import RPi.GPIO as GPIO
from time import sleep

class StepperMotor:
    def __init__(self, enable_pin, step_pin, dir_pin, mode_pins, step_type):
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(enable_pin, self.GPIO.OUT)
        self.GPIO.setup(step_pin, self.GPIO.OUT)
        self.GPIO.setup(dir_pin, self.GPIO.OUT)
        self.GPIO.setup(mode_pins, self.GPIO.OUT)
        resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
        microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        delay = .005/microsteps[step_type]
        self.GPIO.output(mode_pins, resolution[step_type])


    def run(self, steps, clockwise)
        self.GPIO.output(self.enable_pin, self.GPIO.LOW)
        self.GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            self.GPIO.output(self.step_pin, self.GPIO.HIGH)
            self.sleep(self.delay)
            self.GPIO.output(self.step_pin, self.GPIO.LOW)
            self.sleep(self.delay)
        self.GPIO.output(self.enable_pin, self.GPIO.HIGH)
