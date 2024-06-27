#!/bin/bash

while true; do
	cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
    python3 gemz.py &	
	pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    yellow='\033[1;33m'
    reset='\033[0m'
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh gemz.js được thực thi. \nChờ 10 phút trước khi thực hiện lần tiếp theo..."
    sleep 600  # 600 seconds = 10 minutes  
	kill $pid 2>/dev/null
done