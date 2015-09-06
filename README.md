# bayeosraspberrypi
An implementation for a real BayEOS Gateway Client.

## Installation
First, you need to install the [bayeosgatewayclient](https://github.com/kleebaum/bayeosgatewayclient):
- add the following repositories to /etc/apt/sources.list 
	```deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian wheezy main```
- install key ```wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key | apt-key add -```
- ```apt-get update```
- ```apt-get install python-bayeosgatewayclient```

Next, install the following packages:
- ```apt-get install python-smbus```
- ```apt-get install python-scipy```
- ```apt-get install i2c-tools```
- ```apt-get install libi2c-dev```

Now activate I2C bus:
- add the following line to /etc/modules ```i2c-dev```
- uncomment in /boot/config.txt ```dtparam=i2c_arm=on```
- ```modprobe i2c-bcm2708```
- ```modprobe i2c_dev```

Install the bayeosraspberrypi package:
- git clone request ```git clone git://github.com/kleebaum/bayeosraspberrypi.git```
- find the right directory ```cd bayeosraspberryp```
- run ```python setup.py install``` as root

## Usage

### Beginners
The script [bayeosraspberrypi.py](https://github.com/kleebaum/bayeosraspberrypi/blob/master/bayeosraspberrypi/bayeosraspberrypi.py) shows how 
to use the BayEOSWriter and BayEOSSender classes.

### Advanced
The script [bayeosraspberrypiclient.py](https://github.com/kleebaum/bayeosraspberrypi/blob/master/bayeosraspberrypi/bayeosraspberrypiclient.py) shows how 
to extend the BayEOSGatewayClient class.

For your own scripts:
Import the RaspberryPiClient class: ```from bayeosraspberrypi import RaspberryPiClient```.

Define options within the script:
```
PATH = '/tmp/raspberrypi/'
NAME = 'RaspberryPi'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'
```

Or read a config file using the ```bayeos_configparser(config_file)``` method:
```
OPTIONS = bayeos_confparser('../config/bayeosraspberrypi.ini')
```

Create an object and invoke the ```run()``` method:
```
client = RaspberryPiClient(OPTIONS['name'], OPTIONS)
client.run(thread=False) # sender runs in a separate process 
```