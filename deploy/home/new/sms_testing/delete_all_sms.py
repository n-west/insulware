#!/usr/bin/python2.7
import cmgpy
at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

result = icon322.AT(at.cmgd(index=0, flag=4))
