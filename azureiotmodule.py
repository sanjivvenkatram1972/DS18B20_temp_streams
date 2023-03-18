# import IoT Central modules below - gihub link to download iotc: https://github.com/Azure/iot-central-python-client
# pip install iotc
from iotc import IoTCClient
from iotc import IOTCConnectType
from iotc import IoTCClient
from iotc import IOTCConnectType
import os
import time

# get the scope, device and sas key from Azure IoT Central device - click on connect to get these values
scopeId = ''
device_id = ''
sasKey = ''
