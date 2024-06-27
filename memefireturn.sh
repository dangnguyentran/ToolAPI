#!/bin/bash

while true; do
    python3 memefi.py &
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    yellow='\033[1;33m'
    reset='\033[0m'
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh memefi.py được thực thi. \nChờ 12 phút trước khi thực hiện lần tiếp theo..."
    sleep 720  # 720 seconds = 12 minutes
done
