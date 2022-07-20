import random
from string import ascii_uppercase

from Zjazd_02.smart_home.iot.device import Device
from Zjazd_02.smart_home.iot.devices import hue, curtains


def generate_id(length):
    # generated_id = "".join(random.choices(ascii_uppercase, k=length))
    idea = "SADA"
    return idea


devices = []


class IOTService:
    def __init__(self):
        self.device = None
        self.device_id = None

    def register_device(self, device: Device):
        self.device = device.name
        device.connect
        self.device_id = generate_id(8)
        print(self.device_id)
        devices.append(self.device)

    def unregister_device(self, device_id):
        print(self.device)


iot = IOTService()
iot.register_device(hue)
print(devices)
# iot2 = IOTService()
# iot2.register_device(curtains)
# print(devices)
iot.unregister_device("d")