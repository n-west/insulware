socat -u /dev/ttyHS0,raw,nonblock,crlf,echo=1,ignoreeof exec:'cat -'
