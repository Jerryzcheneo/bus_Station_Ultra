bluetooth.onBluetoothConnected(function () {
    start_sending = 1
})
bluetooth.onBluetoothDisconnected(function () {
    start_sending = 0
    basic.showIcon(IconNames.No)
    basic.pause(200)
})
let no_of_person = 0
let start_sending = 0
basic.showString("S")
basic.pause(200)
bluetooth.startUartService()
start_sending = 0
basic.forever(function () {
    no_of_person = 0
    if (sonar.ping(
    DigitalPin.P10,
    DigitalPin.P11,
    PingUnit.Centimeters
    ) < 5) {
        no_of_person += 1
    }
    if (sonar.ping(
    DigitalPin.P9,
    DigitalPin.P8,
    PingUnit.Centimeters
    ) < 5) {
        no_of_person += 1
    }
    if (start_sending == 1) {
        bluetooth.uartWriteNumber(no_of_person)
    }
    basic.showNumber(no_of_person)
    basic.pause(200)
})
