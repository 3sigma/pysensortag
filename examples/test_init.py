#!/usr/bin/python
# -*- coding: utf-8 -*-

# Requirement: you must have pygatt installed:
# git clone https://github.com/3sigma/pygatt.git
# cd pygatt
# sudo python setup.py install
# cd ..
import pygatt.backends

import pysensortag

# Start the BLED112 (BLE Adapter from BlueGiga)
adapter = pygatt.backends.BGAPIBackend()
adapter.start()

# Connect to SensorTag (put the address of *your* SensorTag below) 
sensortag = pysensortag.PySensorTag(adapter, 'B0:B4:48:C0:5D:00')

# Stop the BLED112
adapter.stop()


