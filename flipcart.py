
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path of chrome_driver
PATH= "C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)
# Url of Flipcart
driver.get("https://www.flipkart.com")

driver.implicitly_wait(100)

#Close the login popup
close=driver.find_element_by_xpath("//*[@class='_2AkmmA _29YdH8']").click()

# signing initially the login popup
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("Phone_no")
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("password")
#driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()

# Search in Search bar
search= driver.find_element_by_name("q")
search.clear()
search.send_keys("redmi note 6 pro (black, 64 gb)")
search.send_keys(Keys.RETURN)

#driver.implicitly_wait(2)

# Select the product
prods= driver.find_elements_by_class_name("_31qSD5")
for i in prods:
    if i.text[0] != 'T':
        #print(i.text)
        driver.get(i.get_attribute('href'))
        break
    else:
        print('No product found')

# Select Buy
time.sleep(3)

# a= driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[3]")    check if not sold out


b= driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div[2]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button").click()

time.sleep(3)

# Putting credential details
# Enter Phone no.
driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input").send_keys("your_phone_no")       # Phone no.
driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[3]/button").click()
time.sleep(1)
# Enter Password
driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[2]/input").send_keys("your_password")         # Password
driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[3]/button").click()
time.sleep(1)

# Delivary Address
driver.find_element_by_xpath("//*[@id='CNTCT80CCD4ACA3C847DAB6752F31B']/button").click()

# Enter Email
driver.find_element_by_xpath("//*[@id='container']/div/div[2]/div/div[1]/div[3]/div/div/div/div[2]/div[2]/span[1]/form/input").send_keys("your_email")
# hit continue
driver.find_element_by_xpath("//*[@id='to-payment']/button").click()


time.sleep(5)

driver.quit()
