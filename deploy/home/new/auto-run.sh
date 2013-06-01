#!/bin/bash

PATH=$PATH:.

print_sms | while read OP config_url ; do
  rm new.config
  echo "performing $OP"
  echo "config $config_url"
  validate_config $config_url new.config
  if [[ -f new.config ]] ; then
    mv new.config good.config
    auditor=$(setup_session good.config)  # tell management to give us a port now!
    # tell management to give us a port now!
    setup_session good.config
  fi
done
