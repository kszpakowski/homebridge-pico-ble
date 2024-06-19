# BLE Light

A Raspberry PI Pico W as a smart light driver using BLE and homebridge

## Why BLE?

1. No need for setting up wifi connection!

## How it works?

RPI runs a BLE GATT server allowing reading and setting light state.

### Service

UUID cad6e164de14425f8d19f241b592a385

### Characteristics

|name|uuid|desc|struct format|
|-|-|-|-|
|on|d00b8ba4d8ce42ff92f2b0d193c58da4|0 - off, 1 - on|little-endian char `<b`|
|set_on|19380250824b46c797a979761b8a27a7||little-endian char `<b`|
|brightness|127cf8c9b7fe47e3b2e03901b7988b00|brightness level from 0 to 100 |little-endian char `<b`|
|set_brightness|66286dbfe5e946d4b300a0ec456f677c||little-endian char `<b`|

> TODO describe more details

## References

### BLE

- [Adafruit Introduction to Bluetooth Low Energy](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt)
- [Bluetooth Assigned Numbers Specification](https://www.bluetooth.com/specifications/assigned-numbers/)

### Pico

- [High level, object oriented, asyncio based Micropython BLE module](https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble)
- [Low level BLE Micropython module](https://docs.micropython.org/en/latest/library/bluetooth.html)
- [Struct module documentation](https://docs.micropython.org/en/latest/library/struct.html)

### Node

- [Noble - Node BLE lib](https://www.npmjs.com/package/@abandonware/noble#write)
- [Homebridge plugin for BLE xiaomi hygrothermograph](https://github.com/hannseman/homebridge-mi-hygrothermograph#readme)

## TODO

1. Add characteristic value validation
1. Verify if get and set characteristic should be separate or combined
