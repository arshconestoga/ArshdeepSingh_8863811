from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# navigate to Amazon login page
driver.get("https://www.amazon.ca/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.ca%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=caflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(3)

# going in to create account
Account = driver.find_element("id", "createAccountSubmit")
Account.click()
time.sleep(3)

# going back to sign in
Signin = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[9]/a")
Signin.click()
time.sleep(3)
# fill in email field
email = driver.find_element("id", "ap_email")
email.send_keys("arshmakkar@gmail.com")
time.sleep(3)
email.send_keys(Keys.RETURN)
# fill in password field
password = driver.find_element("id", "ap_password")
password.send_keys("Qwerty#0987")
time.sleep(5)
password.send_keys(Keys.RETURN)

# Go to your orders
Orders = driver.find_element("id", "nav-orders")
Orders.click()
time.sleep(5)

# adding ellements
account = driver.find_element("xpath", "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span")
signout= driver.find_element("xpath", "/html/body/div[1]/header/div/div[3]/div[2]/div[2]/div/div[2]/a[15]/span")

# Mouse move over actions to signout
actions=ActionChains(driver)
actions.move_to_element(account).move_to_element(signout).click().perform()
time.sleep(5)
# close the browser
driver.quit()