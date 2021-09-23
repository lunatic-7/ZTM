# For automation (to control a website with human touch only with coding), first we are 
# gonna install selenium by typing (pip install selenium). Then we have to download the drivers 
# of browser we are gonna automate from selenium documentation (a stable version). Here,
# I m gonna download a driver of chrome.
# This chrome driver will help us in manipulating the chrome browser.

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()  # To maximize chrome window size.

# So, There is a site (selenium easy) https://www.seleniumeasy.com/test/ on which we are gonna
# try selenium to autmate it.

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')  # To open this link
# Copied from google.

# REMEMBER Selenium reads HTML of a webpage.

assert 'Selenium Easy Demo' in chrome_browser.title  # This is gonna check if Selenium easy demo exists
# in Title part of selenium's website HTML or not. We can do this thing with print statement as well.
# And remember, if we get a False, assert statement is gonna error out our programe.

show_message_button = chrome_browser.find_element_by_class_name('btn-default')  # To grab btn-default named class
print(show_message_button.get_attribute('innerHTML'))  # To grab the text inside that class, which is Show Message here.

# Let's start Automation.
# First now let's grab the text-area from selenium website:

assert 'Show Message' in chrome_browser.page_source  # Page source is complete HTML,

user_message = chrome_browser.find_element_by_id('user-message')  # To grab the text-area as it has this id.
user_message.clear()  # To clear any, in case if any earlier entry.
user_message.send_keys('I AM EXTRAAA COOOOOOL!')  # To type this message in the selected text-area.

show_message_button.click()  # To click on the button, finally.

output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRAAA COOOOOOL!' in output_message.text  # Just to verify if we have got this as output.

# REMEMBER ---> We can select these by using css selectors as well like this:
show_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')  # Means select 
# btn class which is +nt inside get_input id.
print(show_button)

chrome_browser.close()  # To automtically close the browser after doing our stuff.

# We often need to use time.sleep() in automation process, to prevent sites, from blocking 
# our account, as automation do things really fast, sites detects that it is a bot, and block
# our account.
