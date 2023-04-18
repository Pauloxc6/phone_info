#!/usr/bin/python3
# -*- coding=utf-8 -*-
#-------------------------------------------------------------------------------------------------------------------------------------
import os
import time
import socket
import pyfiglet
import phonenumbers
from getmac import get_mac_address as gma
from phonenumbers import geocoder
from phonenumbers import carrier
from datetime import datetime

#--------------------------------------------------------------------------------------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
#-------------------------------------------------------------------------------------------------------------------------------------

os.system("clear")
print('\033[93m')
os.system("pyfiglet Phone SEC")
print()
print()
print('\033[94m')
print('-' * 60)
print("Author    : Paulo Cezar")
print("github    : https://github.com/Pauloxc6")
print("Instagram : https://instagram.com/pauloxc6")
print()
print("Localhost     : ", socket.gethostbyname(socket.gethostname()))
print("PRIVATE IP    : ", s.getsockname()[0])
print("MAC ADDRESS   : ", gma())
print()
print('Scanning started at: ' + str(datetime.now()))
print('-' * 60)
print()

#-------------------------------------------------------------------------------------------------------------------------------------

try:

    def menu():

        print('\033[96m')
        print("Escolha uma opção:")
        print("1. Start")
        print("2. Exit")

#-------------------------------------------------------------------------------------------------------------------------------------

    def phone():

        os.system('clear')
        print("\033[91m")
        os.system("clear")
        os.system("pyfiglet Input Number")
        print()
        print("\033[95m")
        print('Ex: {Country Code}{DDD}9XXXXYYYY')
        print('Ex: +5531912345678')
        number = input("Phone Number: ")

#-------------------------------------------------------------------------------------------------------------------------------------

        os.system("clear")
        print("\033[96m")
        os.system("pyfiglet Attack Starting")
        print("\033[92m")
        print("[                    ] 0% ")
        time.sleep(5)
        print("[=====               ] 25%")
        time.sleep(5)
        print("[==========          ] 50%")
        time.sleep(5)
        print("[===============     ] 75%")
        time.sleep(5)
        print("[====================] 100%")
        time.sleep(3)

#-------------------------------------------------------------------------------------------------------------------------------------

        os.system("clear")
        number_n = phonenumbers.parse(number, None)
        local = geocoder.description_for_number(number_n, "CH")
        number_f = number
        number_fa = phonenumbers.parse(number_f)
        number_fi = phonenumbers.format_number(number_fa, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        number_fn = phonenumbers.format_number(number_fa, phonenumbers.PhoneNumberFormat.NATIONAL)
        number_fe = phonenumbers.format_number(number_fa, phonenumbers.PhoneNumberFormat.E164)
        ca = carrier.name_for_number(number_n, "en")

#-------------------------------------------------------------------------------------------------------------------------------------

        print("\033[91m")
        os.system("pyfiglet Information Number")
        print("\033[90m")
        print('-' * 60)
        print(number_n)
        print('LOCAL: ', local)
        print('FORMAT-INTERNATIONAL: ', number_fi)
        print('FORMAT-NATIONAL: ', number_fn)
        print('FORMAT-E164: ', number_fe)
        print('CARRIER: ', ca)
        print('-' * 60)

        print("\033[0m")
        exit()

#-------------------------------------------------------------------------------------------------------------------------------------

    while True:
         try:
            if __name__ == '__main__':
                menu()
                cmd = input('Command: ')

                if cmd == '1':
                   phone()

                if cmd == '2':
                    os.system('clear')
                    exit()

         except ValueError:
            print('\nValor digitado inválido. Digite um número inteiro de 1 a 2!\n')

except Exception as error:
    print('Error: ', error)
#-------------------------------------------------------------------------------------------------------------------------------------
