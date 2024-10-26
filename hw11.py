import RPi.GPIO as GPIO
import time

sw1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_value = GPIO.input(sw1)

try:
    while True:
        sw1Value = GPIO.input(sw1)
        if prev_value == 0 and sw1Value == 1:
            print("click")
        prev_value = sw1Value
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
