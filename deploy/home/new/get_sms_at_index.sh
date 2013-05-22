(echo "AT+CMGF=1"; echo "AT+CMGR=${1}"; sleep 1 ; echo ; sleep 1;  ) | socat - /dev/ttyHS1,raw,echo=0,crlf,nonblock
