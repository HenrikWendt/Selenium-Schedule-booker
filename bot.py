import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



"""
sal = input("Vilken sal vill du boka? ") 
datum2 =input("Vilket datum? (OBS bara dag och månad ex 1/3) ") 
starttid =input("Från vilken tid? (OBS måste sluta på 15 ex 13:15) ")
sluttid =input("Till vilken tid? (OBS måste sluta på 00 ex 18:00, man kan max boka 4 timmar) ")
user = input("Liu-ID: ")
password = input("Lösenord till Liu-ID: ")
"""


sal ="ISYtan9"
datum2 ="20/9" # (OBS bara dag och månad ex 1/3)
starttid ="13:15" #(OBS måste sluta på 15 ex 13:15)
sluttid ="17:00" #(OBS måste sluta på 00 ex 18:00, man kan max boka 4 timmar)
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
#driver = webdriver.Chrome()
driver = webdriver.Chrome('E:\\Progg\\Selenium-bot\\chromedriver', options=options)


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
time.sleep(2)
driver.find_elements_by_xpath(datum)[0].click()

time.sleep(2) 
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

time.sleep(2)

#bookingText = driver.find_element_by_id("table0")
#print(bookingText.text)
#text = bookingText.text
time.sleep(2)

driver.find_elements_by_xpath('//*[@id="showsendmail"]')[0].click()
time.sleep(2)
driver.find_elements_by_xpath('//*[@id="sendmailbutton"]')[0].click()

driver.quit()

#Send Email comfirmation.


"""
    options2 = webdriver.ChromeOptions()
    driver2 = webdriver.Chrome('E:\\Progg\\Selenium-bot\\chromedriver', options=options2)
    action2 = ActionChains(driver2)
    driver2.get('https://outlook.office365.com/mail/inbox')


    time.sleep(2)
    driver2.find_element_by_name("loginfmt").send_keys(user+"@student.liu.se")
    driver2.find_elements_by_xpath('//*[@id="idSIButton9"]')[0].click()
    time.sleep(5)
    driver2.find_elements_by_xpath('//*[@id="passwordInput"]')[0].send_keys(password)
    driver2.find_elements_by_xpath('//*[@id="submitButton"]')[0].click()
    time.sleep(5)
    driver2.find_elements_by_xpath("//*[contains(text(), 'Nytt meddelande')]")[0].click()

    time.sleep(3)

    action2.send_keys("henrikwendt95@gmail.com")
    action2.send_keys(Keys.TAB)
    action2.send_keys(Keys.TAB)
    action2.send_keys(Keys.TAB)
    action2.send_keys(Keys.TAB)
    action2.send_keys("Bekräftelse på salsbokning av: " +user)
    action2.send_keys(Keys.TAB)
    action2.send_keys(text)
    action2.send_keys(Keys.TAB)
    action2.send_keys(Keys.TAB)
    action2.send_keys(Keys.ENTER)
    action2.send_keys(Keys.ENTER)
    action2.perform()
    time.sleep(2)


    driver2.quit()
"""