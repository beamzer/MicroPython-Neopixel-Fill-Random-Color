import uos
import ustruct
import neopixel
import machine
import time

bright = 45
nrleds = 24
speed = 50
speed = 1/speed
wait = 1

# initialise, with "nrleds" neopixel LEDs connected to D4
np = neopixel.NeoPixel(machine.Pin(4), nrleds)

def randint(maxval):
	a = uos.urandom(1)		# this returns a byte with random value
	d = ustruct.unpack('i',a)	# convert to int
	R = int( (d[0]/255) * maxval )	# scale 
	return R


### enter endless loop
while True:
	# Assign the current LED a random red, green and blue value between 0 and "bright"
	red   = randint(bright)
	green = randint(bright)
	blue  = randint(bright)
	for pixel_id in range(nrleds):		# Iterate over each LED [0..23] in the strip
		np[pixel_id] = (red, green, blue)
		np.write()			# Display the current pixel data on the Neopixel strip
		time.sleep(speed)

	time.sleep(wait)			# Sleep for "wait" seconds

	for pixel_id in range(nrleds):
		np[pixel_id] = (0,0,0)		# or use -pixel_id to clear the other way round
		np.write()
		time.sleep(speed)

	time.sleep(wait)
