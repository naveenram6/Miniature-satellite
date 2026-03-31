import machine
import utime
from chittiSat.sdcard import *
import uos
import time
from chittiSat.pressure import *
from chittiSat.assistant import *
from chittiSat.mq2 import MQ2
from chittiSat.gyro import MPU6050
led = machine.Pin(25,machine.Pin.OUT)
sensor = MQ2(pinData = 26)

sensor.calibrate()

i2c = machine.I2C(0, scl = machine.Pin(1), sda = machine.Pin(0))
dev = i2c.scan()
mpu6050 = MPU6050(i2c)
bmp280  = BMP280(i2c)
calibrate.pressure(bmp280)
spi = machine.SPI(1, sck = machine.Pin(14), mosi= machine.Pin(15),miso= machine.Pin(12))

sd = SDCard(spi)
uos.mount(sd,'/sd') 
print("sd card detected")
print(uos.listdir('/sd'))

myfile = card.newFile(uos.listdir('/sd'))
with open(myfile,"w") as f:
    f.write("Time")
    f.write(",")
    f.write("Pressure")
    f.write(",")
    f.write("Temperature")
    f.write(",")
    f.write("Smoke")
    f.write(",")
    f.write("LPG")
    f.write(",")
    f.write("Methane")
    f.write(",")
    f.write("Hydrogen")
    f.write(",")
    f.write("ax")
    f.write(",")
    f.write("ay")
    f.write(",")
    f.write("az")
    f.write(",")
    f.write("gx")
    f.write(",")
    f.write("gy")
    f.write(",")
    f.write("gz")
    f.write("\n")#next line
    while True:
        t = time.ticks_ms()/1000 # 1 sec = 1000 ms  
        
        pressure = bmp280.pressure
        temperature = bmp280.temperature
        
        Smoke = sensor.readSmoke()
        LPG = sensor.readLPG()
        Methane = sensor.readMethane()
        Hydrogen = sensor.readHydrogen()
        gx=round(mpu6050.gyro.x,2)
        gy=round(mpu6050.gyro.y,2)
        gz=round(mpu6050.gyro.z,2)
        ax=round(mpu6050.accel.x,2)
        ay=round(mpu6050.accel.y,2)
        az=round(mpu6050.accel.z,2)
        
        f.write(str(t))
        f.write(",")
        f.write(str(pressure))
        f.write(",")
        f.write(str(temperature))
        f.write(",")
        f.write(str(Smoke))
        f.write(",")
        f.write(str(LPG))
        f.write(",")
        f.write(str(Methane))
        f.write(",")
        f.write(str(Hydrogen))
        f.write(",")
        f.write(str(ax))
        f.write(",")
        f.write(str(ay))
        f.write(",")
        f.write(str(az))
        f.write(",")
        f.write(str(gx))
        f.write(",")
        f.write(str(gy))
        f.write(",")
        f.write(str(gz))
        f.write("\n")
        f.flush()
        led.toggle()
        utime.sleep(1)

        
