# Text

import os, sys, time, random

def banner():
	os.system('clear')
banner()

def type(y):
	for x in y + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(random.random() * 0.3 )
type('\033[1;45m\033[97;1m QUOTES \033[0m')
type('')
type('')
type('\033[1;34m Pursue Perfection Then Success Will Overtake You ')
type('\033[1;32m Learn What You Like Then You Will Easily Understand \033[0m')
type('')
type('\033[1;33m* Created by Senja\033[0m')
type('')
type('')
exit(1)
time.sleep(1)
