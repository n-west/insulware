#!/usr/bin/python
import sys
import cmgpy
import time

at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

icon322.AT(at.cfun(fun=4))
res =icon322.AT(at.cfun().query() )
print res.text
icon322.AT(at.cmgf(mode=1))
res = icon322.AT(at.cmgs(da="+19082165054", msg="Test from cmgpy"))
print res.text


#####
# EOF
