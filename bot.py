import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

sal = input("Vilken sal vill du boka? ") 
datum2 =input("Vilket datum? (OBS bara dag och månad ex 1/3) ") 
starttid =input("Från vilken tid? (OBS måste sluta på 15 ex 13:15) ")
sluttid =input("Till vilken tid? (OBS måste sluta på 00 ex 18:00, man kan max boka 4 timmar) ")
user = input("Liu-ID: ")
password = input("Lösenord till Liu-ID: ")

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
driver = webdriver.Chrome('D:\Progg\Selenium-bot\chromedriver', options=options)
"""driver.maximize_window()"""

action = ActionChains(driver)
driver.get('https://cloud.timeedit.net/liu/web/wr_stud/')
time.sleep(0)
driver.find_elements_by_xpath("//*[contains(text(), 'Klicka här för att logga in')]")[0].click()
time.sleep(0)
driver.find_elements_by_xpath('//*[@id="userNameInput"]')[0].send_keys(user)
driver.find_elements_by_xpath('//*[@id="passwordInput"]')[0].send_keys(password)

driver.find_elements_by_xpath('//*[@id="submitButton"]')[0].click()
time.sleep(0)
driver.find_elements_by_xpath("//*[contains(text(), 'Studentbokning LiU')]")[0].click()
time.sleep(0)
driver.find_elements_by_xpath('//*[@data-param="search_text"]')[0].send_keys(sal)
time.sleep(1)
driver.find_elements_by_xpath(datum)[0].click()
"""test = driver.find_element_by_id('objectselectionresult')
for option in test.find_elements_by_tag_name('data-short'):
    if option.text == datum:
        option.click() 
        break"""
time.sleep(0) 
firstLevelMenu = driver.find_element_by_id("objectselectionresult")
action.move_to_element(firstLevelMenu).perform()
firstLevelMenu.click()
time.sleep(0)




feald = driver.find_element_by_id('reserveformedit')
for option in feald.find_elements_by_tag_name('option'):
    if option.text == starttid:
        option.click() 
        break

for option in feald.find_elements_by_tag_name('option'):
    if option.text == sluttid:
        option.click() 
        break

driver.find_elements_by_xpath('//*[@id="continueRes2"]')[0].click()

time.sleep(5)

driver.quit()

"""driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
"""
