# bayeosraspberrypi
An implementation for a real BayEOS Gateway Client.

## Installation
You need to install [bayeosgatewayclient](../bayeosgatewayclient) first.

- add the following repositories to /etc/apt/sources.list 
	```deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian wheezy main```
- install key ```wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key | apt-key add -```
- ```apt-get update```
- ```apt-get install python-bayeosgatewayclient```

Furthermore, install the following packages:

- ```apt-get install python-smbus```
- ```apt-get install python-scipy```
- ```apt-get install i2c-tools```
- ```apt-get install libi2c-dev```

No activate I2C Bus:
- add the following line to /etc/modules ```i2c-dev```
- uncomment in /boot/config.txt ```dtparam=i2c_arm=on```
- ```modprobe i2c-bcm2708```
- ```modprobe i2c_dev```


- Install the package by running ```python setup.py install``` as root

## Example
### Inheritance of BayEOSGatewayClient Class
```from bayeosgatewayclient import BayEOSGatewayClient```
Implement the abstract readData() method.


```
class RasperryPi(BayEOSGatewayClient):
    
    def readData(self):
    	pass
```