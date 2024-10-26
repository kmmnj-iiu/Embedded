import RPi.GPIO as GPIO
import time

BUZZER = 12

scale = [261, 294, 330, 349, 392, 440, 494, 523]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261)

p.start(50)

try:
    for freq in scale:
        p.ChangeFrequency(freq)
        time.sleep(0.5)
    p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
