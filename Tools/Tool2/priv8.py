import os,requests,re,time
from colorama import init,Fore
from multiprocessing.dummy import Pool

class settings:
	green = Fore.GREEN
	red = Fore.RED
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	googleurls = {"https://www.google.com/search?q=[dork]&num=100&start=0",
	              "https://www.google.com/search?q=[dork]&num=100&start=100",
	              "https://www.google.com/search?q=[dork]&num=100&start=200"}


def scan(dork):
	for googleurl in settings.googleurls:
		try:
			googleurl = googleurl.replace("[dork]",dork)
			r = requests.get(googleurl,headers=settings.headers,timeout=10)
			if '<div id="recaptcha"' in r.text:
				print("[!] Google Captcha! Change your IP and wait!")
				time.sleep(15)
			else:
				sites = re.findall('<div class="r"><a href="(.*?)" ping="/url?',r.text)
				for site in sites:
					site = site.replace("http://","protocol1")
					site = site.replace("https://","protocol2")
					site = site + cutstring
					site = site[:site.find(cutstring)+0]
					site = site.replace("protocol1","http://")
					site = site.replace("protocol2","https://")
					print(site)
					with open("grabbedtest.txt","a") as f:
						f.write(site + "\n")
				lines_seen = set()
				outfile = open('grabbed.txt', "a")
				infile = open('grabbedtest.txt', "r")
				for line in infile:
					if line not in lines_seen:
						outfile.write(line)
						lines_seen.add(line)
				outfile.close()
				infile.close()
				if os.name == "nt":
					os.system("del grabbedtest.txt")
				else:
					os.system("rm -rf grabbedtest.txt")							
		except:
			pass


init(convert=True)

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

banner = """
{}

  ______                      _       _     ____            _      __      __  __   ____  
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | |___ \ 
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | |   __) |
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | |  |__ < 
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |  ___) |
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_| |____/ 
                                                                                          
                                                                                          

 [{}+{}] BestGoogleDorker Priv8 Tool
 [{}+{}] Author : Viper 1337
 [{}+{}] My Facebook : fb.me/viper1337official/

"""

print(banner.format(settings.green,settings.red,settings.green,settings.red,settings.green,settings.red,settings.green)) 

dorklist = raw_input("{}\n[{}*{}] Dorklist : ".format(settings.green,settings.red,settings.green))
cutstring = raw_input("{}\n[{}*{}] Cut string : ".format(settings.green,settings.red,settings.green))
print()

try:
	dorks = open(dorklist,"r").read().splitlines()
	pp = Pool(1)
	pr = pp.map(scan,dorks)
except:
	print("{}[{}-{}] Error open files! Try again!".format(settings.red,settings.green,settings.red))
                                     
