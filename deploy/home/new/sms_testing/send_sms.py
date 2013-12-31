#!/usr/bin/python2.7
import cmgpy
at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

icon322.AT(at.cmgf(mode=1))

dest = "+19082165058"
message = "hello, from beagle"

result = icon322.AT(at.cmgs(da=dest, msg=message))
print result.text
