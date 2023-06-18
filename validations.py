from argparse import ArgumentTypeError
from urllib.parse import urlparse
from validators import url, ipv4, ipv6, domain, between
from re import sub
from requests import get, exceptions

class ArgumentError(ArgumentTypeError):
    pass
 
def check_scheme(user_input):
    parsed = urlparse(user_input)
    if parsed.scheme and parsed.scheme not in ['http', 'https']:
        raise ArgumentError("Invalid scheme. Only 'http' and 'https' are allowed.")
    return user_input
 
def add_scheme(user_input):
    check_scheme(user_input)

    parsed = urlparse(user_input)
    if not parsed.scheme:
        user_input = f"http://{user_input}"
    else:
        user_input = parsed.path
 
    return user_input
 
def remove_scheme(user_input):
    check_scheme(user_input)
    
    parsed = urlparse(user_input)
    if not parsed.scheme:
        user_input = parsed.path
    else:
        user_input = parsed.netloc
 
    return user_input
 
def url_validation(user_input):
    user_input = add_scheme(user_input)
    if url(user_input):
        return user_input
    else:
        raise ArgumentError("Invalid URL.")
 
def ip_address_validation(user_input):
    user_input = remove_scheme(user_input)
    if ipv4(user_input) or ipv6(user_input):
        return user_input
    else:
        raise ArgumentError("Invalid IP address.")
 
def domain_validation(user_input):
    user_input = remove_scheme(user_input)
    if domain(user_input):
        return user_input
    else:
        raise ArgumentError("Invalid domain name.")
 
def port_validation(user_input):
    if between(int(user_input), min=1, max=65535):
        return user_input
    else:
        raise ArgumentError(f"Invalid port number. Must be between 1 and 65535.")
 
def add_port(user_input, port):
    user_input = f"{user_input}:{port}"
    return user_input
 
def juice_shop_validation(user_input):
    base_url = sub(r'^https?://', '', user_input)
    http_url = f'http://{base_url}'
    https_url = f'https://{base_url}'
 
    for url in [http_url, https_url]:
        try:
            response = get(url)
            if response.ok and "OWASP Juice Shop" in response.text:
                return True
        except exceptions.RequestException:
            continue
 
    return False
