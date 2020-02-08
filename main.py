# WS2812-Matrix
# Created at 2020-02-08 21:16:40.780285



import streams
import LedMatrix

streams.serial()

led_pin = D8                      # this should match the data pin of the LED strip
switch_pin = D2                   # this should match the pin to which the button is connected

rows = 10
cols = 10
        
matrix = LedMatrix.Matrix(led_pin, rows, cols)
matrix.clear()
matrix.on()
sleep(500)
matrix.setall(0,0,200)
matrix.on()
sleep(500)
matrix.set(1,6,(200,0,0))
matrix.brightness(0.4)
matrix.on()

while True:
   matrix.lshift()
   matrix.on()
   sleep(100)