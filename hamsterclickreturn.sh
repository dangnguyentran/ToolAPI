#!/bin/bash

while true; do
    node hamsterclick.js &
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    yellow='\033[1;33m'
    reset='\033[0m'
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh hamsterclick.js được thực thi. \nChờ 21 phút trước khi thực hiện lần tiếp theo..."
    sleep 1260  # 1260 seconds = 21 minutes
done
