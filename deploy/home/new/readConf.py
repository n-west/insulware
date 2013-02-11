#!/usr/bin/python

import ConfigParser
from optparse import OptionParser



    

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
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="f", default="connectConfig", help="path to config file")
    parser.add_option("-s", "--section",  dest="section", default="main",
                    help="section to read from")
    (opts, args) = parser.parse_args()
    f = opts.f
    section = opts.section
    #attrs = args
    #attrList = attrs.split(' ')
    s = parseConfig(f, section, args)
    for setting in args:
        print(s[setting]),
    

