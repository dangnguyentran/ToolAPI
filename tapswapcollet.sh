#!/usr/bin/expect

spawn python3 tapswap.py
			expect "prompt1"
			send "y\r"
			expect "prompt2"
			send "n\r"
			expect "prompt3"
			send "n\r"
			expect "prompt4"
			send "y\r"		
expect eof

