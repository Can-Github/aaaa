def on_forever():
    sample.set_motor_speed(MotorShaftDirection.CLOCKWISE, 30, 500)
    basic.pause(100)
    sample.set_motor_speed(MotorShaftDirection.COUNTER_CLOCKWISE, 30, 500)
basic.forever(on_forever)
