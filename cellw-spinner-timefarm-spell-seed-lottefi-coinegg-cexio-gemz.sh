#!/data/data/com.termux/files/usr/bin/bash

yellow='\033[1;33m'
blue='\033[0;32m'
reset='\033[0m'

while true; do
	
    # Thực thi cellwallet.py
		cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
		python3 cellwallet.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh cellwallet.py được thực thi.${reset} \nChờ 3 phút trước khi thực hiện lần tiếp theo..."
		sleep 180  # 300 seconds = 5 minutes
		kill $pid 2>/dev/null

	# Thực thi spinnercoin.js
		node spin.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh spin.js được thực thi.${reset} \nChờ 3 phút trước khi thực hiện lần tiếp theo..."
		sleep 180  # 300 seconds = 3 minutes
		kill $pid 2>/dev/null
	
	# Thực thi timefarm.js
		node timefarm.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh timefarm.js được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 120 seconds = 2 minutes
		kill $pid 2>/dev/null

	# Thực thi Spell.py			
		python3 Spell.py --upgrade y &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh Spell.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid
		
	# Thực thi seed.py	
		python3 seed.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh seed.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	

	# Thực thi lottefi.py	
		python3 lottefi.py --start n --task n &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh lottefi.py được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	

    # Thực thi coineeg.py
		cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
		python3 coinegg.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh coineeg.py được thực thi.${reset} \nChờ 5 phút trước khi thực hiện lần tiếp theo..."
		sleep 300  # 300 seconds = 5 minutes
		kill $pid 2>/dev/null 
	
	# Thực thi cexio.py
		cd /storage/emulated/0/Toolscripts/cexio-coineeg-cellwallet
		python3 cexio.py &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh cexio.py được thực thi.${reset} \nChờ 3 phút trước khi thực hiện lần tiếp theo..."
		sleep 180  # 300 seconds = 5 minutes
		kill $pid 2>/dev/null
	
	# Thực thi gemz.js	
		node gemz.js &
		pid=$!
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		yellow='\033[1;33m'
		reset='\033[0m'
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh gemz.js được thực thi.${reset} \nChờ 2 phút trước khi thực hiện lần tiếp theo..."
		sleep 120  # 600 seconds = 10 minutes
		kill $pid	
		

done