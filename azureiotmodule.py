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

# connect to azure IoT Central
def main():
    device_client = IoTCClient(device_id, scopeId, IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,sasKey)
    print(device_client)
    device_client.connect()
    device_client.send_property({"DevConn":50})
    print("device connected")

if __name__ == '__main__':
    main()
