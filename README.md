Ubiquiti Login Script
==============================================
Pequeña script en Python en estado mas que beta para poder recolectar informacion de equipos
de Ubiquiti (www.ubnt.com) que ya no se obtiene via SNMP.

Los equipos soportados son todos aquellos que llevan AirOs 5.5.4 en adelante.
Es necesario contar con la libreria "requests" de Python.

Uso:

ublogin.py host username password

Ex: ublogin.py 192.168.1.20 ubnt ubnt

Nota:

-No funciona si el acceso a la antena es via ssl (lo implementare en breve)

-De momento, los valores han de ser extraidos via grep, la proxima release ya podran ser consultados via su nombre, como pueden ser "frequency" o "channel".

