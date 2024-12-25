from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,  TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium_stealth import stealth
from modify import modify_resume
from modify import cover_letter
from render import render_resume
from cleaning import get_data_href
import time
import random

EMAIL="Your Internshaala Email Here"
PASSWORD="Internshaala Password"
DIRECTORY="Path for modified resumes"
LOGIN_URL="https://internshala.com/login/student"
CENTRAL_URL="https://internshala.com"

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--enable-javascript")
chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument('--headless')

prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
driver.maximize_window()

def check_additional_questions():
    time.sleep(1)
    try:
        add_popup = driver.find_elements(By.CSS_SELECTOR, "h4.question-heading")
        check = False
        for ele in add_popup:
            if(ele.text == "Additional question(s)"):
                check = True
        if(check):
            print("Additional Questions detected")
            time.sleep(25)
        else:
            print("Element Detected but relevant text check failed")
    except:
        print("Additional questions search failed ")

def already_applied():
    time.sleep(1)

    try:
        disabled_btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-large.disabled")
        print("Already Applied to this Internship")
        return True
    except:
            return False

def relocation_popup():
    time.sleep(1)
    try:
        label = driver.find_element(By.XPATH, "//label[@for='check']")
        label.click()

        print("Relocation box ticked")
    except:
        print("Relocation checkbox not found")

def remove_current_resume():

    try: 
        frame_close_btn = driver.find_element(By.CLASS_NAME, "frame-close")
        frame_close_btn.click()

        print("Removed Previous Resume")
    except:
        print("Removing current resume operation aborted")

def cover_letter_holder():
    
    try:
        cover_letter_placeholder = driver.find_element(By.CSS_SELECTOR, ".ql-editor.ql-blank")
        cover_letter_txt=cover_letter(job_description)
        cover_letter_placeholder = driver.find_element(By.CSS_SELECTOR, ".ql-editor.ql-blank")
        cover_letter_placeholder.send_keys(cover_letter_txt)
    except:
        print("Cover Letter Operation Aborted")

def submit():
    time.sleep(1)
    try:
        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.click()

        time.sleep(2)
    except:
        print("Submitting Operation Aborted")

def upload_modified_resume():
    relocation_popup()
    cover_letter_holder()
    remove_current_resume()
    check_additional_questions()

    file_name = rf"{DIRECTORY}\{company_name}.pdf" 
    try:
        upload_btn = driver.find_element(By.ID, "custom_resume")
        upload_btn.send_keys(file_name)

        submit()
    except:
        "Final resume uploading operation failed"

        

def apply_button():
    time.sleep(random.randint(1, 2))

    try:
        apply_btn = driver.find_element(By.ID, "easy_apply_button")
        apply_btn.click()
        
        upload_modified_resume()
    except NoSuchElementException:
        print("No such element exception raised while clicking apply button. Trying again")
        # apply_button()
    
    except StaleElementReferenceException:
        print("Stale element reference raised while clicking apply button. Trying again")
        apply_button()

def final_resume(job_description, skills_required, company_name):
    final_resume = modify_resume(job_description, skills_required)
    resume_name=f"{company_name}.pdf"
    render_resume(final_resume, resume_name)
    
    apply_button()

def get_job_desc():
    time.sleep(random.randint(1, 2))

    try:
        global job_description
        job_description = driver.find_element(By.CLASS_NAME, "text-container").text
        skills_required = driver.find_element(By.CLASS_NAME, "round_tabs_container").text

        global company_name
        company_name = driver.find_element(By.CLASS_NAME, "link_display_like_text").text
        
        final_resume(job_description, skills_required, company_name)
    except NoSuchElementException:
        print("No such element exception raised while finding job description and skills. Trying again")
        #get_job_desc()
    
    except StaleElementReferenceException:
        print("Stale element reference raised while finding job description and skills. Trying again")
        get_job_desc()

def navigation():
    time.sleep(1)
    data_href_list = get_data_href()
    print("Successfully scraped data href's")

    for data_href in data_href_list:
        url = CENTRAL_URL+data_href
        driver.get(url)
        
        response = already_applied()
        if(response):
            continue
        else:
            get_job_desc()
        
def manual_login():
    time.sleep(1)
    try:
        login_btn = driver.find_element(By.ID, "login_submit")
        manual_login()
    except NoSuchElementException:
        print("Congrats, Login Completed!")
        navigation()

def login_button(current_trial=0, max_trials=10):
    time.sleep(random.randint(2, 3))
    if(current_trial<max_trials):
        try:
            login_btn = driver.find_element(By.ID, "login_submit")
            login_btn.click() 
            
            current_trial+=1
            login_button(current_trial)
        except NoSuchElementException:
            print("Congrats, Login Completed!")
            navigation()
        except ElementClickInterceptedException:
            print("Captcha Error")

            time.sleep(random.randint(1, 2))
            close_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.modal_primary_btn.close_action")
            close_button.click()
            time.sleep(1)

            current_trial+=1
            login_button(current_trial)        
        except StaleElementReferenceException:
            login_button()
    else:
        print("Max Trials Reached")
        manual_login()

def initial_credentials(url, id, password):
    driver.get(url)
    time.sleep(random.randint(3, 5))
    try:
        email_space=driver.find_element(By.ID, "email")
        for char in id:
            time.sleep(random.randint(1, 2))
            email_space.send_keys(char)
        print("Email entered successfully")

        time.sleep(1)
    
        password_space = driver.find_element(By.ID, "password")
        for char in password:
            time.sleep(1)
            password_space.send_keys(char)
        print("Password entered successfully")
    except NoSuchElementException:
        print("No such element exception raised while entering credentials. Trying again")
        initial_credentials()
    
    except StaleElementReferenceException:
        print("Stale element reference raised while entering credentials. Trying again")
        initial_credentials()
    
    
    login_btn = driver.find_element(By.ID, "login_submit")
    login_btn.click() 

    time.sleep(random.randint(1, 2))

    login_button()
    


initial_credentials(LOGIN_URL, EMAIL, PASSWORD)