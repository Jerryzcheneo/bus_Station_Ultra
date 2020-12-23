let People = 0
basic.forever(function () {
    People = 0
    if (sonar.ping(
    DigitalPin.P10,
    DigitalPin.P11,
    PingUnit.Centimeters
    ) < 5) {
        People += 1
        if (sonar.ping(
        DigitalPin.P9,
        DigitalPin.P8,
        PingUnit.Centimeters
        ) < 5) {
            People += 1
            basic.showNumber(People)
            basic.pause(500)
        } else {
            basic.showNumber(People)
            basic.pause(500)
        }
    } else if (sonar.ping(
    DigitalPin.P9,
    DigitalPin.P8,
    PingUnit.Centimeters
    ) < 5) {
        People += 1
        basic.showNumber(People)
        basic.pause(500)
    } else {
        basic.showNumber(People)
        basic.pause(500)
    }
})
