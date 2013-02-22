#!/usr/bin/python

from pymodem import Modem
import pymodem.commands.at as at
import subprocess
import re

################################
# define some helper functions #
################################

def readConfigFile(fileLocation):
    '''
    Some settings already exist (or at least a file does).
    Load up the old settings so we don't lose them.
    return a dict
    '''
    fileObject = open(fileLocation, 'r')
    config = {}
    for line in fileObject:
        keyVals = line.split('=')
        config[keyVals[0] ] = keyVals[1]
    fileObject.close()
    return config

def messageSanitizer(messageString):
    '''
    Expect something along the lines of:
    FRM:Nathan West \nSUBJ:config\nMSG:CMD URI\r\n
    return a dict with keys: sender, subject, message
    '''
    print messageString
    qar = re.match('FRM:(?P<sender>.*)\n'+ # match sender
            'SUBJ:(?P<subject>.*)\n'+ # grab the subject
            'MSG:(?P<message>.*\n)', # the rest is the message
            messageString )
    print qar.groupdict()
    return qar.groupdict()

def authenticateSMSMaster(blob):
    '''
    TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO:
    This is slightly awkward.. I don't have a good idea for doing this yet
    Receiving an SMS from an email, a la to: 9082165058@txt.att.net
    Results in an SMS with da being ATT's SMS gateway and the actual
    sender's identity is in text along with the content. This creates
    a pretty legitimate security nightmare. For now (for demo purposes)
    I'm just going to return True; however, this MUST be fixed.

    For example:
    FRM:Earle West \nSUBJ:POLLING YOU\nMSG:7328584026@txt.att.net\r\ncurl --request POST 'http://transactionalweb.com/mconnect.php'
    '''
    return True

def parseConfigSMS(sms, config):
    '''
    I want to receive config options through an SMS
    and return a dict
    
    Received format:
    key=value;key=value;key=value
    '''
    configList = sms.split(';')
    for setting in configList:
        print "setting "
        print setting
        settingList = setting.split('=')
        print "settingList: "
        print settingList
        config[settingList[0]] = settingList[1]
    return config

def parseCommandSMS(sms):
    '''
    Receive command and uri through an SMS and return a dict with cmd, uri

    received format:
    cmd uri
    '''
    instruction = dict()
    splitSMS = sms.split(' ',1) # break up cmd and uri by the first space
    instruction['command'] = splitSMS[0] 
    instruction['resource'] = splitSMS[1]
    print 'L82;print cmd'
    print instruction['command'] + '::::' + instruction['resource']
    return instruction
    
def fetch(uri):
    ''' fetch a uri with curl, return the filename '''
    # This is hacky, but I don't really like this anyway...
    uri = uri.strip()
    fileName = uri.split('/')[-1].split('?')[0]
    print uri
    print fileName
    with open("/home/nathan/%s"%fileName, 'w') as config_file:
            subprocess.Popen(["curl", uri], stdout=config_file)
    return fileName

def execute(fileName):
    ''' given a fileName that should exist, run it '''
    call("./home/new/%s" % fileName)
    

def writeConfigFile(configFileLocation, configs):
    '''
    Write the config (as a dict) to the config file
    A convenient thing about this is that we only ADD or MODIFY
    to the config file. This means I don't have to worry about
    the length of the file. I can overwire mercilessly since
    the write will always be at least as long as the read.

    Which brings up a question.... Do we add ability to REMOVE
    eventually? If so, we'll need a /COMMAND/ parser instead of
    just this /CONFIG/ parser.
    '''
    fileObject = open(configFileLocation, 'w')
    for item in configs:
        fileObject.write("%s=%s\n" % (item, configs[item]) )
    fileObject.close()
        
##################
# main execution #
##################

# QUESTION: should configFile be a parameter?
configFile = '/home/nathan/code/insulware/deploy/home/new/connectConfig'
modem = Modem('/dev/ttyHS0', 115200)
sanity = modem.AT(at.sanity() )
assert sanity.rval == 1, "MODEM IS NOT WORKING"

# Turn on the RX/TX
modem.AT(at.cfun(fun=1) )
modem.AT(at.cmgf(mode=1) ) # text mode

# 0) load existing results (mainly to avoid wiping out stuff
# configs = readConfigFile(configFile)

unreadSMSList = modem.AT( at.cmgl(stat="REC UNREAD") )

for message in unreadSMSList.messageList:
    print 'L133:printing message:'
    print message['message']
    # 0.5) sanitize
    messageData = messageSanitizer(message['message'])
    # 1) authenticate sender
    authenticated = authenticateSMSMaster(message['message'])
    assert authenticated == True, "Warning, unauthenticated text!"
    # 2) parse message
    instruction = parseCommandSMS(messageData['message'])
    
    # 3) act on instruction
    if instruction['command'] == 'STR':
        # curl the file and save in home dir
        fetch(instruction['resource'])
    elif instruction['command'] == 'EXEC1':
        # curl the file and save in home dir
        fileName = fetch(instruction['resource'])
        # execute the file
        execute(fileName)
    elif instruction['command'] == 'EXEC':
        # execute the file
        execute(fileName)
    else:
        # what to do if the instruction is unknown?
        pass

# clean up (turn off rx/tx)
modem.AT(at.cfun(fun=4) )
