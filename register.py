from selenium import webdriver

# Open codeforces in Chrome
browser = webdriver.Chrome()
browser.get('https://codeforces.com/register')

#Submit handle
handle = browser.find_element_by_name('handle')
handle.send_keys('akhaxx')

#Submit email
email = browser.find_element_by_name('email')
email.send_keys('gwyeqfg@hfvoefuho.tk')

#Submit password
password = browser.find_element_by_name('password')
password.send_keys('Tatasky98')

#Submit confirm_password
confirm_password = browser.find_element_by_name('passwordConfirmation')
confirm_password.send_keys('Tatasky98')

confirm_password.submit()
