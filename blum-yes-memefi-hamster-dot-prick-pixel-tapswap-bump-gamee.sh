#!/data/data/com.termux/files/usr/bin/bash

yellow='\033[1;33m'
blue='\033[0;32m'
reset='\033[0m'

while true; do
	# Thực thi blum.py
		python3 blum1.py --task n --reff y &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh blum.py được thực thi.${reset} \nChờ 10 phút trước khi thực hiện lần tiếp theo..."
		sleep 600  # 1800 seconds = 10 minutes
		kill $pid 2>/dev/null
	
	# Thực thi yescoin.js
		python3 yescoin.py --task y --multi n --fill n --max-level 10 &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh yescoin.js được thực thi.${reset} \nChờ 8 phút trước khi thực hiện lần tiếp theo..."
		sleep 480  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null
	
	# Thực thi memefi.py
		python3 memefi.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh memefi.py được thực thi.${reset} \nChờ 8 phút trước khi thực hiện lần tiếp theo..."
		sleep 480  # 600 seconds = 10 minutes
		kill $pid
	
	# Thực thi hamsterclick.js
		node hamsterclick.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh hamsterclick.js được thực thi.${reset} \nChờ 8 phút trước khi thực hiện lần tiếp theo..."
		sleep 480  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi dotcoins.py				
		python3 dotcoins.py --auto-upgrade y --clear-task y --upgrade-count 10 &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh dotcoins.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi Prick.py			
		python3 prick.py --boost y &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh prick.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 3 minutes
		kill $pid

	# Thực thi pixeltap.py	
		python3 pixeltap.py --auto-upgrade-pet y --max-level-pet 20 --auto-daily-combo y --user-input-order "1,4,3,2" &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh pixeltap.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	

	# Thực thi tapswap.py			
		python3 tapswap.py --use_booster Y --use_upgrade N --use_kyc N --auto_clear Y --auto_claim_league Y &				
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh tapswap.py được thực thi.${reset} \nChờ 1 phút trước khi thực hiện lần tiếp theo..."
		sleep 60  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi bump.js	
		node bump.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh bump.js được thực thi.${reset} \nChờ 1,5 phút trước khi thực hiện lần tiếp theo..."
		sleep 90  # 600 seconds = 10 minutes
		kill $pid	
		
	# Thực thi gamee.py	
		python3 gamee.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh gamee.py được thực thi.${reset} \nChờ 1.5 phút trước khi thực hiện lần tiếp theo..."
		sleep 90  # 600 seconds = 10 minutes
		kill $pid
	
done