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
type('\033[1;34m Sometimes you need to be alone and think, not to be lonely')
type('\033[1;32m but to enjoy your free time being your self. [I am not happy]')
type('')
type('\033[1;33m* Created by Senja\033[0m')
type('')
type('')
exit(1)
time.sleep(1)
