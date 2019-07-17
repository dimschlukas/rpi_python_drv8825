from stepper import StepperMotor

StepperMotor.__init__(12, 23, 24, (14, 15, 18), '1/32')
StepperMotor.run(200, True)
