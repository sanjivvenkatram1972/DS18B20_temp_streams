# import os & time module
import os
import time

# Python package and CLI tool to work with w1 temperature sensors like DS1822, DS18S20 & DS18B20 on the Raspberry Pi
# pip install w1thermsensor
from w1thermsensor import W1ThermSensor

# import Azure IoTCentral module to load connections and relevant methods
from azureiotcmodule import *

# variable that lists available temperature sensors
var_sensorcount = W1ThermSensor.get_available_sensors()

# declare variable to capture list of temperature sensor IDs
global var_id1

# variable to capture the IDs of temperature sensors - naturally you know how many sensors you have connected - in this case 4
var_id1 = (var_sensorcount[0].id)
var_id2 = (var_sensorcount[1].id)
var_id3 = (var_sensorcount[2].id)
var_id4 = (var_sensorcount[3].id)

# declare a variable to capture a list of temperature outputs. Declare this empty to start with
my_temp = []

# within the main function of Azure IoT Central connect to Azure IoT Central with SAS key.
def main():

    device_client = IoTCClient(device_id, scopeId, IOTCConnectType.IOTC_CONNECT_DEVICE_KEY,sasKey)
    print(device_client)
    device_client.connect()
    device_client.send_property({"DevConn":50})
    print("device connected")
    
# while connected start the loop    
    while True:
        #print("ready")
        # define a method to capture temperature output
        def get_temp(sensr):
            # var_temperature variable gets the temperatures from sensors using the "sensr" parameter
            var_temperature = sensr.get_temperature()
            # the list my_temp then captures the temperature by appending temperatures values in sequence
            my_temp.append(var_temperature)
            # Ignore the first value of every sensor output (for values to stablelize)
            # we then capture the respective temp values from each sensor from the my_temp list
            if len(my_temp) > 3:
                print("Temperature 1 :",my_temp[::2][-1])
                print("Temperature 2 :",my_temp[1::2][-1])
                print("Temperature 3 :",my_temp[2::2][-1])
                print("Temperature 4 :",my_temp[3::2][-1])
        
        # connect to the respective sensor and add sensor id to respective variable
        var_sensor1 = W1ThermSensor(sensor_id=var_id1)
        var_sensor2 = W1ThermSensor(sensor_id=var_id2)
        var_sensor3 = W1ThermSensor(sensor_id=var_id3)
        var_sensor4 = W1ThermSensor(sensor_id=var_id4)

        # get the respective temperature value using the method from above
        var_value1 = get_temp(var_sensor1)
        var_value2 = get_temp(var_sensor2)
        var_value3 = get_temp(var_sensor3)
        var_value4 = get_temp(var_sensor4)

        # control stream rate
        time.sleep(0.0001)

if __name__ == '__main__':
    main()

