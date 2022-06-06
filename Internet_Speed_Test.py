# pip install speedtest

import speedtest
wifi = speedtest.Speedtest()
print('Wifi Downlaod Speed is',wifi.download())
print('Wifi Upload Speed is',wifi.upload())
