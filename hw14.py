import RPi.GPIO as GPIO
import time

sw_pins = [5, 6, 13, 19]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in sw_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_values = [GPIO.input(pin) for pin in sw_pins]
click_counts = [0] * len(sw_pins)

try:
    while True:
        for i, pin in enumerate(sw_pins):
            sw_value = GPIO.input(pin)
            if prev_values[i] == 0 and sw_value == 1:
                click_counts[i] += 1
                print('sw{} click'.format(i + 1), click_counts[i])
            prev_values[i] = sw_value
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
