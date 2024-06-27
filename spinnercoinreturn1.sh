#!/bin/bash

while true; do
    node spinres.js &
	current_time=$(date +"%Y-%m-%d %H:%M:%S")
    yellow='\033[1;33m'
    reset='\033[0m'
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh spinnercoin.js được thực thi. \nChờ 60 phút trước khi thực hiện lần tiếp theo..."
    sleep 3600  # 3600 seconds = 60 minutes
done