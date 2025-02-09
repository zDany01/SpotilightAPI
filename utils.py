from tinytuya import BulbDevice
from os import environ
from random import randint

bulb: BulbDevice = None

def strBool(value: str) -> bool:
    return value.lower() in ["true", "1", "on"]

def getBulb() -> BulbDevice:
    global bulb
    if bulb is not None:
        return bulb
    
    try:
        bulbID = environ["BULB_ID"]
        bulbIP = environ["BULB_IP"]
        bulbSecret = environ["BULB_SECRET"]
        bulbSwitch = environ["BULB_SWITCH_ON"]
        if not bulbID or not bulbIP or not bulbSecret:
            raise ValueError()
    except:
        print("Unable to get Bulb Info.\nRemember to set your bulb info in the docker environment!")
        exit(1)
    
    bulb = BulbDevice(
        dev_id=bulbID,
        address=bulbIP,
        local_key=bulbSecret,
        version=3.3
    )

    if strBool(bulbSwitch):
        bulb.turn_on()
        bulb.set_white(1000, 1000)

    return bulb

def randomColor(color) -> int:
    color += randint(0, 255)
    return color if color < 256 else color - 255