#!/bin/bash

# cron setting for the pc_health_check.py (the cron-job will be running once in every 10 minutes)
newjob="*/10 * * * * /home/adb_linux/system_health_monitor/scripts/pc_health_check.py"
# create a file of all exiting cron-jobs
crontab -l -u "$(whoami)" > currentjob.txt

# check if the job to be added already exist in the cron list, making the script idempontent
if cat currentjob.txt | grep -qFx "$newjob"; then
    echo "job already exist"
    rm currentjob.txt
    exit
else
    # create an empty line comment
    echo "#" >> currentjob.txt
    # add the new cron-job to the list of existing ones
    echo "$newjob" >> currentjob.txt
    # s used to update the crontab (cron table) for the current user with the contents of the file "currentjob.txt
    error=$(crontab currentjob.txt -u "$(whoami)" 2>&1 >/dev/null)

    if crontab -l -u "$(whoami)" | grep -qFx "$newjob"; then
        echo "Job Added Successfully"
        rm currentjob.txt
    else
        echo "could not add cron-job"
        echo "Error: $error"
    fi
fi
