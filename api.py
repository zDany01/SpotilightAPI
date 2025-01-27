from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware

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