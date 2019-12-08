#!/usr/bin/bash
# Calculator in Terminal
# Coded by Senja
# Github: github.com/stepbystepexe/Calculator

checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
    printf "\e[0m[\e[1;91m!\e[0m] \e[1;77mPlease, run this program as root!\n\n\e[0m"
    exit 1
fi

}

clearscreen() {

clear
reset
sleep 1

}

dependencies() {

command -v bash > /dev/null 2>&1 || { echo >&2 "I require bash but it's not installed. Install it. Aborting."; exit 1; }
command -v python2 > /dev/null 2>&1 || { echo >&2 "I require python2 but it's not installed. Install it. Aborting."; exit 1; }

}

banner() {

printf "

        \e[0;32m█▀▀ █▀█ █   █▀▀ █ █ \e[0;37m█   █▀█ ▀█▀ █▀█ █▀▀
        \e[0;32m█   █▀█ █   █   █ █ \e[0;37m█   █▀█  █  █ █ █
        \e[0;32m▀▀▀ ▀ ▀ ▀▀▀ ▀▀▀ ▀▀▀ \e[0;37m▀▀▀ ▀ ▀  ▀  ▀▀▀ ▀
"

}

template() {

echo
printf "\e[0;46;90;1m:      Calculator Terminal v1.0, Coded by @stepbystep    :\e[0m\n"
sleep 1
echo

}

menu() {

printf "\e[0m[\e[91;1m1\e[0m] \e[77;1mPertambahan\n";
printf "\e[0m[\e[92;1m2\e[0m] \e[77;1mPengurangan\n";
printf "\e[0m[\e[93;1m3\e[0m] \e[77;1mPerkalian\n";
printf "\e[0m[\e[94;1m4\e[0m] \e[77;1mPembagian\n";
printf "\e[0m[\e[96;1m5\e[0m] \e[77;1mPemangkatan\n";
printf "\e[0m[\e[97;1m0\e[0m] \e[77;1mExit\n";

read -p $'\n\n\e[0m[\e[1;95m/\e[0m\e[0m] \e[1;77mSelect an option: \e[0m' option;

case $option in

1) python2 tambah.py

;;

2) python2 kurang.py

;;

3) python2 kali.py

;;

4) python2 bagi.py

;;

5) python2 pangkat.py

;;

0) printf "\n\e[0m[\033[91;1m!\e[0m] \e[1;77mExit the program!\n\n"
exit 1

;;

*) printf "\n\e[0m[\033[91;1m!\e[0m] \e[1;77mInvalid option!\n"
sleep 1
clearscreen
banner
template
menu
esac

}

#checkroot
#dependencies
clearscreen
banner
template
menu
