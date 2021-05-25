basic.forever(function () {
    sample.setMotorSpeed(MotorShaftDirection.Clockwise, 30, 500)
    basic.pause(100)
    sample.setMotorSpeed(MotorShaftDirection.CounterClockwise, 30, 500)
})