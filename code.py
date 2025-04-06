import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_debouncer import Debouncer


kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
tulitus = digitalio.DigitalInOut(board.GP16)
tulitus.switch_to_input(pull=digitalio.Pull.DOWN)
switch = Debouncer(tulitus)

oikea = digitalio.DigitalInOut(board.GP17)
oikea.switch_to_input(pull=digitalio.Pull.DOWN)
oikealle = Debouncer(oikea)

vasen = digitalio.DigitalInOut(board.GP18)
vasen.switch_to_input(pull=digitalio.Pull.DOWN)
vasemmalle = Debouncer(vasen)

ylos = digitalio.DigitalInOut(board.GP19)
ylos.switch_to_input(pull=digitalio.Pull.DOWN)
UP = Debouncer(ylos)

alas = digitalio.DigitalInOut(board.GP20)
alas.switch_to_input(pull=digitalio.Pull.DOWN)
DOWN = Debouncer(alas)



while True:
    
    switch.update()
    if switch.rose:
        kbd.send(Keycode.F1)
        
    oikealle.update()
    if oikealle.rose:
        kbd.send(Keycode.RIGHT_ARROW)
    if oikealle.value:
        kbd.send(Keycode.RIGHT_ARROW)
        
    vasemmalle.update()
    if vasemmalle.rose:
        kbd.send(Keycode.LEFT_ARROW)
    if vasemmalle.value:
        kbd.send(Keycode.LEFT_ARROW)


    UP.update()
    if UP.rose:
        kbd.send(Keycode.UP_ARROW)
    if UP.value:
        kbd.send(Keycode.UP_ARROW)


    DOWN.update()
    if DOWN.rose:
        kbd.send(Keycode.DOWN_ARROW)
    if DOWN.value:
        kbd.send(Keycode.DOWN_ARROW)


        
