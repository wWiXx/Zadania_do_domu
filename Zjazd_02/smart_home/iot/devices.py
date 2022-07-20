from Zjazd_02.smart_home.iot.device import Device
from Zjazd_02.smart_home.iot.message import MessageType

hue = Device("Hue Light")
speaker = Device("Smart Speaker")
curtains = Device("Curtains")

# hue.connect
# hue.disconnect
# hue.send_message(MessageType(1), "data")
# hue.status_update()
