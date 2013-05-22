#!/bin/bash
export PATH=.:$PATH
echo "modemsetup"
./modemsetup.sh
echo "streaming modem"
#( rewind_messages ;
#( ./stream_modem.sh | ./getsmsid.sh )) | while read sms_id ; do
( ./stream_modem.sh | ./getsmsid.sh ) | while read sms_id ; do
  sms=$(get_sms_at_index.sh $sms_id | grep STR)
  echo "$(date +%FT%T): ${sms_id}: $sms"
  config_url=$(echo "$sms" | cut -d' ' -f 2)
  echo $(date +%FT%T): config_url "$config_url"
  rm -f new.config 
  test -n ${config_url} && validate_config "${config_url}" new.config
  if [[ -f new.config ]] ; then
    mv new.config good.config
    # do the auditing
    echo "$(date +%FT%T): auditing..."
    setup_session good.config
    # delete $sms_id
    echo "$(date +%FT%T): deleting ${sms_id}"
    # delete_sms_at $sms_id
  fi
done
