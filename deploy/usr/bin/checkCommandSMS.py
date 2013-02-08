

from pymodem import Modem
import pymodem.commands.at as at

modem = Modem('/dev/ttyHS0', 115200)
sanity = modem.AT(at.sanity() )
assert result.rval == 1, raise ValueError("Modem is not working")

# Turn on the RX/TX
modem.AT(at.cfun(fun=1) )

# 0) load existing results (mainly to avoid wiping out stuff
oldConfigs = readConfigFile('/home/new/connectConfig')

unreadSMSList = modem.AT( at.cmgl(stat="REC UNREAD") )
for message in unreadSMSList:
    # 1) authenticate sender
    authenticated = authenticateSMSMaster(message.da)
    if authenticated:
        # 2) parse message
        newConfigs = parseConfigSMS(message.message, config=oldConfigs)

# 3) store results
writeConfigFile(configFileLocation, configs)

################################
# define some helper functions #
################################

def readConfigFile(fileLocation):
    '''
    Some settings already exist (or at least a file does).
    Load up the old settings so we don't lose them.
    return a dict
    '''

def authenticateSMSMaster(blob):
    '''
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

def parseConfigSMS(sms):
    '''
    I want to receive config options through an SMS
    and return a dict
    
    Received format:
    key=value;key=value;key=value
    '''
    configList = sms.split(';')
    for setting in configList:
        settingList = setting.split('=')
        config[settingList[0]] = settingList[1]
    return config

def writeConfigFile(configFileLocation, configs):
    '''
    Write the config (as a dict) to the config file
    '''
