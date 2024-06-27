#!/data/data/com.termux/files/usr/bin/bash

yellow='\033[1;33m'
blue='\033[0;32m'
reset='\033[0m'

while true; do
	# Thực thi coineeg.py
		cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
		python3 coinegg.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh coineeg.py được thực thi.${reset} \nChờ 10 phút trước khi thực hiện lần tiếp theo..."
		sleep 600  # 300 seconds = 5 minutes
		kill $pid 2>/dev/null 
	
	# Thực thi cyberfinance.py
		python3 cyberfinance.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh cyberfinance.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 2 minutes
		kill $pid 2>/dev/null
	
	# Thực thi gleam.py
		python3 gleam.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh gleam.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid
	
	# Thực thi gemz.js
		cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
		python3 gemz.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh gemz.js được thực thi.${reset} \nChờ 10 phút trước khi thực hiện lần tiếp theo..."
		sleep 600  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi supermeowall.py				
		python3 supermeowall.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh supermeowall.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi arix.py			
		python3 arix.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh arix.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 3 minutes
		kill $pid

	# Thực thi matchain.py	
		python3 matchain.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh matchain.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	

	# Thực thi metaboss			
		python3 tapswap.py --use_booster Y --use_upgrade N --use_kyc N --auto_clear Y --auto_claim_league Y &				
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh tapswap.py được thực thi.${reset} \nChờ 1 phút trước khi thực hiện lần tiếp theo..."
		sleep 60  # 600 seconds = 10 minutes
		kill $pid 2>/dev/null

	# Thực thi pocketfi	
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