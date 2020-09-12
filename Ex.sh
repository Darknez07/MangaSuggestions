#! /bin/bash
cd Manga
./Runner.sh
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo install crontab
    Linux.sh
fi
schtasks /create /tn Prepare /tr Prepare.py /sc daily /st 08:00 /ed 12/31/2021 /f