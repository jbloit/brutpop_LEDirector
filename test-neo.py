## LIBRARIES
import time 
import board 
import neopixel

#GPIO PIN
pixels1 = board.D18 
##COMMENTED OUT pixels2 = board.D15

## Num leds daisychained
num_pixels = 32

## colour information
ORDER = neopixel.GRB

## class with information
pixelswow1  = neopixel.NeoPixel (pixels1, num_pixels, pixel_order=ORDER, brightness = 1)
##COMMENTED OUT pixelswow2 = neopixel.NeoPixel (pixels2, num_pixels, pixel_order=ORDER)

## ranges for seperate rings and their info
for a in range (0,16):
	pixelswow1[a]= (0,255,0)

for b in range (16,32):
	pixelswow1[b] = (255,0,0)

##UTILITY EXAMPLES
## ONE LED TO ADDRESS FROM 1 - 32 pixelswow1[1]= (0,255,0)
##ALL LED ADDRESS pixelswow1.fill ((255,0,0))

