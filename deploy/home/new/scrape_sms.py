#!/usr/bin/python
import sys
import cmgpy
import time

at = cmgpy.commands.at
icon322 = cmgpy.Modem('/dev/ttyHS0', 115200)

sms_file = open('sms_history.txt', 'a') # append all SMS to file

print icon322.AT(at.cmgf(mode=1)).raw
icon322.send('AT+CMGL="ALL"\r\n')
print icon322.receive( )
result = icon322.AT(at.cmgl(stat="ALL"))

messages = result.messageList
print "found messages: %s" % (len(messages))
for message in messages:
    print message
    # {'date': '13/02/23,13:05:54-24', 'cmgl': '1', 'stat': 'REC READ', 'message': 'Str: blather!', 'da': '+19082165058'}
    formatted_message_string = message['date'] + ";" + message['da'] + ";\"" + message['message'] + "\""
    formatted_message_string = formatted_message_string.strip( )
    formatted_message_string = formatted_message_string.strip( )

    sms_file.write(formatted_message_string+'\n')

icon322.AT(at.cmgd(index=0, flag=4)) # delete ALL SMS with flag=4

#####
# EOF
