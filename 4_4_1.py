import threading
import serial
import time
import RPi.GPIO as GPIO

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = ""

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 24
BIN2 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline()
        data = data.decode()
        gData = data

def go():
    print("Moving Forward")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(100)

def back():
    print("Moving Backward")
    GPIO.output(AIN1, 1)
    GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)

def left():
    print("Turning Left")
    GPIO.output(BIN1, 1)
    GPIO.output(BIN2, 0)
    R_Motor.ChangeDutyCycle(100)
    GPIO.output(AIN1, 1)
    GPIO.output(AIN2, 0)
    L_Motor.ChangeDutyCycle(100)

def right():
    print("Turning Right")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(100)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(100)

def stop():
    print("Stopping")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 0)
    L_Motor.ChangeDutyCycle(0)
    R_Motor.ChangeDutyCycle(0)

def main():
    global gData
    try:
        while True:
            if gData.find("B0") >=  0:
                gData = ""
                print("ok go")
                go()
            elif gData.find("B2") >= 0:
                gData = ""
                print("ok back")
                back()
            elif gData.find("B1") >= 0:
                gData = ""
                print("ok left")
                left()
            elif gData.find("B3") >= 0:
                gData = ""
                print("ok right")
                right()
            elif gData.find("B4") >= 0:
                gData = ""
                print("ok stop")
                stop()

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass
    finally:
        L_Motor.stop()
        R_Motor.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    task1 = threading.Thread(target=serial_thread)
    task1.start()
    main()
    bleSerial.close()
