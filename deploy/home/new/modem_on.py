#!/usr/bin/python
import sys
import cmgpy
import time

at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

print icon322.AT(at.cfun(fun=4))
print icon322.AT(at.cmgf(mode=4))


#####
# EOF
