(echo "AT+CMGF=1"; echo "AT+CMGR=${1}"; echo ;   ) | socat - /dev/ttyHS0,raw,echo=0,crlf,nonblock
