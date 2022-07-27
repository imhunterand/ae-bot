import os,sys,re
import requests
import ssl
import socket
import httplib
import urllib2
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[36m'
purple = '\033[35m'
reset = '\033[0m'
#initialize OS for display clear
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass
print(red+"""

  ______                      _       _     ____            _      __      __  __   ____  
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | |___ \ 
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | |   __) |
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | |  |__ < 
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |  ___) |
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_| |____/ 
                                                                                          
    ICQ: 744289868                                                                                      

""")
print(yellow+"""_______________________________
< Mass cPanel Reset Password Checker  >
 -------------------------------""")
print(blue+"Author By Viper 1337"+reset)
def error():
	try:
		requests.post('http://www.google.com')
		open(sys.argv[1], 'rb')
	except requests.exceptions.ConnectionError:
		print(red+"[ - ]"+reset+" Tidak Ada Koneksi Internet")
		exit()
	except IOError:
		print(red+"[ - ]"+reset+" File Tidak Di Temukan!")
		exit()
	except IndexError:
		print(red+"[ - ]"+reset+" Usage : python2 file.py list.txt")
		exit()
error()
def main(url):
	try:
		urls = url.replace('cpanel/','cpanel').replace('cpanel','cpanel/').strip()
		req = urllib2.Request(urls, headers={'User-Agent': 'Mozilla/5.0'})
		sites = urllib2.urlopen(req,timeout=6)
		regex = re.findall('(?=://)(.*?\d)(?=/")', sites.read())
		for url in regex:
			find = urllib2.urlopen('http'+url,timeout=6)
			if 'Reset Password' in find.read():
				print(urls+green+' --> Active'+reset)
				with open('active.txt','ab') as active:
					active.write(urls+'\n')
					active.close()
			else:
				print(urls+red+' --> Disable'+reset)
			pass
	except(urllib2.URLError,ssl.CertificateError,socket.error,httplib.InvalidURL):
			print(urls+yellow+' --> Cpanel Not Found'+reset)
	except ValueError:
		pass
pass

lists = open(sys.argv[1], 'rb').read().splitlines()
t = ThreadPool(250)
t.map(main, lists)
t.close()
t.join()

if __name__ == '__main__': 
 
    print("Site cPanel Active :"+green+" active.txt")
    print(blue+""+reset)
