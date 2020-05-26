import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re


def get_first_comment(u_name):
    url = 'https://9gag.com/u/'+u_name+'/comments'
    driver2 = webdriver.Chrome('C:/Users/saini/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
    driver2.maximize_window()
    driver2.get(url)
    html = driver2.find_element_by_tag_name('html')
    while True:
        html.send_keys(Keys.END)
        kk=driver2.find_element_by_xpath("//a[contains(@class, 'btn end')]")
#         kk2=driver2.find_element_by_xpath("//a[contains(@href, '/hot') and contains(@class, 'btn') ]")
        if kk.is_displayed():
            print ("Element found")
            print(u_name)
            text_list=driver2.find_elements_by_xpath("//article[contains(@id, 'jsid-post')]")
            dayss_rank=rank_analyser(int("".join(re.findall(r'\d+', driver2.find_element_by_xpath("//section[contains(@class, 'profile-header')]").text))))
            comm=('https://9gag.com/gag/'+text_list[-1].get_attribute("id")[10:])
            driver2.close()
            break
    return comm,dayss_rank


def rank_analyser(no_days):
    if(no_days<=69):
        return 'Officer Cadet'
    if(no_days>=69 and no_days<249):
        return '2nd Lieutenant'
    if(no_days>=249 and no_days<419):
        return 'Lieutenant'
    if(no_days>=419 and no_days<634):
        return 'Captain'
    if(no_days>=634 and no_days<809):
        return 'Major'
    if(no_days>=809 and no_days<1000):
        return 'Lt. Colonel'
    if(no_days>=1000 and no_days<1500):
        return 'Colonel'
    if(no_days>=1500 and no_days<1670):
        return 'Brigadier'
    if(no_days>=1670 and no_days<2000):
        return 'Major General'
    if(no_days>=2000 and no_days<2700):
        return 'Lt. General'
    if(no_days>=2700 and no_days<3000):
        return 'General'
    if(no_days>=3000):
        return 'Field Marshal'
    

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('C:/Users/saini/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
driver.maximize_window()
url='https://9gag.com/login'
driver.get(url)
login=driver.find_element_by_xpath("//input[contains(@id, 'login-email-name')]")
login.send_keys("") #enter email for bot account
password=driver.find_element_by_xpath("//input[contains(@id, 'login-email-password')]")
password.send_keys("") #enter password 
submit=driver.find_element_by_xpath("//input[contains(@type, 'submit')]")
submit.click()
time.sleep(6)
driver.get('https://9gag.com/gag/agAVN7W')
time.sleep(1)
while True:
    text_list=driver.find_elements_by_xpath("//*[contains(@id, 'c_')and not(descendant::*[@class='collapsed-comment'])]")
    # text_list=text_list[:-1]
    if(len(text_list)!=0):
        for i in text_list:
            print(i.text)
            if(i.text!=''):
                try:
                    us_name=(i.text.split("\n")[0])
                    co_1,rank_day=get_first_comment(us_name)
                    print(co_1)
                    if(co_1!='not found'):
                        i.find_element_by_xpath(".//a[contains(@class, 'reply')]").click()
                        driver.switch_to_active_element().send_keys(rank_day+" Sir!" +" Here's your link "+ co_1)
                        driver.find_elements_by_xpath("//a[contains(@class, 'cmnt-btn size-30 submit-comment')]")[-1].click()
                except Exception as e:
                    print(e)
            else:
                print('skip')
            print('sleeping')
            time.sleep(300)
    driver.refresh()