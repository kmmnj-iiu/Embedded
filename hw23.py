import RPi.GPIO as GPIO
import time

BUZZER = 12
sw1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_value = GPIO.input(sw1)
p = GPIO.PWM(BUZZER, 261)

scale = {
    'C': 261,
    'D': 294,
    'E': 329,
    'F': 349,
    'G': 392,
    'A': 440,
}

melody = [
    ('E', 0.3), ('E', 0.3), ('E', 0.3), ('D', 0.3), ('C', 0.5), ('C', 0.7),
    ('E', 0.3), ('E', 0.3), ('E', 0.3), ('D', 0.3), ('C', 0.5), ('C', 0.7),
    ('F', 0.2), ('F', 0.2), ('F', 0.2), ('F', 0.2), ('E', 0.2), ('D', 0.5), ('D', 0.7),
    ('F', 0.3), ('F', 0.3), ('F', 0.3), ('E', 0.3), ('D', 0.5), ('D', 0.7)
]

def honk():
    p.start(50)
    for note, duration in melody:
        frequency = scale[note]
        p.ChangeFrequency(frequency)
        time.sleep(duration)
    p.stop()

try:
    while True:
        sw1Value = GPIO.input(sw1)
        if prev_value == 0 and sw1Value == 1:
            honk()
            time.sleep(0.5)
        prev_value = sw1Value
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
