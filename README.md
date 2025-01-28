# SpotilightAPI
An API that listen to predefined calls to change the color and brightness of Tuya RGB Bulbs

## Requirements
 - Docker

## Setup
### Docker Compose
To run this application download the `docker-compose.yaml` and edit these environment variable 
 - BULB_ID
 - BULB_IP
 - BULB_SECRET

with your Tuya Bulb data. ([How to obtain them](https://community.home-assistant.io/t/how-i-made-tuya-local-work-with-full-color-controls/478030)) \
Then, in the same folder, create and run the container with
``` bash
docker compose up -d
```

### Building Manually
 1. Download or clone the repository
 2. Open a terminal in the repository folder and build the docker image
 ``` bash
 docker image build -t spotilightapi .
 ```
 3. Create and run the container with your Bulb data
 ``` bash
docker run --name spotilightapi \
-e BULB_ID=YourIDHere \
-e BULB_IP=1.2.3.4 \
-e BULB_SECRET="SecretHere" \
-p 2890:2890 \
spotilightapi
 ```

## Documentation
Since this API uses FastAPI as a backend, you can see the auto-generated docs by appending `/docs` or `/redoc`

## Contribution
If you want to improve the code you can use the `docker-compose.local.yaml` to build the application. \
Edit with your bulb data and rename the `dev.env.sample` file to `dev.env` to keep your data safe from future git commits

## License
Distributed under the MIT License. See `LICENSE` for more information.
