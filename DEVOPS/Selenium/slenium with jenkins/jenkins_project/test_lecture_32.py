# importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# webdriver integration with pytest

# defining a function that will run before running evry function
def setup_function():
    global driver
    # Define hub URL
    

# Setup Chrome options (as desired_capabilities is deprecated in newer versions)
    

    # Establish remote connection to Selenium Grid
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    driver. maximize_window()


# defining function that will run at the end of each function
def teardown_function():
    driver.quit()


# making a function to locate the sign in and password box on github and filling values in it
@pytest.mark.parametrize('username,password',[("ahsanzafar0501@gmail.com","mygmailpassword"),("ahmed","ahmed123")])
def test_credentials(username,password):
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="login_field"]').send_keys(username)
    time.sleep(10)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(10)
    allure.attach(driver.get_screenshot_as_png(), name="mygithub_sc", attachment_type=AttachmentType.PNG)


# the above function runs two times as I have passed two values, but this function run one by one not simultaneously

# to run functions simultaneously, you need to install pip install pytest-xdist
# after installing above thing, run function again now this time, both task will run at once simultaneously
# command will be: python -m pytest ./test_lecture_32.py -n 2
# as i have two tuples or two values i will mention 2 i -n


