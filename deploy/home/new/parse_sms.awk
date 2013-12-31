#!/usr/bin/awk -f 

BEGIN {
    FS=";"
    getline last_read_sms < ".last_read_sms.txt"
    print $last_read_sms
    found_last = 0
    print "hello, done begin"
}

{
    if ($0 == $last_read_sms) {
        found_last = 1
        # parse all of the remaining SMS
    }

}



