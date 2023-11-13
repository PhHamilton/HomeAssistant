import hassapi as hass
from datetime import time

#
# Hello World App
#
# Args:
#


class ToggleWindowLights(hass.Hass):
    def initialize(self):
        self.log("Initializing ToggleWindowLights")
    
    def TurnLightsOn(self): 
        self.log("Turning on window lights")

    def TurnLightsOff(self): 
        self.log("Turning off window lights")
