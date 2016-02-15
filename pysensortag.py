

class PySensorTag(object): 

    def __init__(self, adapter):
        self.device = adapter.connect('B0:B4:48:C0:5D:00')
        
        print "Connexion au SensorTag"
        
        print "Nom du device: "
        value = self.device.handle_read(3)
        print bytearray(value)
        
        print "RSSI: "
        print self.device.get_rssi()
        
        print "Firmware revision string: "
        value = self.device.handle_read(20)
        print bytearray(value)
        
        self.test = "toto"
       
       
    def GetTest(self):
        print self.test
        
        
    def ActivateTemperatureSensor(self):
        self.device.char_write_handle(36, [0x01])


    def DeactivateTemperatureSensor(self):
        self.device.char_write_handle(36, [0x00])


    def GetTemperature(self):
        value = self.device.handle_read(33)

        rawVobj = (value[1]<<8) + value[0]
        rawTamb = (value[3]<<8) + value[2]
        
        ambientTemp = float(rawTamb * 0.25 * 0.03125)
        objectTemp = float(rawVobj * 0.25 * 0.03125)
        
        return (ambientTemp, objectTemp)


    def ActivateHumiditySensor(self):
        self.device.char_write_handle(44, [0x01])


    def DeactivateHumiditySensor(self):
        self.device.char_write_handle(44, [0x00])


    def GetHumidity(self):
        value = self.device.handle_read(41)

        rawHtemp = (value[1]<<8) + value[0]
        rawHum = (value[3]<<8) + value[2]
        
        HTemp = float(rawHtemp / 65536.0 * 165 - 40)
        Humidity = float(rawHum / 65536.0 * 100)
        
        return (HTemp, Humidity)


    def ActivateBarometerSensor(self):
        self.device.char_write_handle(52, [0x01])


    def DeactivateBarometerSensor(self):
        self.device.char_write_handle(52, [0x00])


    def GetBarometer(self):
        value = self.device.handle_read(49)
        
        rawBTemp = (value[2]<<16) + (value[1]<<8) + value[0]
        rawPressure = (value[5]<<16) + (value[4]<<8) + value[3]
        
        BTemp = float(rawBTemp / 100)
        Pressure = float(rawPressure / 100)
        
        return (BTemp, Pressure)


    def ActivateMovementSensor(self):
        sensorOnVal = 0x7F02
        self.device.char_write_handle(60, [(sensorOnVal >> 8) & 0xFF, sensorOnVal & 0xFF])


    def DeactivateMovementSensor(self):
        sensorOffVal = 0x0000
        self.device.char_write_handle(60, [(sensorOffVal >> 8) & 0xFF, sensorOffVal & 0xFF])


    def GetMovement(self):
        value = self.device.handle_read(57)
        
        scaleAcc = 4096.0
        Ax = self._TwoBytesToSignedFloat(value[7], value[6]) / scaleAcc
        Ay = self._TwoBytesToSignedFloat(value[9], value[8]) / scaleAcc
        Az = self._TwoBytesToSignedFloat(value[11], value[10]) / scaleAcc
        
        scaleGyro = 128.0
        Wx = self._TwoBytesToSignedFloat(value[1], value[0]) / scaleGyro
        Wy = self._TwoBytesToSignedFloat(value[3], value[2]) / scaleGyro
        Wz = self._TwoBytesToSignedFloat(value[5], value[4]) / scaleGyro
        
        scaleMag = (32768.0 / 4912.0)
        Mx = self._TwoBytesToSignedFloat(value[13], value[12]) / scaleMag
        My = self._TwoBytesToSignedFloat(value[15], value[14]) / scaleMag
        Mz = self._TwoBytesToSignedFloat(value[17], value[16]) / scaleMag
        
        return (Ax, Ay, Az, Wx, Wy, Wz, Mx, My, Mz)


    def ActivateLuxometerSensor(self):
        self.device.char_write_handle(68, [0x01])


    def DeactivateLuxometerSensor(self):
        self.device.char_write_handle(68, [0x00])


    def GetLuxometer(self):
        value = self.device.handle_read(65)
        
        rawLux = (value[1]<<8) + value[0]
        
        m = rawLux & 0x0FFF;
        e = (rawLux >> 12) & 0xFF;
        Lux = m * (0.01 * pow(2.0, e))
        
        return Lux


    def _TwoBytesToSignedFloat(self, MSByte, LSByte):
        SixteenBits = (MSByte << 8) + LSByte
        if SixteenBits > 32768:
            return (65536 - SixteenBits) * (-1)
        else:
            return SixteenBits



