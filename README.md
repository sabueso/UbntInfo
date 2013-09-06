Pequeña aplicacion en Python en estado mas que beta para poder recolectar
informacion que ya no se obtiene via SNMP.

Uso:

ublogin.py host username password

Ex: ublogin.py 192.168.1.20 ubnt ubnt

Nota: 
-No funciona si el acceso a la antena es via ssl
-De momento, los valores han de ser extraidos via grep, la proxima release ya podran
ser consultados via su nombre, como pueden ser "frequency" o "channel".
