Login&Fetch Data script for Ubiquiti airOS devices
====================================

Little python script in beta stage for retrieve data of Ubiquiti airOS devices trought their web server that is
not possible to be retrieved via SNMP (changed in last updates of Ubiquiti firmware).
You could retrieve some useful information,like channel,ccq,or frequency and then use it for graph purposes or for info.


Requirements:
---
*You need to use the firmware 5.5.2 or greater, and python-requests package have to be installed.*


Usage:
---
Its easy!

Just "ublogin.py  -i ip/hostname -u user -p password -d [channel|frequency|ccq|signal|rssi]"

```
Ex: /ublogin.py -i 192.168.1.20 -u ubnt -p ubnt -d frequency
```
These options are avaliable for "-d" data retrive:

**
mode essid apmac channel frequency signal rssi noisef rstatus stats rx_nwids rx_crypts rx_frags tx_retries missed_beacons err_other hide_essid opmode antenna chains ack distance ccq txrate rxrate security qos count polling enabled quality capacity noack airsync_mode airsync_connections airsync_down_util airsync_up_util
**


The -o option is for output formatting, by this time only "zenoss" formating its included:

ZenOss need some output like "UnusefullData|dataouput=5318" for only handle the "5318".
If you create a local template for graph Ubiquiti devices in ZenOss, you only have to create the Data Source with the respective
command with "-o zenoss", and then add a Data Point with the "dataoutput" string, and link it to Graph Definition, and thats all!
Your data graphed on ZenOss ;)

**
Remember that ZenOss comes with a bundled version of Python, so you have to install python-requests manually!
You can follow a little how-to here: http://community.zenoss.org/thread/16119
**


Its very easy to add support for other formats, look inside the ".py" file and copy the syntax used for zenoss and that's all!


Notes:
---
Now support SSL requests,but the certs are no verified.

Feedback will be appreciated =)
Ramiro <sabueso_dot_sabueso_dot_org>
