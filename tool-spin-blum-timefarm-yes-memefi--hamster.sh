#!/data/data/com.termux/files/usr/bin/bash

yellow='\033[1;33m'
reset='\033[0m'

while true; do
    # Thực thi spinnercoin.js
    node spin.js &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh spin.js được thực thi. \nChờ 3 phút trước khi thực hiện lần tiếp theo..."
    sleep 300  # 300 seconds = 3 minutes
    kill $pid 2>/dev/null

    # Thực thi blum.py
    python blum1.py --task n --reff y &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh blum.py được thực thi. \nChờ 10 phút trước khi thực hiện lần tiếp theo..."
    sleep 600  # 1800 seconds = 10 minutes
    kill $pid 2>/dev/null

    # Thực thi timefarm.js
    node timefarm.js &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh timefarm.js được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
    sleep 120  # 120 seconds = 2 minutes
    kill $pid 2>/dev/null

    # Thực thi yescoin.js
    python3 yescoin.py --task y --multi n --fill n --max-level 10 &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh yescoin.js được thực thi. \nChờ 7 phút trước khi thực hiện lần tiếp theo..."
    sleep 420  # 600 seconds = 10 minutes
    kill $pid 2>/dev/null
	
	# Thực thi memefi.py
    python3 memefi.py &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh memefi.py được thực thi. \nChờ 8 phút trước khi thực hiện lần tiếp theo..."
    sleep 480  # 600 seconds = 10 minutes
    kill $pid
	
	# Thực thi hamsterclick.js
	node hamsterclick.js &
    pid=$!
    current_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo -e "\n[$yellow$current_time$reset] \nTập lệnh hamsterclick.js được thực thi. \nChờ 8 phút trước khi thực hiện lần tiếp theo..."
    sleep 480  # 600 seconds = 10 minutes
    kill $pid 2>/dev/null

		
done
