# SpotilightAPI

**SpotilightAPI** is a lightweight Python API built with **FastAPI** that controls **Tuya RGB Bulbs**. It listens for specific HTTP calls to toggle power or apply random color effects, making it ideal for integration with other automation tools or fun "party mode" scripts.

## 🛠️ Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 📋 Prerequisites

* **Docker Engine** (Required for containerized deployment)
* **Tuya Device Keys** (Local Key and Device ID)

> **Tip:** If you don't know how to get your Tuya `LOCAL_KEY` and `DEVICE_ID`, check out this [guide on the Home Assistant Community](https://community.home-assistant.io/t/how-i-made-tuya-local-work-with-full-color-controls/478030).

## 🚀 Installation & Deployment

You can deploy this API using Docker Compose (Recommended) or by building the image manually.

### Option A: Docker Compose (Recommended)
1.  **Download the configuration:**
    Ensure you have `docker-compose.yaml` in your working directory.

2.  **Configure Environment Variables:**
    Edit the `docker-compose.yaml` file (or create a `.env` file) to include your specific bulb credentials:

    ```yaml
    environment:
      - BULB_ID=your_device_id
      - BULB_IP=your_bulb_ip_address
      - BULB_SECRET=your_local_key
      - BULB_SWITCH_ON=True  # Set to False if you don't want to auto-on at boot
    ```

3.  **Start the Service:**
    ```bash
    docker compose up -d
    ```

### Option B: Manual Docker Build
If you prefer to build and run the container manually:

1.  **Build the Image:**
    ```bash
    docker image build -t spotilightapi .
    ```

2.  **Run the Container:**
    ```bash
    docker run --name spotilightapi \
      -e BULB_ID="YourDeviceID" \
      -e BULB_IP="192.168.x.x" \
      -e BULB_SECRET="YourLocalKey" \
      -e BULB_SWITCH_ON=True \
      -p 2890:2890 \
      spotilightapi
    ```

## ⚙️ Configuration

The application relies on the following environment variables:

| Variable | Type | Description |
| :--- | :--- | :--- |
| `BULB_ID` | `string` | **Required**. The unique Device ID of your Tuya Bulb. |
| `BULB_IP` | `string` | **Required**. The local IP address of the bulb on your network. |
| `BULB_SECRET` | `string` | **Required**. The "Local Key" for the device. |
| `BULB_SWITCH_ON`| `bool` | If `True`, the API will attempt to turn the bulb on when the container starts. |

## 📡 API Endpoints

The API exposes three specific endpoints to control the light:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | **Health Check.** Returns HTTP 418 ("I'm a teapot") to indicate the API is running. |
| `GET` | `/bar` | **Toggle.** Switches the bulb ON or OFF based on its current state. |
| `GET` | `/beat` | **Randomize.** Changes the bulb color to a random RGB value. |

> **Note:** Since this project uses FastAPI, you can also view the interactive Swagger documentation at `http://localhost:2890/docs` once the container is running.

## 👨‍💻 Local Development

If you want to contribute or run the code without Docker:

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Environment:**
    Rename `dev.env.sample` to `dev.env` and fill in your bulb details.

3.  **Run with Docker Compose (Dev Mode):**
    Use the local override file to mount your source code directly into the container:
    ```bash
    docker compose -f docker-compose.local.yaml up --build
    ```

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
