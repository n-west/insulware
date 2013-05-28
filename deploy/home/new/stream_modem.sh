#!/bin/bash

echo "setting up to monitor modem"
#python monitor_modem.py &
#sleep 3
#( socat -d -d  -u tcp:localhost:3333,crlf,nodelay -,ignoreeof,raw )

( socat -d -d  -u /dev/ttyHS1,nonblock,raw -,crlf   )
