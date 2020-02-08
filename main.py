# WS2812-Matrix
# Created at 2020-02-08 21:16:40.780285



import streams
import ws2812_matrix

streams.serial()

led_pin = D8                      # this should match the data pin of the LED strip

rows = 10
cols = 10
        
matrix = ws2812_matrix.matrix(led_pin, rows, cols, True)
matrix.brightness(0.4)
matrix.on()

flag = False
while True:
    
    if flag:
        color =(0,220,0)
        flag = False
    else:
        color =(225,0,0)
        flag = True
        
    for i in range(cols):
        for j in range(rows):
            matrix.set(j,i,color)
   
            matrix.on()
            sleep(20)
    