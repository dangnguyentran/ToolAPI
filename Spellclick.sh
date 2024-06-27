#!/usr/bin/expect

spawn python3 Spell.py
expect "prompt1"
send "y\r"
expect eof

