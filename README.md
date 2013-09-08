Login&Fetch Data script for Ubiquiti AirOS devices
=============================================================
Little python script in beta stage for retrieve data of Ubiquiti AirOs devices, trought the web server, that is
not possible to be retrieved via SNMP (changed in last updates for Ubiquiti firmware).
You could retrieve some useful information, like channel,ccq, or frequency , for graph purposes or just for info.

Requierements:
You need to use the firmware 5.5.4 for best usage, and python-requests package installied.

Usage:

./ublogin.py  -i ip/hostname -u user -p password -s [ssl|off] -d [channel|freq|ccq]

Ex: /ublogin.py -i 192.168.1.20 -u ubnt -p ubnt -s off -d frequency

These options are avaliable for "-d" data retrive:

mode essid apmac channel frequency signal rssi noisef rstatus stats rx_nwids rx_crypts rx_frags tx_retries missed_beacons err_other hide_essid opmode antenna chains ack distance ccq txrate rxrate security qos count polling enabled quality capacity noack airsync_mode airsync_connections airsync_down_util airsync_up_util


Notes:

Now support SSL, but the certs are no verified.
