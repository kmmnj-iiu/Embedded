import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261)
p.start(50)

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

try:
    for note, duration in melody:
        frequency = scale[note]
        p.ChangeFrequency(frequency)
        time.sleep(duration)
    p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
