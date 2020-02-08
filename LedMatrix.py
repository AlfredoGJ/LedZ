from worldsemi.ws2812 import ledstrips as pixel

class Matrix:
    def __init__(self, led_pin, num_rows,num_cols):
        self.leds=pixel.LedStrip(led_pin,num_rows*num_cols)
        self.num_cols=num_cols
        self.num_rows= num_rows
        
    def on(self):
        self.leds.on()
        
    def clear(self):
        self.leds.clear()
        
    def get(self, row, col):
        if(row %2==0):
            return self.leds[row*self.num_cols+col]
        else:
            return self.leds[row*self.num_cols+self.num_cols-1-col]
            
    def set(self, row, col, color):
        if(row %2==0):
            self.leds[row*self.num_cols+col]=color
        else:
            self.leds[row*self.num_cols+self.num_cols-1-col]=color
        
    def lshift(self):
        self.leds.lshift()
        
    def sshift(self):
        self.leds.rshift()
        
    def setall(self, r,g,b):
        self.leds.setall(r,g,b)
        
    def brightness(self,bright):
        self.leds.brightness(bright)
        
    def merge(self,leds,func):
        self.leds.merge(leds,func)