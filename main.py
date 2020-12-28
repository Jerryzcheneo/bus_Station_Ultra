def on_bluetooth_connected():
    global start_sending
    start_sending = 1
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global start_sending
    start_sending = 0
    basic.show_icon(IconNames.NO)
    basic.pause(200)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

no_of_person = 0
start_sending = 0
basic.show_string("S")
basic.pause(200)
bluetooth.start_uart_service()
start_sending = 0

def on_forever():
    global no_of_person
    People = 0
    no_of_person = 0
    if sonar.ping(DigitalPin.P10, DigitalPin.P11, PingUnit.CENTIMETERS) < 5:
        no_of_person += 1
    if sonar.ping(DigitalPin.P9, DigitalPin.P8, PingUnit.CENTIMETERS) < 5:
        no_of_person += 1
    if start_sending == 1:
        bluetooth.uart_write_number(no_of_person)
    basic.show_number(People)
    basic.pause(200)
basic.forever(on_forever)
