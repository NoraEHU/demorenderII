import requests
import random
import time

URL = "https://demorenderii.onrender.com"
URL_PATH = URL + "/api/data"

while True:
    data = {
        "device_id": "sensor_1",
        "value": round(random.uniform(20, 30), 2)
    }
    r = requests.post(URL_PATH, json=data)
    print(f"Sent: {data}, Response: {r.json()}")
    time.sleep(5)
