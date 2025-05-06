from bm_serial import BristlemouthSerial
from MS5803 import MS5803
import board
import digitalio
import time
import busio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
bm = BristlemouthSerial()
last_send = time.time()

# Pins are configured for the Adalogger RP2040 and other Feather boards
i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

while True:
    now = time.time()
    if now - last_send > 30:
        led.value = True
        last_send = now

        ms = MS5803(i2c)

        print(ms.get_measurements())

        # return temperature in Celsius and pressure in mbar
        temp, pressure = ms.get_measurements(temp_units='celsius', pressure_units='mbar')

        # print temperature and pressure readings to serial monitor
        print(f"Temperature: {temp:.2f} C, Pressure: {pressure:.2f} mbar")

        bm.spotter_tx(f"Temperature: {temp:.2f} C, Pressure: {pressure:.2f} mbar")
        bm.spotter_log(
            "any_file_name.log",
            f"Temperature: {temp:.2f} C, Pressure: {pressure:.2f} mbar",
        )
        led.value = False
