from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

    @property
    @abstractmethod
    def status(self):
        pass

    @property
    def powerUsage(self):
        return self._powerUsage
    
    @powerUsage.setter
    def powerUsage(self,value):
        if not isinstance(value,int) or value<0:
           raise ValueError("Power usage must be a non-negative integer")
        self._powerUsage = value
    
    def __gt__(self,other):
        if not isinstance(other, Device):
            raise TypeError("Comparison must be between two Device instances")
        return self.powerUsage > other.powerUsage
        
class Light(Device):
    def __init__(self,power,brightness,powerUsage):
        self.power = power
        self._brightness = brightness
        super().__init__(powerUsage)

    def turn_on(self):
        self.power = "On"

    def turn_off(self):
        self.power = "Off"
    
    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self,value):
        if value > 10:
            print("Brightness can not be grater than 10")
        elif value < 0:
            print("Brightness cannot be lower than zero")
        else:
            self._brightness = value
        if self.power == "Off":
            self._brightness = 0

    def status(self):
        return(f"Power :{self.power}, Brightness :{self._brightness}")
    
class Thermostat(Device):
    def __init__(self,power,temperature,powerUsage):
        self.power = power
        self._temperature = temperature
        super().__init__(powerUsage)

    def turn_on(self):
        self.power = "On"

    def turn_off(self):
        self.power = "Off"
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self,value):
        if value > 100:
            print("Temperature can not be grater than 100")
        elif value < 0:
            print("Temperature cannot be lower than zero")
        else:
            self._temperature = value
        if self.power == "Off":
            self._temperature = 0

    def status(self):
        return(f"Power :{self.power}, Temperature:{self._temperature}")

class SmartSpeaker(Device):
    def __init__(self,power,volume,powerUsage):
        self.power = power
        self._volume = volume
        super().__init__(powerUsage)
    
    def turn_on(self):
        self.power = "On"

    def turn_off(self):
        self.power = "Off"
    
    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self,value):
        if value > 100:
            print("Volume can not be grater than 100")
        elif value < 0:
            print("Volume cannot be lower than zero")
        else:
            self._volume = value
        if self.power == "Off":
            self._volume = 0

    def status(self):
        return(f"Power :{self.power}, Volume :{self._volume} ")
    
class Room():
    def __init__(self,devices = []):
        self.devices = devices

    def add_device(self,device):
        self.devices.append(device)

    def remove_device(self,device):
        if device in self.devices:
            del device
        else:
            pass

    def total_powerused(self):
        total_power = 0
        for i in self.devices:
            total_power += i.powerUsage
        return total_power
        

class SmartHome():
    def __init__(self,rooms = []):
        self.rooms = rooms

    def total_power_usage(self):
        hometotal_power = 0
        for i in self.rooms:
            hometotal_power += i.total_powerused()


         

    