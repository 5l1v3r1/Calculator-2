#!/usr/bin/python
# -*- coding: utf-8 -*-
# Calculator
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Calculator

import os, sys, time, random
from time import sleep

info = """
Nama        : Calculator
Versi       : 3.1 (Update: 15 September 2020, 3:00 AM)
Tanggal     : 05 Maret 2019
Author      : Nedi Senja
Tujuan      : Sengaja di encrypt
              biar bada giat belajar
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;46;90;1m[         Calculator, My Github: @stepbystepexe          ]\033[0m"""

logo = """
\033[0;32m█▀▀▀▀ █▀▀▀█ █     █▀▀▀▀ █   █ \033[0;37m█    █▀▀▀█ ▀▀█▀▀ █▀▀▀█ █▀▀▀▄
\033[0;32m█     █▀▀▀█ █     █     █   █ \033[0;37m█    █▀▀▀█   █   █   █ █▀▀▀▄
\033[0;32m▀▀▀▀▀ ▀   ▀ ▀▀▀▀▀ ▀▀▀▀▀ ▀▀▀▀▀ \033[0;37m▀▀▀▀ ▀   ▀   ▀   ▀▀▀▀▀ ▀   ▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def home():
    os.system('clear')
    os.system('reset')
    time.sleep(1)
    print
    print(logo)
    print(example)
    print
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mSaya tidak real kalo code program saya ini ditiru")
    write("         Seburuk apaun itu tolong hargai karya milik orang\033[0m\n")

def pembagian():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    home()
    number1 = input('\n\033[0m[\033[41;77;1m Nominal \033[0m] ')
    number2 = input('\033[0m[\033[44;77;1m Di Bagi \033[0m] ')
    print
    print('\033[0m[\033[43;90;1m  Hasil  \033[0m]\033[0m'),(number1 / number2)
    print
    raw_input('[ Tekan Enter ]')
    restart()

def perkalian():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    home()
    number1 = input('\n\033[0m[\033[41;77;1m Nominal \033[0m] ')
    number2 = input('\033[0m[\033[44;77;1m Di Kali \033[0m] ')
    print
    print('\033[0m[\033[43;90;1m  Hasil  \033[0m]\033[0m'),(number1 * number2)
    print
    raw_input('[ Tekan Enter ]')
    restart()

def pengurangan():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    home()
    number1 = input('\n\033[0m[\033[41;77;1m Nominal \033[0m] ')
    number2 = input('\033[0m[\033[44;77;1m Kurangi \033[0m] ')
    print
    print('\033[0m[\033[43;90;1m  Hasil  \033[0m]\033[0m'),(number1 - number2)
    print
    raw_input('[ Tekan Enter ]')
    restart()

def pemangkatan():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    home()
    number1 = input('\n\033[0m[\033[41;77;1m Nominal \033[0m] ')
    number2 = input('\033[0m[\033[44;77;1m Pangkat \033[0m] ')
    print
    print('\033[0m[\033[43;90;1m  Hasil  \033[0m]\033[0m'),(number1 ** number2)
    print
    raw_input('[ Tekan Enter ]')
    restart()

def penjumlahan():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    home()
    number1 = input('\n\033[0m[\033[41;77;1m Nominal \033[0m] ')
    number2 = input('\033[0m[\033[44;77;1m Jummlah \033[0m] ')
    print
    print('\033[0m[\033[43;90;1m  Hasil  \033[0m]\033[0m'),(number1 + number2)
    print
    raw_input('[ Tekan Enter ]')
    restart()

os.system('clear')
os.system('reset')
sleep(1)
print
print(logo)
print(example)
print
print("\033[0m[\033[96;2;1m1\033[0m] \033[1;77mPembagian")
print("\033[0m[\033[96;2;1m2\033[0m] \033[1;77mPerkalian")
print("\033[0m[\033[96;2;1m3\033[0m] \033[1;77mPengurangan")
print("\033[0m[\033[96;2;1m4\033[0m] \033[1;77mPemangkatan")
print("\033[0m[\033[96;2;1m5\033[0m] \033[1;77mPenjumlahan")
print
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print
option = raw_input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option == '01' or option == '1':
    pembagian()
elif option == '02' or option == '2':
    perkalian()
elif option == '03' or option == '3':
    pengurangan()
elif option == '04' or option == '4':
    pemangkatan()
elif option == '05' or option == '5':
    penjumlahan()
elif option.strip() in '& 6 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 7 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Calculator')
    print(info)
    sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 8 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    sleep(1)
    restart()
