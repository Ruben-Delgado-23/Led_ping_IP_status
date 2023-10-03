#Importing Libraries

from ping3 import ping, verbose_ping
import time
import RPi.GPIO as GPIO

GPIO_RED_LIGHT = 21        # Led for Ip status not responding
GPIO_GREEN_LIGHT = 20      # Led for Ip status responding

# setup the GPIO pins

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(GPIO_RED_LIGHT, GPIO.OUT)
GPIO.setup(GPIO_GREEN_LIGHT, GPIO.OUT)

# main loop: ping IP, turn on appropriate Led, repet

while True:
# IP address to be monitored
  ping("150.1.7.32", )
  verbose_ping("150.1.7.32", count=1)

  if ping("150.1.7.32") == None:
    GPIO.output(GPIO_RED_LIGHT, GPIO.HIGH)  # Turn on red LED
    GPIO.output(GPIO_GREEN_LIGHT, GPIO.LOW)  # Turn off green LED
    time.sleep(1)   # Check IP status every 1 second
    print ("network issue")

  else:
    GPIO.output(GPIO_RED_LIGHT, False)  # Turn off red LED
    GPIO.output(GPIO_GREEN_LIGHT, True) # Turn on green LED
    time.sleep(1) # Check IP status every 1 second
    print ("network ok")

# Clean up GPIO's
    GPIO.cleanup()
