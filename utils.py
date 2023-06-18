from sys import platform
from shutil import which
from random import choices
from string import ascii_lowercase, digits
from json import dumps
from requests import Session

def get_operating_system():
    mapping = {
            'win32': 'Windows',
            'darwin': 'MacOS',
            'linux': 'Linux'
            }
    return mapping.get(platform, 'Unknown')
 
SUPPORTED_BROWSERS = {
    'Linux': ['firefox', 'chrome', 'chromium'],
    'Windows': ['firefox', 'chrome', 'edge'],
    'MacOS': ['firefox', 'chrome', 'safari'],
}
 
def check_browser(browser):
    current_os = get_operating_system()
 
    if browser not in SUPPORTED_BROWSERS.get(current_os, []):
        raise ValueError(f"{browser} is not supported or untested on {current_os}.")
 
    if current_os == 'Linux' and browser == 'chrome':
        if which('chrome') is None:
            browser = 'chromium'
        else:
            browser = 'chrome'
    elif current_os == 'Linux' and browser == 'chromium':
        if which('chromium') is None:
            browser = 'chrome'
        else:
            browser = 'chromium'
 
    if which(browser) is None:
        raise ValueError(f"{browser} is not installed or not detected.")
 
    return True

def generate_random_email():
    username = ''.join(choices(ascii_lowercase + digits, k=10))
    domain = "owasp.org"
    email = f"{username}@{domain}"
    return email

def get_admin_session(url_address):
    payload = dumps({'email': 'admin@juice-sh.op', 'password': 'admin123'})
    return connect(url_address, payload)

def connect(url_address, payload):
    session = Session()
    headers = {'Content-Type': 'application/json'}
    login = session.post('{}/rest/user/login'.format(url_address),
                         headers=headers,
                         data=payload)
    if not login.ok:
        raise RuntimeError('Error logging in. Content: {}'.format(login.content))
    token = login.json().get('token')
    session.cookies.set('token', token)
    session.headers.update({'Authorization': 'Bearer {}'.format(token)})
    return session

def send_feedback(url_address, session, payload):
    submit = session.post('{}/api/Feedbacks'.format(url_address),
                          headers={'Content-type': 'application/json'},
                          data=dumps(payload))

def whoami(url_address, session):
    who = session.get('{}/rest/user/whoami'.format(url_address), headers={'Accept': 'application/json'})
    if not who.ok:
        raise RuntimeError('Error retrieving current user details')
    return who.json()

def get_current_user_id(url_address, session):
    return whoami(url_address, session).get('id')

def get_basket_url(url_address):
    return '{}/rest/basket'.format(url_address)

def build_basket(productid, basketid, quantity):
    return dumps({'ProductId': productid, 'BasketId': basketid, 'quantity': quantity})

def add_basket(url_address, session, payload):
    basketurl = '{}/api/BasketItems'.format(url_address)
    additem = session.post(basketurl, headers={'Content-Type': 'application/json'}, data=payload)

def checkout(url_address, session, basketid):
    checkout = session.post('{}/{}/checkout'.format(get_basket_url(url_address), basketid))