#!/bin/bash
export PATH=.:$PATH
./modemsetup.sh
./stream_modem.sh | ./getsmsid.sh | while read sms_id ; do
  sms=$(get_sms_at_index.sh $sms_id | grep STR)
  echo $(date +%FT%T): "$sms"
  read preamble config_url <<<$sms
  # config_url=$(echo "$sms" | cut -d' ' -f 2)
  echo $(date +%FT%T): config_url "$config_url"
  test -n ${config_url} && ( rm new.config ; validate_config "${config_url}" new.config )
  if [[ -f new.config ]] ; then
    mv new.config good.config
    # do the auditing
    echo $(date +%FT%T): auditing..."
    tail -n 40 good.config
    setup_session good.config
    # delete $sms_id
    echo $(date +%FT%T): deleting $sms_id"
    delete_sms_at $sms_id
  fi
done
