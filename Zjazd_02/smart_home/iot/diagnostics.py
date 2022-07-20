from Zjazd_02.smart_home.iot.device import Device
from Zjazd_02.smart_home.iot.devices import hue


def collect_diagnostics(device: Device):
    print("Connecting to diagnostics server.")
    device.status_update()
    print(f"Sending status update <status_ok> to server.")


collect_diagnostics(hue)
