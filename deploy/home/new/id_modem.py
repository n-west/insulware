#!/usr/bin/python
import sys
import cmgpy
import time

at = cmgpy.commands.at
#icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

# what is "what is my phone command?"
# AT+CNUM
icon322.send("AT+CNUM\r\n")
print icon322.receive( )

#####
# EOF
