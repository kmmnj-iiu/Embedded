import RPi.GPIO as GPIO
import time

sw1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

previous_state = 0

try:
    while True:
        sw1Value = GPIO.input(sw1)
        if previous_state == 0 and sw1Value == 1:
            print("스위치가 눌렸습니다!")
        
        previous_state = sw1Value
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
