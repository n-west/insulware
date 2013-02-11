#!/usr/bin/python

import ConfigParser
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f", "--file", dest="f", default="connectConfig",
                help="path to config file")
parser.add_option("-s", "--section",  dest="section", default="main",
                help="section to read from")

    

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
        print(value),
        attrRequested[attr] = value
    return attrRequested


if __name__ == "__main__":
    (opts, args) = parser.parse_args()
    f = opts.f
    section = opts.section
    #attrs = args
    #attrList = attrs.split(' ')
    parseConfig(f, section, args)
