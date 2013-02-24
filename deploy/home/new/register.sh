#!/bin/sh
# Run every time a new config is downloaded
PUBKEYLOC=$1

# 0) generate an ssh config, send to mothership
./ssh_setup $PUBKEYLOC

# 1) enable systemd service to poll devices
systemd enable med_auditor
