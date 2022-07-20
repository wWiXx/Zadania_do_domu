from dataclasses import dataclass

from Zjazd_02.smart_home.iot.message import MessageType


@dataclass
class Device:
    name: str

    @property
    def connect(self):
        print(f"Connecting {self.name}")
        return None

    @property
    def disconnect(self):
        print(f"Disconnecting {self.name}")
        return None

    def send_message(self, message_type: MessageType, data: str):
        print(f"{self.name} handling message of type {message_type.name} with data [{data}].")

    def status_update(self):
        lower_name = self.name.lower().replace(" ", "_")
        print(f"{lower_name}_status_ok")
