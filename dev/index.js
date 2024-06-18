// https://github.com/micropython/micropython-lib/blob/master/micropython/bluetooth/aioble/examples/temp_sensor.py

const noble = require('@abandonware/noble');

const service_uuid = 'cad6e164de14425f8d19f241b592a385'
const on_characteristic_uuid = 'd00b8ba4d8ce42ff92f2b0d193c58da4'
const set_on_characteristic_uuid = '19380250824b46c797a979761b8a27a7'
const brightness_characteristic_uuid = '127cf8c9b7fe47e3b2e03901b7988b00'
const set_brightness_characteristic_uuid = '66286dbfe5e946d4b300a0ec456f677c'

noble.on('stateChange', async (state) => {
    if (state === 'poweredOn') {
        await noble.startScanningAsync([service_uuid], false);
    }
});

async function setChr(char, val) {
    const bbuff = Buffer.alloc(1)
    bbuff.writeUInt8(val, 0)
    await char.writeAsync(bbuff, false)
}

noble.on('discover', async (peripheral) => {
    console.log('discovered peripherial', peripheral.address)
    await noble.stopScanningAsync();
    await peripheral.connectAsync();
    console.log('connected to peripherial')

    peripheral.on('disconnect', async () => {
        console.log('disconnected')
        await noble.startScanningAsync([service_uuid], false);
    })

    const { characteristics } = await peripheral.discoverAllServicesAndCharacteristicsAsync();

    const on_characteristic = characteristics.find(chr => chr.uuid === on_characteristic_uuid)
    const set_on_characteristic = characteristics.find(chr => chr.uuid === set_on_characteristic_uuid)
    const brightness_characteristic = characteristics.find(chr => chr.uuid === brightness_characteristic_uuid)
    const set_brightness_characteristic = characteristics.find(chr => chr.uuid === set_brightness_characteristic_uuid)

    brightness_characteristic.subscribe()
    brightness_characteristic.on('data', buff => {
        console.log('brightness', buff.readInt16LE())
    })

    on_characteristic.subscribe()
    on_characteristic.on('data', buff => {
        console.log('on', buff.readInt16LE())
    })

    setChr(set_on_characteristic, true);
    setChr(set_brightness_characteristic, 75);
});
