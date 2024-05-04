class Button:
    def __init__(self, pin: int) -> None:
        self.pin = pin

class LED:
    def __init__(self, pin: int, is_rgb: bool=False) -> None:
        self.pin = pin
        self.rgb = is_rgb

        self.led = Pin(self.pin)
    
    def on(self):
        pass
