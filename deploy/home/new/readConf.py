#!/usr/bin/python

import ConfigParser
import sys 

def parseConfig(f, section, attrList):
    ''' 
    read section of an ini conf file and 
    print/return requested settings
    '''
    parser = ConfigParser.SafeConfigParser()
    parser.read(f)
    attrRequested = dict()
    for attr in attrList:
        value = parser.get(section, attr)
        attrRequested[attr] = value
    return attrRequested


if __name__ == "__main__":
    args = sys.argv
    f = args[1]
    section = args[2]
    #attrs = args
    #attrList = attrs.split(' ')
    confArgs = args[3:-1]
    s = parseConfig(f, section, confArgs)
    for setting in args:
        print(s[setting]),
    

