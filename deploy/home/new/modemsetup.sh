echo AT&F >> /dev/ttyHS
echo ATE0V1&D2&C1S0=0 >>  /dev/ttyHS0
echo ATS0=0 >> /dev/ttyHS0
echo AT+CMGF=1 >> /dev/ttyHS0
echo AT+CMGL\"ALL\" >>/dev/ttyHS0
echo AT+CNMI=1,2 >> /dev/ttyHS0
