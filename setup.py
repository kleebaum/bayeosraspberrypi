"""bayeosraspberrypi setup"""

try:
    from setuptools import setup
except ImportError as ierr:
    print 'Import error :' + str(ierr)
    from distutils.core import setup

setup(
    name='bayeosraspberrypi',
    version='0.0.3',
    packages=['bayeosraspberrypi'],
    install_requires=['bayeosgatewayclient', 'smbus'],
    data_files=[('config',['config/bayeosraspberrypi.ini'])],
    description='An implementation for a real BayEOS Gateway Client.',
    author='Anja Kleebaum',
    author_email='Anja.Kleebaum@stmail.uni-bayreuth.de',
    license='GPL2',
    keywords='bayeos gateway client raspberry pi',
    classifiers=['Programming Language :: Python'])
