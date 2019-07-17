from stepper import StepperMotor
from time import sleep

motor = StepperMotor(12, 23, 24, (14, 15, 18), '1/32')
motor.run(6400, True)
sleep(0.5)
motor.run(6400, False)
