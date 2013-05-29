#!/bin/bash
export PATH=.:$PATH
LOG_FILE="/home/new/logfile.txt"
echo "modemsetup"
./modemsetup.sh
echo "streaming modem"
set -x
#( rewind_messages ;
#( ./stream_modem.sh | ./getsmsid.sh )) | while read sms_id ; do
# ./stream_modem.sh | while read sms_id ; do
./stream_modem.sh | while read notification ; do
  echo INCOMING $notification
  sms_id=$(echo $notification | grep CMTI | ./getsmsid.sh)
  test -z $sms_id && continue
  sms=$(get_sms_at_index.sh $sms_id | grep STR)
  echo "$(date +%FT%T): ${sms_id}: $sms"
  config_url=$(echo "$sms" | cut -d' ' -f 2)
  echo $(date +%FT%T): config_url "$config_url"
  echo "RADIO MODE"
  # pon
  pon icon322
  sleep 15
  /sbin/ifconfig | tee - a $LOG_FILE
  /sbin/route -n | tee - a $LOG_FILE
  ping -c2 google.com
  ping -c2 173.194.43.9
  rm -f new.config 
  cat /etc/resolv.conf
  test -n ${config_url} && validate_config "${config_url}" new.config
  if [[ -f new.config ]] ; then
    mv new.config good.config
    # do the auditing
    echo "$(date +%FT%T): auditing..."
    setup_session good.config
    # delete $sms_id
    echo "$(date +%FT%T): deleting ${sms_id}"
    delete_sms_at $sms_id
  fi
  poff
done
