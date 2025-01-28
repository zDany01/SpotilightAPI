from fastapi import FastAPI, responses, Depends
from fastapi.middleware.cors import CORSMiddleware
from tinytuya import BulbDevice
from random import randint
import utils

reset: bool = False
red: int = randint(0, 255)
green: int = randint(0, 255)
blue: int = randint(0, 255)

utils.getBulb() #Cache the bulb and perform the check before an API call occurs

api = FastAPI(title="SpotilightAPI", description="An API that listen to predefined call to change the color and brightness of Tuya RGB Bulbs", version="0.1", license_info={"name": "MIT License", "identifier": "MIT", "url": "https://github.com/zDany01/SpotilightAPI/blob/main/LICENSE"})
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/", response_class=responses.PlainTextResponse, status_code=418)
def root():
    pass

@api.head("/beat", response_class=responses.PlainTextResponse, status_code=200)
def process_beat(bulb: BulbDevice = Depends(utils.getBulb)):
    global reset
    bulb.set_brightness_percentage(0 if reset else 100, True)
    reset = not reset

@api.head("/bar", response_class=responses.PlainTextResponse, status_code=200)
def process_bar(bulb: BulbDevice = Depends(utils.getBulb)):
    global red, green, blue
    red = utils.randomColor(red)
    green = utils.randomColor(green)
    blue = utils.randomColor(blue)
    bulb.set_colour(red, green, blue, True)