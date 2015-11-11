"""makeing lights bink in a funcation """
import time 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [6,19,17]
GPIO.setup(pins,GPIO.OUT)
GPIO.output(pins,0)

def on(pin):
    GPIO.output(pin,1)
def off(pin):
    GPIO.output(pin,0)

def blink():
    GPIO.output(pins,1)
    time.sleep(0.5)
    GPIO.output(pins,0)
    time.sleep(0.5)
def up():
    GPIO.output(19,1)
    time.sleep(0.6)
    GPIO.output(6,1)
    time.sleep(0.6)
    GPIO.output(17,1)
    time.sleep(0.6)
    GPIO.output(19,0)
    time.sleep(0.6)
    GPIO.output(6,0)
    time.sleep(0.6)
    GPIO.output(17,0)
    time.sleep(0.6)
def doctor():
    GPIO.output(19,1)
    time.sleep(0.7)
    off(19,0)
    time.



    
if __name__ == "__main__":
    while True:
            doctor()

