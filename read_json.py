import json

with open("dispositivos_rmc.json","r") as f:
   data = json.load(f)

for device in data['devices']:
   # Getting all management IPs of all devices
   
   if "management" in device['nics'].keys():
        print("Device {0} --> management IP {1}".format(device['name'],device['nics']['management']['IP']))
   if "data" in device['nics'].keys():
        print("Device {0} --> data IP {1}".format(device['name'],device['nics']['data']['IP']))
 
