import ConfigParser
from bayeosgatewayclient import BayEOSGatewayClient, bayeos_confparser
from random import randint
from time import sleep
import os
from gpio import GPIO
from i2c import I2C
from sht21 import SHT21
from mcp3424 import MCP3424
import numpy  # apt-get install python-numpy
from scipy import stats  # apt-get install python-scipy

class RaspberryPiClient(BayEOSGatewayClient):
    """Raspberry Pi client class."""

    def init_writer(self):
        # gpio pins
        ADDR_PINS = [11, 12, 13, 15, 16, 18]  # GPIO 17, 18, 27, 22, 23, 24
        DATA_PIN = 24  # GPIO 8
        EN_PIN = 26  # GPIO 7
        self.gpio = GPIO(ADDR_PINS, EN_PIN, DATA_PIN)

        self.init_sensors()
        self.addr = 1  # current address

    def read_data(self):
        # address 0 is reserved for flushing with air
        self.gpio.set_addr(0)  # set flushing address
        sleep(0.6)  # flush for 60 seconds
        self.gpio.reset()  # stop flushing

        self.gpio.set_addr(self.addr)  # start measuring wait 60 seconds, 240 measure
        measure = self.measure(3)
        self.gpio.reset()

        return measure

    def save_data(self, values=[], origin='CO2_Chambers'):
        self.writer.save(values, origin="RaspberryPi Kammer Nr. " + str(self.addr))
        self.writer.flush()
        print 'save data ' + str(values)
        
        self.addr += 1
        if self.addr > 15:
            self.addr = 1

    def init_sensors(self):
        try:
            self.i2c = I2C()
            self.sht21 = SHT21(1)
            self.mcp3424 = MCP3424(self.i2c.get_smbus())
        except IOError, e:
            print "I2C Connection Error :" + str(e) + ". This must be run as root. Did you use the right device number?"

    def measure(self, seconds=10):
        measured_seconds = []
        temp = []
        hum = []
        co2 = []
        for i in range(0, seconds):
            temp.append(self.sht21.read_temperature())
            hum.append(self.sht21.read_humidity())
            co2.append(self.mcp3424.read_voltage(1))
            measured_seconds.append(i)
            sleep(1)
        mean_temp = numpy.mean(temp)
        var_temp = numpy.var(temp)
        mean_hum = numpy.mean(hum)
        var_hum = numpy.var(hum)
        slope, intercept, r_value, p_value, std_err = stats.linregress(measured_seconds, co2)
#         print "Mean temp.: " + str(mean_temp) + " Variance: " + str(var_temp)
#         print "Mean humidity: " + str(mean_hum) + " Variance: " + str(var_hum)
#         print "Slope: " + str(slope)
        return [mean_temp, var_temp, mean_hum, var_hum, slope, intercept]

OPTIONS = bayeos_confparser('../config/bayeosraspberrypi.ini')

client = RaspberryPiClient(OPTIONS['name'], OPTIONS)
client.run()

# try:
#     client.run()
# except KeyboardInterrupt as err:
#     print str(err) + ' Stopped measurement loop.'
# finally:
#     client.writer.gpio.cleanup()
