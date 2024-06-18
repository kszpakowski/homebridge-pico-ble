# BLE Light

A Raspberry PI Pico W as a smart light driver using BLE and homebridge

## Why BLE?

1. No need for setting up wifi connection!

## How it works?

RPI runs a BLE server, with a user defined service

### Service

UUID cad6e164de14425f8d19f241b592a385

### Characteristics

|name|uuid|desc|
|-|-|-|
|on|d00b8ba4d8ce42ff92f2b0d193c58da4||
|set_on|19380250824b46c797a979761b8a27a7||
|brightness|127cf8c9b7fe47e3b2e03901b7988b00||
|set_brightness|66286dbfe5e946d4b300a0ec456f677c||

> TODO describe more details

## References

### BLE

- [Adafruit Introduction to Bluetooth Low Energy](https://learn.adafruit.com/introduction-to-bluetooth-low-energy/gatt)

### Pico

- [Low level BLE Micropython module](https://docs.micropython.org/en/latest/library/bluetooth.html)
- [High level, object oriented, asyncio based Micropython BLE module](https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble)

### Node

- [Homebridge plugin for BLE xiaomi hygrothermograph](https://github.com/hannseman/homebridge-mi-hygrothermograph#readme)
- [Noble - Node BLE lib](https://www.npmjs.com/package/@abandonware/noble#write)
