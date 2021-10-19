import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from datetime import datetime, timedelta

"""
sal = input("Vilken sal vill du boka? ") 
datum2 =input("Vilket datum? (OBS bara dag och månad ex 1/3) ") 
starttid =input("Från vilken tid? (OBS måste sluta på 15 ex 13:15) ")
sluttid =input("Till vilken tid? (OBS måste sluta på 00 ex 18:00, man kan max boka 4 timmar) ")
user = input("Liu-ID: ")
password = input("Lösenord till Liu-ID: ")
"""

date = datetime.today() + timedelta(days=2)
 
sal ="SH408"
datum2 = str(date.day)+"/"+str(date.month)  # (OBS bara dag och månad ex 1/3)
starttid ="17:15" #(OBS måste sluta på 15 ex 13:15)
sluttid ="19:00" #(OBS måste sluta på 00 ex 18:00, man kan max boka 4 timmar)
user =""
password =""

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()

print ("Sal: "+ sal)
print ("Datum: "+ datum2)
print ("Starttid: "+ starttid)
print ("Sluttid: "+ sluttid)
print ("Liu-ID: "+ user)
print ("Lösenord: "+"***********")

datum1 = "//*[contains(text(), '"
datum3 = "')]"
datum = datum1 + datum2 + datum3

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('E:\\Progg\\Selenium-bot\\chromedriver', options=options)
action = ActionChains(driver)
delay = 3

def performAction(action,xpath):
    if xpath:
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, action)))
            return True
        except TimeoutException:
            return False
    else:
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, action)))
            return True
        except TimeoutException:
            return False

def waitForPageToLoad(action, xpath):
    loopCount = 0
    while performAction(action,xpath) != True:
        if(loopCount < 10):
            loopCount = loopCount + 1
            print(loopCount)
            performAction(action,xpath)
        else:
            print("Page wont load, or can't find element")
            driver.quit()
            return False
    return True

def dateShifterHelper(action, xpath):
    loopCount = 0
    while performAction(action,xpath) != True:
        if(loopCount < 4):
            loopCount = loopCount + 1
            print(loopCount)
            performAction(action,xpath)
        else:
            print("Page wont load, or can't find element")
            return False
    return True 

driver.get('https://cloud.timeedit.net/liu/web/wr_stud/')

waitForPageToLoad("//*[contains(text(), 'Klicka här för att logga in')]",True)
driver.find_elements_by_xpath("//*[contains(text(), 'Klicka här för att logga in')]")[0].click()

waitForPageToLoad('//*[@id="userNameInput"]',True)
driver.find_elements_by_xpath('//*[@id="userNameInput"]')[0].send_keys(user)
driver.find_elements_by_xpath('//*[@id="passwordInput"]')[0].send_keys(password)
driver.find_elements_by_xpath('//*[@id="submitButton"]')[0].click()

waitForPageToLoad("//*[contains(text(), 'Studentbokning LiU')]",True)
driver.find_elements_by_xpath("//*[contains(text(), 'Studentbokning LiU')]")[0].click()
waitForPageToLoad('//*[@data-param="search_text"]',True)
driver.find_elements_by_xpath('//*[@data-param="search_text"]')[0].send_keys(sal)

time.sleep(2)
try:
    driver.find_elements_by_xpath(datum)[0].click()
    
except:
        print("Can't find date, trying next week.")
        try:
            driver.find_elements_by_xpath('//*[@id="leftresdateinc"]')[0].click()
            time.sleep(2)
            driver.find_elements_by_xpath(datum)[0].click()
        except:
            #Retries with longer waiting
            driver.find_elements_by_xpath('//*[@id="leftresdatedec"]')[0].click()
            if dateShifterHelper(datum,True):
                driver.find_elements_by_xpath(datum)[0].click()
            else:
                driver.find_elements_by_xpath('//*[@id="leftresdateinc"]')[0].click()
                if dateShifterHelper(datum,True):
                    driver.find_elements_by_xpath(datum)[0].click()  
                else:
                    driver.quit()


waitForPageToLoad("objectselectionresult",False)
firstLevelMenu = driver.find_element_by_id("objectselectionresult")
action.move_to_element(firstLevelMenu).perform()
firstLevelMenu.click()

waitForPageToLoad('reserveformedit',False)
feald = driver.find_element_by_id('reserveformedit')
for option in feald.find_elements_by_tag_name('option'):
    if option.text == starttid:
        option.click() 
        break

for option in feald.find_elements_by_tag_name('option'):
    if option.text == sluttid:
        option.click() 
        break

try:
    waitForPageToLoad('//*[@id="continueRes2"]',True)
    driver.find_elements_by_xpath('//*[@id="continueRes2"]')[0].click()
except:
    #Crash can't click on the correct slot, needs more work
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    print("Faild to book. #Crash can't click on the correct slot, needs more work")

try:
    waitForPageToLoad('//*[@id="showsendmail"]',True)
    driver.find_elements_by_xpath('//*[@id="showsendmail"]')[0].click()
except:
    #Someone has allready booked this slot, needs more work
    print("Faild to book. #Someone has allready booked this slot, needs more work")

waitForPageToLoad('//*[@id="sendmailbutton"]',True)
driver.find_elements_by_xpath('//*[@id="sendmailbutton"]')[0].click()

driver.quit()
