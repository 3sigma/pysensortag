#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Requirement: you must have pygatt installed:
# git clone https://github.com/3sigma/pygatt.git
# cd pygatt
# sudo python setup.py install
# cd ..
import pygatt.backends

import pysensortag
from time import sleep

# D�marrage du BLED112
adapter = pygatt.backends.BGAPIBackend()
adapter.start()

# Connexion au SensorTag
sensortag = pysensortag.PySensorTag(adapter, 'B0:B4:48:C0:5D:00')

print("Activation du capteur de temperature")
sensortag.ActivateTemperatureSensor()

print("Activation du luxometre\n")
sensortag.ActivateLuxometerSensor()

# D�lai laissant le temps aux activations de se r�aliser
sleep(1)

# Lecture et affichage des temp�ratures
temperatures = sensortag.GetTemperature()
ambientTemp = temperatures[0]
objectTemp = temperatures[1]
print("Ambient Temp: %.2f C" % ambientTemp)
print("Object Temp: %.2f C\n" % objectTemp)

# Lecture et affichage de la luminosit�
Lux = sensortag.GetLuxometer()
print("Light intensity: %.2f lx" % Lux)

# Arr�t du BLED112
adapter.stop()
