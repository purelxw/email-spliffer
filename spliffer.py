import os, sys, time, getpass, smtplib, colorama

from colorama import Fore

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(f'''{Fore.RESET}



{Fore.LIGHTBLACK_EX}     ┌─┐┌┬┐┌─┐┬┬    {Fore.LIGHTGREEN_EX}┌─┐┌─┐┬  ┬┌─┐┌─┐┌─┐┬─┐
{Fore.LIGHTBLACK_EX}     ├┤ │││├─┤││    {Fore.LIGHTGREEN_EX}└─┐├─┘│  │├┤ ├┤ ├┤ ├┬┘
{Fore.LIGHTBLACK_EX}     └─┘┴ ┴┴ ┴┴┴─┘  {Fore.LIGHTGREEN_EX}└─┘┴  ┴─┘┴└  └  └─┘┴└─ {Fore.LIGHTBLACK_EX} made by purelxw
    
{Fore.LIGHTWHITE_EX}   - make sure your gmail has less secure apps on (https://myaccount.google.com/lesssecureapps)
{Fore.LIGHTWHITE_EX}   - https://github.com/purelxw
    '''+Fore.RESET)

else:
    sys.exit('Usage: python spliffer.py')
    os.system("clear || cls")

print("")
print("")
print("")
spamemail = input(f"{Fore.LIGHTBLACK_EX} Enter spammer's gmail address: "f"{Fore.LIGHTBLUE_EX}")
spampassword = getpass.getpass(f"{Fore.LIGHTBLACK_EX} Enter spammer's password (will not show on console): "f"{Fore.LIGHTBLUE_EX}")

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

try:
    email.login(spamemail, spampassword)
except smtplib.SMTPAuthenticationError:
    print("")
    print(f"{Fore.RED} The gmail or password might be wrong")
    print(f"{Fore.RED} OR You maybe haven't switched on less secure apps (https://myaccount.google.com/lesssecureapps)")
    print(f"{Fore.RED} Closing in 5 seconds...")
    time.sleep(5)
    exit()

print("")
print(f"{Fore.GREEN} Gmail and password is correct, less secure apps is enabled")
print("")
victimemail = input(f"{Fore.LIGHTBLACK_EX} Enter victim's email address: "f"{Fore.LIGHTBLUE_EX}")
message = input(f"{Fore.LIGHTBLACK_EX} Enter the message you want to send: "f"{Fore.LIGHTBLUE_EX}")
number = int(input(f"{Fore.LIGHTBLACK_EX} Enter how many times you want to send this message: "f"{Fore.LIGHTBLUE_EX}"))

print("")
print(f"{Fore.LIGHTBLACK_EX} Checking Information...")
time.sleep(2.5)
print(f"{Fore.GREEN} Information is correct!")
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
    print(f"{Fore.GREEN} Rolling spliff... \n")
    while i < number:
        i+=1
        server.sendmail(spamemail,victimemail,message)
        if i == 1:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 2:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 3:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 4:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 5:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 6:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 7:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 8:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 9:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        elif i == 0:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        else:
            print((f'{Fore.MAGENTA}'' [%d] Email sent ')%(i))
        sys.stdout.flush()
    print("")
    print(f"{Fore.GREEN} The email has been put in a spliff")
    print(f"{Fore.GREEN} Closing in 5 seconds...")
    time.sleep(5)
    exit()

except KeyboardInterrupt:
    print("")
    print(f"{Fore.RED} The email has not been put in a spliff")
    print(f"{Fore.RED} Closing in 3 seconds...")
    time.sleep(3)
    exit()
