#!/usr/bin/bash
# Tools Aritmatika
# Coded by Senja
# Github: github.com/thesixtynine/Mathematics

checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
    printf "\e[1;77mPlease, run this program as root!\n\e[0m"
    exit 1
fi

}

checktor() {

check=$(curl --socks5-hostname localhost:9050 -s https://www.google.com > /dev/null; echo $?)

if [[ "$check" -gt 0 ]]; then
    printf "\e[1;77mPlease, check your TOR Connection! Just type \"tor\" or \"service tor start\"\n\e[0m"
    exit 1

fi

}

clearscreen() {

clear
reset
sleep 1

}

dependencies() {

command -v nano > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v python > /dev/null 2>&1 || { echo >&2 "I require wget but it's not installed. Install it. Aborting."; exit 1; }

}

banner() {

printf '\e[1;77m
      __  ___     __  __                  __  _
     /  |/  /__ _/ /_/ /  ___ __ _  ___ _/ /_(_)______
    / /|_/ / _ `/ __/ _ \/ -_)  ` \/ _ `/ __/ / __(_-<
   /_/  /_/\_,_/\__/_//_/\__/_/_/_/\_,_/\__/_/\__/___/

'

}

template() {

echo
printf "\e[0m[\e[94;1m#\e[0m] Tools Aritmatika\n"
printf "\e[0m[\e[93;1m*\e[0m] Coded by Senja\n"
printf "\e[0m[\e[96;1m#\e[0m] My Github: @thesixtynine\n"
sleep 1
echo

}

menu() {

printf "\e[0m[\e[92;1m1\e[0m] \e[77;1mPertambahan\n";
printf "\e[0m[\e[92;1m2\e[0m] \e[77;1mPengurangan\n";
printf "\e[0m[\e[92;1m3\e[0m] \e[77;1mPerkalian\n";
printf "\e[0m[\e[92;1m4\e[0m] \e[77;1mPembagian\n";
printf "\e[0m[\e[92;1m5\e[0m] \e[77;1mPemangkatan\n";
printf "\e[0m[\e[92;1mQ\e[0m] \e[77;1mQuotes\n";
printf "\e[0m[\e[92;1m0\e[0m] \e[77;1mExit\n";

read -p $'\n\e[0m[\e[1;95m/\e[0m\e[0m] \e[1;77mSelect an option: \e[0m' option;

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

Q) python text.py
exit

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
#checktor
#dependencies
clearscreen
banner
template
menu
