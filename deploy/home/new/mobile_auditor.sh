#!/bin/sh
# send a medical device to the cloud (cloudify!)

export CONF="connectConfig"
alias read_config='git config -f $CONF --get'
while true;
do
# detect devices, noop for now
device_vid=$(read_config deviceDetect.vid)
device_pid=$(read_config deviceDetect.pid)
dede_output=$(./detectDevices $(device_vid) $(device_pid) )

if $dede_output == 'true' # if there's a device connected...
then 
    # alert the mothership of incoming connection
    resourceReq_addr=$(read_config resourceRequest.addr)
    resourceReq_port=$(read_config resourceRequest.port)
    resourceReq_page=$(read_config resourceRequest.page)
    resourceReq_user=$(read_config resourceRequest.user)
    resourceReq_key=$(read_config resourceRequest.key)
    resourceRequestOptions='$resourceReq_addr $resourceReq_port resourceReq_page resourceReq_user resourceReq_key'
    
    BAUD=$(./requestResources $resourceRequestOptions)
    
    # connect the socket
    audit_addr=$(read_config serialToNet.addr)
    audit_port=$(read_config serialToNet.port)
    net_output=$(./serialToNet $audit_addr $audit_port)
fi # if true

done #while true;

