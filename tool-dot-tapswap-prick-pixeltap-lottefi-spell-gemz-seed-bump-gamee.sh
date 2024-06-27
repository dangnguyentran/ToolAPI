#!/bin/bash

yellow='\033[1;33m'
reset='\033[0m'

while true; do
    # Thực thi dotcoins.py				
		python3 dotcoins.py --auto-upgrade y --clear-task y --upgrade-count 10 &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh dotcoins.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null
		
	# Thực thi tapswap.py			
		python3 tapswap.py --use_booster Y --use_upgrade N --use_kyc N --auto_clear Y --auto_claim_league Y &				
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh tapswap.py được thực thi. \nChờ 4 phút trước khi thực hiện lần tiếp theo..."
		sleep 240  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null
	
	 # Thực thi Prick.py			
		python3 prick.py --boost y &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh prick.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 3 minutes
		kill $pid
	
    # Thực thi Spell.py			
		python3 Spell.py --upgrade y &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh Spell.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid
 
  
	# Thực thi pixeltap.py	
		python3 pixeltap.py --auto-upgrade-pet y --max-level-pet 20 --auto-daily-combo y --user-input-order "1,4,3,2" &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh pixeltap.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	

	# Thực thi lottefi.py	
		python3 lottefi.py --start n --task n &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh lottefi.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	
	
	
	# Thực thi gemz.js	
		node gemz.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh gemz.js được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	
		
	# Thực thi seed.py	
		python3 seed.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh seed.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	
	# Thực thi bump.js	
		node bump.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh bump.js được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	
	
	# Thực thi gamee.py	
		python3 gamee.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \nTập lệnh gamee.py được thực thi. \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid
	
done
