from machine import Pin, PWM

class PwmLight:

    FULL_DUTY = 65535

    def __init__(self, pin, on=False, brightness=100):
        self.pwmled = PWM(Pin(pin))
        self.pwmled.freq(1000)
        self.is_on = on
        self.brightness = brightness
        self._update()

    def _update(self):
        print(f"Setting led state to: {self.is_on}, brightness to: {self.brightness}")
        duty = int((self.FULL_DUTY / 100)) * self.brightness if self.is_on else 0
        self.pwmled.duty_u16(duty)

    def turn_on(self):
        self.is_on = True
        self._update()

    def turn_off(self):
        self.is_on = False
        self._update()

    def set_on(self, on):
        self.is_on = on
        self._update()

    def set_brightness(self, value):
        self.brightness = max(min(value, 100), 0)
        self._update()

    def get_state(self):
        return {"on": self.is_on, "brightness": self.brightness}

