import ctypes
import win32gui
import win32con
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from subprocess import Popen, call
from random import choice, uniform
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from os import listdir
from io import BytesIO
import win32clipboard
from PIL import Image

dolphin_path = open('./config/dolphin-path.txt','r').read()
service = Service(executable_path='./chromedriver-win-x64.exe')
chrome_options = Options()
profiles  =  open('./config/dolphin-profiles.txt','r').read().splitlines()
ports = open('./config/ports.txt','r').read().splitlines()

def setWindow():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    terminal_handle = user32.FindWindowW(None, u'C:\\Windows\\system32\\cmd.exe')
    user32.ShowWindow(terminal_handle, 6)
    user32.ShowWindow(terminal_handle, 9)
    user32.MoveWindow(terminal_handle, 0, 932, 1920, 104, True)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 932, 1920, 104, 0)

def dolphinStart():
    Popen(dolphin_path)
    sleep(15)
    print(Fore.GREEN+'Dolphin Anty started.'+Style.RESET_ALL)

def dolphinKill():
    call(f'TASKKILL /F /IM "Dolphin Anty.exe"')
    print(Fore.GREEN+'Dolphin Anty closed.'+Style.RESET_ALL)

def startProfiles():
    with open('./config/ports.txt','w') as f: f.write('')
    for i in range(len(profiles)):
        api_request = requests.get(f'http://localhost:3001/v1.0/browser_profiles/{profiles[i]}/start?automation=1').text
        port = api_request.replace('{"success":true,"automation":{"port":','')[:5]
        if port == '{"suc' or port == '{"err':
            print(Fore.RED+f'Connection error in the ID: {profiles[i]}'+Style.RESET_ALL)
        with open('./config/ports.txt','a') as f: f.write(port+'\n'), f.close()
    print(Fore.GREEN+'Profiles started.'+Style.RESET_ALL)

def closeProfiles():
    for i in range(len(profiles)):
        requests.get(f'http://localhost:3001/v1.0/browser_profiles/{profiles[i]}/stop')
    print(Fore.GREEN+'Profiles closed.'+Style.RESET_ALL)

def twitterFollowBot():
    for _ in range(choice([1,2])):
        for i in range(len(profiles)):
            if ports[i] == '{"suc' or ports[i] == '{"err':
                print(Fore.RED+f'The actions could not be executed on the profile with ID: {profiles[i]}'+Style.RESET_ALL)
            else:
                chrome_options.add_experimental_option('debuggerAddress',f'localhost:{ports[i]}')
                browser = webdriver.Chrome(service=service,options=chrome_options)
                wait = WebDriverWait(browser, 1000)
                browser.get(f'https://twitter.com/{choice(open('./config/prompts/twitter-followbot-prompts.txt','r').read().splitlines())}/followers')
                sleep(uniform(3,4))
                wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Follow"]')))
                try:
                    for _ in range(choice([2,3,4])):
                        browser.find_element('xpath', '//span[text()="Follow"]').click()
                        print(Fore.GREEN+f'Profile: {profiles[i]} has followed a user.'+Style.RESET_ALL)
                        sleep(uniform(0.5,2))
                except:
                    print(Fore.RED+f'An error has occurred in the ID: {profiles[i]}'+Style.RESET_ALL)
    print(Fore.GREEN+'Twitter Followbot completed.'+Style.RESET_ALL)

def twitterMgFarmer():
    for _ in range(choice([1,2])):
        for i in range(len(profiles)):
            if ports[i] == '{"suc' or ports[i] == '{"err':
                print(Fore.RED+f'The actions could not be executed on the profile with ID: {profiles[i]}'+Style.RESET_ALL)
            else:
                chrome_options.add_experimental_option('debuggerAddress',f'localhost:{ports[i]}')
                browser = webdriver.Chrome(service=service,options=chrome_options)
                wait = WebDriverWait(browser, 1000)
                browser.get(f'https://twitter.com/search?q={choice(open('./config/prompts/twitter-mg-farmer-prompts.txt','r').read().splitlines())}&src=typed_query&f=live')
                sleep(uniform(3,4))
                wait.until(EC.element_to_be_clickable(('xpath', '//div[@data-testid="like"]')))
                try:
                    for _ in range(choice([1,2,3])):
                        browser.find_element('xpath', '//div[@data-testid="like"]').click()
                        print(Fore.GREEN+f'Profile: {profiles[i]} has given a like.'+Style.RESET_ALL)
                        sleep(uniform(0.5,2))
                except:
                    print(Fore.RED+f'An error has occurred in the ID: {profiles[i]}'+Style.RESET_ALL)
    print(Fore.GREEN+'Twitter MG Farmer completed.'+Style.RESET_ALL)

def twitterUnfollowBot(all=False):
    for i in range(len(profiles)):
        if ports[i] == '{"suc' or ports[i] == '{"err':
            print(Fore.RED+f'The actions could not be executed on the profile with ID: {profiles[i]}'+Style.RESET_ALL)
        else: 
            chrome_options.add_experimental_option('debuggerAddress',f'localhost:{ports[i]}')
            browser = webdriver.Chrome(service=service,options=chrome_options)
            wait = WebDriverWait(browser, 1000)
            browser.get('https://twitter.com/home')
            sleep(uniform(3,4))
            wait.until(EC.element_to_be_clickable(('xpath', '//a[@aria-label="Profile"]')))
            elem = browser.find_element('xpath', '//a[@aria-label="Profile"]')
            user = elem.get_attribute('href').replace('https://twitter.com/','')
            browser.get(f'https://twitter.com/{user}/following')
            sleep(uniform(3,4))
            wait.until(EC.element_to_be_clickable(('xpath','//div[@class="css-175oi2r r-1awozwy r-18u37iz r-1wbh5a2"]')))
            elems = browser.find_elements('xpath','//div[@class="css-175oi2r r-1awozwy r-18u37iz r-1wbh5a2"]')
            elems1 = browser.find_elements('xpath','//span[text()="Following"]')
            r = 0
            for elem in elems:
                if r == 0:
                    pass
                else:
                    if all == False:
                        if "Follows you" in elem.text:
                            with open('./config/userscrap.txt','w') as f: f.write(elem.text.replace('Follows you',''))
                            e=open('./config/userscrap.txt','r').read().splitlines()
                            print(Fore.RED+f'{e[0]} follows {profiles[i]}. We do not stop following him/her.'+Style.RESET_ALL)
                            sleep(.5)
                        else:
                            try:
                                wait.until(EC.element_to_be_clickable(('xpath','//span[text()="Following"]')))
                                elems1[r].click()
                                wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Unfollow"]')))
                                browser.find_element('xpath', '//span[text()="Unfollow"]').click()
                                print(Fore.GREEN+f'{profiles[i]} has stopped following {elem.text}.'+Style.RESET_ALL)
                                sleep(uniform(1,2))
                            except:
                                pass
                    if all == True:
                        try:
                            with open('./config/userscrap.txt','w') as f: f.write(elem.text.replace('Follows you',''))
                            e=open('./config/userscrap.txt','r').read().splitlines()
                            wait.until(EC.element_to_be_clickable(('xpath','//span[text()="Following"]')))
                            elems1[r].click()
                            wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Unfollow"]')))
                            browser.find_element('xpath', '//span[text()="Unfollow"]').click()
                            print(Fore.GREEN+f'{profiles[i]} has stopped following {e[0]}.'+Style.RESET_ALL)
                            sleep(uniform(1,2))
                        except:
                            pass
                r += 1
    print(Fore.GREEN+'Twitter UnfollowBot completed.'+Style.RESET_ALL)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def twitterScheduler(margindays, hour, minutes):   
    for i in range(len(profiles)):
        if ports[i] == '{"suc' or ports[i] == '{"err':
            print(Fore.RED+f'The actions could not be executed on the profile with ID: {profiles[i]}'+Style.RESET_ALL)
        else:
            actualyear = datetime.today().year
            actualmonth = datetime.today().month
            actualday = datetime.today().day
            picspath = open('./config/pics-path.txt', 'r').read().splitlines()[i] 
            pics = listdir(picspath)
            d = actualday
            m = actualmonth
            y = actualyear
            for pic in pics:
                picsreg = open(f'./config/reg/pics/{profiles[i]}.txt','r').read().splitlines()
                if pic not in picsreg:
                    print(Fore.GREEN+f'Scheduling for the date: {d}/{m}/{y} the picture: "{pic}" in the profile: {profiles[i]}'+Style.RESET_ALL)
                    sleep(1)
                    r=0
                    while True:
                        tweetsreg = open(f'./config/reg/tweets/{profiles[i]}.txt','r').read().splitlines()
                        tweet = choice(open('./config/tweets-texts.txt','r').read().splitlines())
                        if tweet not in tweetsreg:
                            print(Fore.GREEN+f'The tweet text: "{tweet}" has not been used in the profile: {profiles[i]}, the script can continue...'+Style.RESET_ALL)
                            with open(f'./config/reg/tweets/{profiles[i]}.txt','a') as f: f.write(tweet+'\n'), f.close()
                            with open(f'./config/reg/pics/{profiles[i]}.txt','a') as f: f.write(pic+'\n'), f.close()
                            break
                        if r > len(open('./config/tweets-texts.txt','r').read().splitlines()):
                            print(Fore.RED+f'Profile: {profiles[i]} has used all available text tweets.'+Style.RESET_ALL)
                            sleep(3)
                            break
                        else:
                            print(Fore.RED+f'The tweet text: "{tweet}" has already been used in the profile: {profiles[i]}'+Style.RESET_ALL)
                            sleep(.5)
                            r+=1
                    if r < len(open('./config/tweets-texts.txt','r').read().splitlines()): 
                        d += margindays
                        if m == 1:
                            if d >= 31:
                                d = 1
                                m = 2
                        if m == 2:
                            if d >= 29:
                                d = 1
                                m = 3                
                        if m == 3:
                            if d >= 31:
                                d = 1
                                m = 4                                   
                        if m == 4:                   
                            if d >= 30:
                                d = 1
                                m = 5                        
                        if m == 5:                   
                            if d >= 31:
                                d = 1
                                m = 6                       
                        if m == 6:                  
                            if d >= 30:
                                d = 1
                                m = 7                    
                        if m == 7:                
                            if d >= 31:
                                d = 1
                                m = 8           
                        if m == 8:                   
                            if d >= 31:
                                d = 1
                                m = 9                       
                        if m == 9:                   
                            if d >= 30:
                                d = 1
                                m = 10           
                        if m == 10:            
                            if d >= 31:
                                d = 1
                                m = 11
                        if m == 11:
                            if d >= 30:
                                d = 1
                                m = 12
                        if m == 12:
                            if d >= 31:
                                d = 1
                                m = 1
                                y += 1
                        chrome_options.add_experimental_option('debuggerAddress',f'localhost:{ports[i]}')
                        browser = webdriver.Chrome(service=service,options=chrome_options)
                        wait = WebDriverWait(browser, 1000)
                        browser.get('https://twitter.com/compose/tweet/schedule')
                        sleep(uniform(3,4))
                        wait.until(EC.element_to_be_clickable(('xpath', f'//select[@aria-labelledby="SELECTOR_1_LABEL"]//option[@value="{m}"]')))
                        browser.find_element('xpath', f'//select[@aria-labelledby="SELECTOR_1_LABEL"]//option[@value="{m}"]').click()
                        wait.until(EC.element_to_be_clickable(('xpath', f'//select[@aria-labelledby="SELECTOR_2_LABEL"]//option[@value="{d}"]')))
                        browser.find_element('xpath', f'//select[@aria-labelledby="SELECTOR_2_LABEL"]//option[@value="{d}"]').click()
                        wait.until(EC.element_to_be_clickable(('xpath', f'//select[@aria-labelledby="SELECTOR_3_LABEL"]//option[@value="{y}"]')))
                        browser.find_element('xpath', f'//select[@aria-labelledby="SELECTOR_3_LABEL"]//option[@value="{y}"]').click()
                        wait.until(EC.element_to_be_clickable(('xpath', f'//select[@aria-labelledby="SELECTOR_4_LABEL"]//option[@value="{hour}"]')))
                        browser.find_element('xpath', f'//select[@aria-labelledby="SELECTOR_4_LABEL"]//option[@value="{hour}"]').click()
                        wait.until(EC.element_to_be_clickable(('xpath', f'//select[@aria-labelledby="SELECTOR_5_LABEL"]//option[@value="{minutes}"]')))
                        browser.find_element('xpath', f'//select[@aria-labelledby="SELECTOR_5_LABEL"]//option[@value="{minutes}"]').click()
                        wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Confirm"]')))
                        browser.find_element('xpath', '//span[text()="Confirm"]').click()
                        sleep(uniform(1,2))
                        wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Post"]')))
                        browser.find_element('xpath', '//span[text()="Post"]').click()
                        sleep(uniform(1,2))    
                        browser.find_element('xpath', '//div[@role="textbox"]').send_keys(tweet)
                        sleep(uniform(1,2))
                        image = Image.open(f'{picspath}\\{pic}')
                        output = BytesIO()
                        image.convert("RGB").save(output, "BMP")
                        data = output.getvalue()[14:]
                        output.close()
                        send_to_clipboard(win32clipboard.CF_DIB, data)
                        browser.find_element('xpath', '//div[@role="textbox"]').send_keys(Keys.CONTROL + "v")
                        sleep(uniform(8,11))
                        wait.until(EC.element_to_be_clickable(('xpath', '//span[text()="Schedule"]')))
                        browser.find_element('xpath', '//span[text()="Schedule"]').click()
                        print(Fore.GREEN+f'Scheduled post in profile: {profiles[i]}'+Style.RESET_ALL), sleep(1)
                        sleep(uniform(1,2))
                    else:
                        break       
                else: 
                    print(Fore.RED+f'The picture: "{pic}" has already been used in the profile: {profiles[i]}'+Style.RESET_ALL)
                    sleep(.1)
    print(Fore.GREEN+'Twitter Scheduler completed.'+Style.RESET_ALL)
