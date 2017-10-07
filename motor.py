from pynq.overlays.base import BaseOverlay
from time import sleep
from pynq.lib.arduino.arduino_ardumoto import Arduino_Ardumoto
from pynq.lib.arduino.arduino_grove_USranger import Grove_USranger
from pynq.lib.arduino import ARDUINO_GROVE_G1

# Motor stuff
base = BaseOverlay("base.bit")
ardu = Arduino_Ardumoto(base.ARDUINO)
ardu.configure_pins(ardu.defaultpins)
ardu.configure_polarity(ardu.motorA, ardu.pol_default) 
ardu.configure_polarity(ardu.motorB, ardu.pol_reverse) 

# Range finder stuff

USranger = Grove_USranger(base.ARDUINO, ARDUINO_GROVE_G1)

def turn_left (degree):
	ardu.set_speed(ardu.motorA,20)
	ardu.set_speed(ardu.motorB,20)
	ardu.set_dir(ardu.motorA, ardu.forward)
	ardu.set_dir(ardu.motorB, ardu.backward)
	ardu.run(ardu.motorA)
	ardu.run(ardu.motorB)
	for time in range (0, degree):
		sleep (0.5)

	ardu.stop(ardu.motorA)
	ardu.stop(ardu.motorB)

def turn_right (degree):
	ardu.set_speed(ardu.motorA,20)
	ardu.set_speed(ardu.motorB,20)
	ardu.set_dir(ardu.motorA, ardu.backward)
	ardu.set_dir(ardu.motorB, ardu.forward)
	ardu.run(ardu.motorA)
	ardu.run(ardu.motorB)
	for time in range (0, degree):
		sleep (0.5)

	ardu.stop(ardu.motorA)
	ardu.stop(ardu.motorB)

def forward (duration):
	ardu.set_speed(ardu.motorA,20)
	ardu.set_speed(ardu.motorB,20)
	ardu.set_dir(ardu.motorA, ardu.forward)
	ardu.set_dir(ardu.motorB, ardu.forward)
	ardu.run(ardu.motorA)
	ardu.run(ardu.motorB)
	for time in range (0, duration):
		sleep (0.5)

	ardu.stop(ardu.motorA)
	ardu.stop(ardu.motorB)

def backward (duration):
	ardu.set_speed(ardu.motorA,20)
	ardu.set_speed(ardu.motorB,20)
	ardu.set_dir(ardu.motorA, ardu.backward)
	ardu.set_dir(ardu.motorB, ardu.backward)
	ardu.run(ardu.motorA)
	ardu.run(ardu.motorB)
	for time in range (0, duration):
		sleep (0.5)

	ardu.stop(ardu.motorA)
	ardu.stop(ardu.motorB)


while (1):
	distance = USranger.read_distance_inch()
	print ("Distance: " + str(distance) + '"')
	if (distance < 5):
		print ("TOO CLOSE! Backing and turning right")
		backward(1)
		turn_right(1)
	else:
		forward(1)


ardu.stop(ardu.motorA)
ardu.stop(ardu.motorB)
