#!/bin/bash
( 
echo "AT&F";
echo "ATE0V1&D2&C1S0=0"
echo "ATS0=0"
echo "AT+CMGF=1"; echo "AT+CMGL\"ALL\""
echo "AT+CNMI=1,2";
echo "AT+CMGF=1";
echo ;
) | socat - /dev/ttyHS0,raw,echo=0,crlf,nonblock
