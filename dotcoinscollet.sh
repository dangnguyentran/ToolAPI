#!/usr/bin/expect

spawn python3 dotcoins.py
expect "prompt1"
send "y\r"
expect "prompt2"
send "y\r"
expect "prompt3"
send "1\r"
expect eof

