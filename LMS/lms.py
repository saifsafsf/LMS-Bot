from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from LMS import constants as const
import os

'''
takes Chrome driver object & makes a child object LMS
LMS Object can use Chrome object functions & its own too
simply logs in to LMS-NUST & downloads each subject's syllabus
For details, must read README.md provided with the project.
'''
class LMS(webdriver.Chrome):

    '''
    takes chrome driver's address (README.md) & a boolean (explained later)
    USE YOUR OWN ADDRESS
    '''
    def __init__(self, driver_path=r"C:\NUST\Practice\Data Science\Web Scraping\Selenium Drivers", teardown=False):
        # initializing variables
        self.driver_path = driver_path
        self.teardown = teardown
        super(LMS, self).__init__()

        # adding path to the environment variables
        os.environ['PATH'] += self.driver_path

        # waits for a page to load & maximizes window
        self.implicitly_wait(30)
        self.maximize_window()

    '''
    navigates to the login page
    '''
    def login_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(30)

    '''
    uses teardown to find if 
    the program should shutdown Chrome when it ends
    '''
    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    '''
    takes username & password from environment variables
    can also take as arguments
    logs in using the credentials
    '''
    def login(self, 
            username=os.environ.get('LMS_USER'), 
            password=os.environ.get('LMS_PASS')
            ):
        
        # finding the username input textbox & clearing it
        input_user = self.find_element(by=By.ID, value='username')
        input_user.clear()

        # typing username
        input_user.send_keys(username)

        # finding password input textbox & clearing it
        input_pass = self.find_element(by=By.ID, value='password')
        input_pass.clear()

        # typing password & pressing ENTER
        input_pass.send_keys(password)
        input_pass.send_keys(Keys.RETURN)

    '''
    takes subject's id
    uses 'download center' in the given subject's webpage
    downloads the compressed syllabus
    '''
    def download_subject(self, id):
        # navigating to the subject page
        self.get(const.SUBJECT_LINK + id)
        self.implicitly_wait(30)

        # 'download center' button in the sidebar
        down_cntr_btn = self.find_element(by=By.CSS_SELECTOR, value='li[data-key="downloadcenter"]')
        down_cntr_btn.click()

        # unselecting all files
        select_none = self.find_element(by=By.ID, value='downloadcenter-none-included')
        select_none.click()

        # finding hidden options
        show_opt = self.find_element(by=By.ID, value='downloadcenter-bytype')
        show_opt.click()

        # selecting files only
        all_files = self.find_element(by=By.ID, value='downloadcenter-all-mod_resource')
        all_files.click()

        # creating .zip & downloading
        zip_button = self.find_element(by=By.ID, value='id_submitbutton')
        zip_button.click()