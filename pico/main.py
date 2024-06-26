import sys


from micropython import const

import asyncio
import aioble
import bluetooth

import random
import struct

from lights import PwmLight

light = PwmLight(4, brightness=0)

_SRV_UUID = bluetooth.UUID("cad6e164-de14-425f-8d19-f241b592a385")
_ON_CHR_UUID = bluetooth.UUID("d00b8ba4-d8ce-42ff-92f2-b0d193c58da4")
_SET_ON_CHR_UUID = bluetooth.UUID("19380250-824b-46c7-97a9-79761b8a27a7")
_BRIGHTNESS_CHR_UUID = bluetooth.UUID("127cf8c9-b7fe-47e3-b2e0-3901b7988b00")
_SET_BRIGHTNESS_CHR_UUID = bluetooth.UUID("66286dbf-e5e9-46d4-b300-a0ec456f677c")


_ADV_APPEARANCE_LIGHT_DRIVER = const(596)

# How frequently to send advertising beacons.
_ADV_INTERVAL_MS = 250_000
_STATE_UPDATE_INTERVAL_MS = 2000


# Register GATT server.
light_service = aioble.Service(_SRV_UUID)

on_characteristic = aioble.Characteristic(
    light_service, _ON_CHR_UUID, read=True, notify=True
)

set_on_characteristic = aioble.Characteristic(
    light_service, _SET_ON_CHR_UUID, capture=True, write=True
)

brightness_characteristic = aioble.Characteristic(
    light_service, _BRIGHTNESS_CHR_UUID, read=True, notify=True
)

set_brightness_characteristic = aioble.Characteristic(
    light_service, _SET_BRIGHTNESS_CHR_UUID, capture=True, write=True
)

aioble.register_services(light_service)


async def read_set_on_chr_task():
    while True:
        _, data = await set_on_characteristic.written()
        val = struct.unpack("<b", data)
        light.set_on(bool(val[0]))


async def read_set_brightness_chr_task():
    while True:
        _, data = await set_brightness_characteristic.written()
        val = struct.unpack("<b", data)
        light.set_brightness(val[0])


async def update_task():
    while True:
        on_characteristic.write(
            struct.pack("<b", light.get_state()["on"]), send_update=True
        )
        brightness_characteristic.write(
            struct.pack("<b", light.get_state()["brightness"]), send_update=True
        )
        await asyncio.sleep_ms(_STATE_UPDATE_INTERVAL_MS)


async def peripheral_task():
    while True:
        async with await aioble.advertise(
            _ADV_INTERVAL_MS,
            name="pico-light-ble",
            services=[_SRV_UUID],
            appearance=_ADV_APPEARANCE_LIGHT_DRIVER,
        ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected(timeout_ms=None)


async def main():
    t1 = asyncio.create_task(update_task())
    t2 = asyncio.create_task(peripheral_task())
    t3 = asyncio.create_task(read_set_on_chr_task())
    t4 = asyncio.create_task(read_set_brightness_chr_task())
    await asyncio.gather(t1, t2, t3, t4)


asyncio.run(main())
