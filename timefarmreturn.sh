#!/bin/bash

while true; do
    node timefarm.js &
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    yellow='\033[1;33m'
    reset='\033[0m'
    echo -e "\n[$yellow$current_time$reset] \nScript timefarm.js executed. Waiting for 60 minutes before next execution..."
    sleep 3600  # 3600 seconds = 60 minutes
done


