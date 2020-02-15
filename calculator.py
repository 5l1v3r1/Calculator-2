#!/usr/bin/python
# -*- coding: utf-8 -*-
# Calculator
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Calculator

from __opt__ import *
import os, sys, time, random, marshal

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

example = """\033[0;46;90;1m[     Calculator Terminal, My Githib: @stepbystepexe     ]\033[0m"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def pembagian():
    print
    write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mMengecek ...')
    print
    print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPembagian')
    number1 = input('\033[0m[\033[95;1m/\033[0m] Masukan angka : \033[1;77m')
    number2 = input('\033[0m[\033[95;1m/\033[0m] Ditambah berapa? : \033[1;77m')
    print
    print (number1 / number2)
    print
    raw_input('[ \033[92;1mKembali \033[0;77;1m]')
    restart()

def perkalian():
    print
    write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mMengecek ...')
    print
    print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPerkalian')
    number1 = input('\033[0m[\033[95;1mx\033[0m] Masukan angka : \033[1;77m')
    number2 = input('\033[0m[\033[95;1mx\033[0m] Dikali berapa? : \033[1;77m')
    print
    print (number1 * number2)
    print
    raw_input('[ \033[92;1mKembali \033[0;77;1m]')
    restart()

def pengurangan():
    print
    write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mMengecek ...')
    print
    print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPengurangan')
    number1 = input('\033[0m[\033[95;1m-\033[0m] Masukan angka : \033[1;77m')
    number2 = input('\033[0m[\033[95;1m-\033[0m] Dikurangi berapa? : \033[1;77m')
    print
    print (number1 - number2)
    print
    raw_input('[ \033[92;1mKembali \033[0;77;1m]')
    restart()

def pemangkatan():
    print
    write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mMengecek ...')
    print
    print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPemangkatan')
    number1 = input('\033[0m[\033[95;1m*\033[0m] Masukan angka : \033[1;77m')
    number2 = input('\033[0m[\033[95;1m*\033[0m] Dipangkat berapa? : \033[1;77m')
    print
    print (number1 ** number2)
    print
    raw_input('[ \033[92;1mKembali \033[0;77;1m]')
    restart()

def penjumlahan():
    print
    write ('\033[0m[\033[91;1m!\033[0m] \033[1;77mMengecek ...')
    print
    print ('\033[0m[\033[96;1m#\033[0m] \033[1;77mPertambahan')
    number1 = input('\033[0m[\033[95;1m+\033[0m] Masukan angka : \033[1;77m')
    number2 = input('\033[0m[\033[95;1m+\033[0m] Ditambah berapa? : \033[1;77m')
    print
    print (number1 + number2)
    print
    raw_input('[ \033[92;1mKembali \033[0;77;1m]')
    restart()

os.system('clear')
os.system('reset')
time.sleep(1)
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
option = raw_input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
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
elif option.strip() in '& 2 lisensi'.split():
    print
    os.system('nano LICENSE')
    print
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Calculator')
    print(info)
    time.sleep(1)
    print
    raw_input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print
    os.system('git pull origin master')
    print
    raw_input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print
    time.sleep(1)
    restart()
