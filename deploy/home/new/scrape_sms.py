import cmgpy
at = pymodem.commands.at
icon322 = pymodem.Modem('/dev/ttyHS0', 115200)

sms_file = open('sms_history.txt', 'a') # append all SMS to file

result = icon322.AT(at.cmgl(stat="ALL"))
messages = result.messageList
for message in messages:
    # do we format the SMS first? 
    # TODO: add an example of what gets printed here
    sms_file.write(message)
    icon322.AT(at.cmgd(index=0, flag=4)) # delete ALL SMS with flag=4

