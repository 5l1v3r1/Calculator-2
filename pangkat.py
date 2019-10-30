# Pemanfkatan

import os, sys, time

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
print
write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mChecking...')
print
print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPemangkatan')
number1 = input('\033[0m[\033[95;1m*\033[0m] Enter numbers : \033[1;77m')
number2 = input('\033[0m[\033[95;1m*\033[0m] What rank? : \033[1;77m')
print (number1 ** number2)
