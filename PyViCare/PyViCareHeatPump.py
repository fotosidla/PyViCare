import re
import json
import os
import logging
from PyViCare.PyViCareDevice import Device

class HeatPump(Device):
    def getCompressorActive(self):
        try:
            return self.service.getProperty("heating.compressor")["properties"]["active"]["value"]
        except KeyError:
            return "error"
            
    def getReturnTemperature(self):
        try:
            return self.service.getProperty("heating.sensors.temperature.return")["properties"]["value"]["value"]
        except KeyError:
            return "error"