#This module has components that are used for testing tuya's device control and Pulsar massage queue."""
import logging, os, json
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,
)

ACCESS_ID = "jc338gqh8uenmjy7fvtr"
ACCESS_KEY = "f42b02bbda7e4e1bb487ef5f595a2d35"
API_ENDPOINT = "https://openapi.tuyaus.com"
MQ_ENDPOINT = "wss://mqe.tuyaus.com:8285/"

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

os.system("cls")
print("***************************************************************")
# Call any API from Tuya
response = openapi.get("/v2.0/cloud/thing/ebcb53d2b3bc86a004nmkn/shadow/properties", dict())

print("============================================================")

#resultado = json.load(response)
for dato in response["result"]["properties"] :
  print(dato["code"])
  print(dato["value"])


#print(response["result"]["properties"][0]["value"])

# Init Message Queue
#open_pulsar = TuyaOpenPulsar(
#    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
#)
# Add Message Queue listener
#open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

# Start Message Queue
#open_pulsar.start()

#input()
# Stop Message Queue
#open_pulsar.stop()