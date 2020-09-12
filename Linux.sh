#!/bin/bash
   if [ `id -u` -ne 0 ]; then
      echo "This script can be executed only as root, Exiting.."
      exit 1
   fi

case "$1" in
   install|update)

	CRON_FILE="/var/spool/cron/root"

	if [ ! -f $CRON_FILE ]; then
	   echo "cron file for root doesnot exist, creating.."
	   touch $CRON_FILE
	   /usr/bin/crontab $CRON_FILE
	fi
	grep -qi "Crawler" $CRON_FILE
	if [ $? != 0 ]; then
	   echo "Updating cron job for cleaning temporary files"
           /bin/echo "0 12 * * * \Manga\Runner.sh" >> $CRON_FILE
	fi
