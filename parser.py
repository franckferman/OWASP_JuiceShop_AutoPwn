from argparse import ArgumentParser
from validations import ip_address_validation, domain_validation, port_validation
 
def setup_arg_parser():
    parser = ArgumentParser(description='OWASP Juice Shop AutoPwn - Automated Challenge Solver with Selenium and Requests')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--ip', type=ip_address_validation, help='IP address of the target Juice Shop instance.')
    group.add_argument('-d', '--domain', type=domain_validation, help='Domain name of the target Juice Shop instance.')
    parser.add_argument('-p', '--port', type=port_validation, help='Port number of the target Juice Shop instance. Must be between 1 and 65535.')
    parser.add_argument('-b', '--browser', type=str, default='firefox', help='Browser to use for testing. Supported options are "firefox", "chrome", and "safari". Firefox is used by default.')
    parser.add_argument('-w', '--wait_time', type=int, default=5, help='Delay before request timeout in seconds. Default is 5 seconds.')
 
    return parser
