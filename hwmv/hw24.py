import RPi.GPIO as GPIO
import time

BUZZER = 12
sw_pins = [5, 6, 13, 19]
notes = [261, 329, 392, 440]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for pin in sw_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_values = [GPIO.input(pin) for pin in sw_pins]
p = GPIO.PWM(BUZZER, 261)

def play_tone(frequency):
    p.start(50)
    p.ChangeFrequency(frequency)
    time.sleep(0.2)
    p.stop()

try:
    while True:
        for i, pin in enumerate(sw_pins):
            sw_value = GPIO.input(pin)
            if prev_values[i] == 0 and sw_value == 1:
                play_tone(notes[i])
                time.sleep(0.1)
            prev_values[i] = sw_value
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
