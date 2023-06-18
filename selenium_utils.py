from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def open_url(driver, url_address):
    driver.get(url_address)
 
def wait_for_element_to_be_visible_by_css_selector(wait, selector):
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
 
def open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait):
    open_url(driver, url_address)
    wait_for_element_to_be_visible_by_css_selector(wait, '.logo')
 
def wait_for_element_to_be_clickable_by_css_selector(wait, selector):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
 
def wait_for_element_to_be_clickable_and_return_by_css_selector(wait, selector):
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
 
def wait_for_element_to_be_clickable_and_click_by_css_selector(wait, selector):
    wait_for_element_to_be_clickable_and_return_by_css_selector(wait, selector).click()
 
def write_text(driver, selector, text):
    text_area = driver.find_element(By.CSS_SELECTOR, selector)
    text_area.clear()
    text_area.send_keys(text)
 
def write_text_and_press_enter(driver, selector, text):
    write_text(driver, selector, text)
    text_area = driver.find_element(By.CSS_SELECTOR, selector)
    text_area.send_keys(Keys.ENTER)
 
def dismiss_welcomebanner(wait):
    wait_for_element_to_be_clickable_and_click_by_css_selector(wait, '.close-dialog')
 
def open_homepage_wait_for_juiceshop_logo_and_dismiss_welcomebanner(driver, url_address, wait):
    open_homepage_and_wait_for_juiceshop_logo(driver, url_address, wait)
    dismiss_welcomebanner(wait)
 
def switch_tab(driver, tab_index):
    driver.switch_to.window(driver.window_handles[tab_index])
 
def refresh_url(driver):
    driver.refresh()
 
def open_newtab(driver):
    driver.execute_script("window.open('about:blank', '_blank');")
 
def open_newtab_andswitchtoit(driver):
    open_newtab(driver)
    switch_tab(driver, 1)
 
def parsing_currentpage(driver):
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    return soup