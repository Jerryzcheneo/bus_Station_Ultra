People = 0

def on_forever():
    global People
    People = 0
    if sonar.ping(DigitalPin.P10, DigitalPin.P11, PingUnit.CENTIMETERS) < 5:
        People += 1
        if sonar.ping(DigitalPin.P9, DigitalPin.P8, PingUnit.CENTIMETERS) < 5:
            People += 1
            basic.show_number(People)
            basic.pause(500)
        else:
            basic.show_number(People)
            basic.pause(500)
    else:
        if sonar.ping(DigitalPin.P9, DigitalPin.P8, PingUnit.CENTIMETERS) < 5:
            People += 1
            basic.show_number(People)
            basic.pause(500)
        else:
            basic.show_number(People)
            basic.pause(500)
basic.forever(on_forever)
