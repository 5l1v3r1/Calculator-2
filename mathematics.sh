#!/usr/bin/shell
# Tools Mathematics
# Coded by Senja
# Github: github.com/thesixtynine/Mathematics

clear
reset
sleep 1

printf '\033[1;77m
      __  ___     __  __                  __  _
     /  |/  /__ _/ /_/ /  ___ __ _  ___ _/ /_(_)______
    / /|_/ / _ `/ __/ _ \/ -_)  ` \/ _ `/ __/ / __(_-<
   /_/  /_/\_,_/\__/_//_/\__/_/_/_/\_,_/\__/_/\__/___/

\033[0;37;45m ○● 千尺丨乇几ᗪ丂 ㄒ卄乇 Ꮆ尺卂ㄚ 卄卂ㄒ 爪ㄚ ㄒ乇卂爪 ●○ \033[0m


'

sleep 1
echo "\033[0m[\033[94;1m#\033[0m] \033[0mTools Aritmatika"
echo "\033[0m[\033[93;1m*\033[0m] \033[0mCoded by Senja"
echo "\033[0m[\033[96;1m#\033[0m] \033[0mMy Github: @thesixtynine"
sleep 1
echo
echo
echo "\033[0m[\033[92;1m1\033[0m] \033[77;1mPertambahan";
echo "\033[0m[\033[92;1m2\033[0m] \033[77;1mPengurangan";
echo "\033[0m[\033[92;1m3\033[0m] \033[77;1mPerkalian";
echo "\033[0m[\033[92;1m4\033[0m] \033[77;1mPembagian";
echo "\033[0m[\033[92;1m5\033[0m] \033[77;1mPemangkatan";
echo "\033[0m[\033[92;1m0\033[0m] \033[77;1mExit";
echo

read -p "[/] Select option : " choice;

case $choice in

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

0) exit 1

*) echo "\033[0m[\033[91;1m!\033[0m] \033[1;77mInvalid option"
esac
