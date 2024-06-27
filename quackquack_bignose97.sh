#!/data/data/com.termux/files/usr/bin/bash

yellow='\033[1;33m'
blue='\033[0;32m'
reset='\033[0m'
		# Thực thi bignose.js
		cd /storage/emulated/0/Toolscripts/quackquack/quack
		node bignose.js 2 		
		current_time=$(date +"%Y-%m-%d %H:%M:%S")
		echo -e "\n[$yellow$current_time$reset] \n${blue}Tập lệnh bignose.js được thực thi.${reset} \nChờ 100000 phút trước khi thực hiện lần tiếp theo..."
