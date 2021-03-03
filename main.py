import os
import sys
import time
import smtplib
import colorama
import ctypes
from colorama import Fore

ctypes.windll.kernel32.SetConsoleTitleW('email spammer by lozza')
if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(f'''{Fore.RESET}


    Author: lozza
    
   [{Fore.RED}!{Fore.RESET}] Make sure your gmail has less secure apps on (https://myaccount.google.com/lesssecureapps)
    '''+Fore.RESET)

print('')
print('')

spamemail = input(f" [{Fore.RED}?{Fore.RESET}] Enter spammer's gmail address: ")
spampassword = input(f" [{Fore.RED}?{Fore.RESET}] Enter spammer's password: ")

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

try:
    email.login(spamemail, spampassword)
except smtplib.SMTPAuthenticationError:
    print("")
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.RED}The gmail or password might be wrong")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.RED}OR You maybe haven't switched on less secure apps (https://myaccount.google.com/lesssecureapps)")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Closing in 5 seconds...")
    time.sleep(5)
    exit()

print("")
print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN}Gmail and password is correct, less secure apps is enabled")
print("")
victimemail = input(f"{Fore.RESET} [{Fore.RED}?{Fore.RESET}] Enter victim's email address: ")
message = input(f" [{Fore.RED}?{Fore.RESET}] Enter the message you want to send: ")
number = int(input(f" [{Fore.RED}?{Fore.RESET}] Enter how many times you want to send this message: "))

print("")
print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} Information is correct!{Fore.RESET}")
print("")

try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(spamemail,spampassword)
    i = 0
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} Rolling spliff... \n{Fore.RESET}")
    print('')
    while i < number:
        i+=1
        server.sendmail(spamemail,victimemail,message)
        if i == 1:
            print((f' [{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 2:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 3:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 4:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 5:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 6:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 7:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 8:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 9:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        elif i == 0:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}''[%d] Email sent ')%(i))
        else:
            print((f' {Fore.RESET}[{Fore.RED}>{Fore.RESET}] {Fore.GREEN}'' [%d] Email sent ')%(i))
        sys.stdout.flush()
    print("")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] {Fore.GREEN} The email has been put in a spliff")
    print('')
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Closing in 5 seconds...")
    time.sleep(5)
    exit()

except KeyboardInterrupt:
    print("")
    print(f" [{Fore.RED}!{Fore.RESET}] {Fore.GREEN} The email has not been put in a spliff")
    print(f" {Fore.RESET}[{Fore.RED}!{Fore.RESET}] Closing in 3 seconds...")
    time.sleep(3)
    exit()