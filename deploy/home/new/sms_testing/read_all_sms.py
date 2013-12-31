#!/usr/bin/python2.7


import cmgpy
at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

result = icon322.AT(at.cmgl(stat="REC UNREAD"))
messages = result.messageList
for message in messages:
    print " There is a new message!!!!!!!"
    print message

