import requests
from selenium import webdriver

mock_creds={ #this should come from a config yml file
    'member': {
        'user': 'member',
        'login_url': 'http://127.0.0.1:5000/user/sign-in',
        'email': 'member@example.com',
        'password': 'Password1'
    },
    'admin': {
        'user': 'admin',
        'login_url': 'http://127.0.0.1:5000/user/sign-in',
        'email': 'admin@example.com',
        'password': 'Password1'
    }


}


def make_session(user=None):
    session = requests.session()
    #do the cookie thingies here
    if user:
        creds=mock_creds[user]
        cookies = get_cookies_with_selenium(creds)
        for cookie in cookies:
            cookie_obj = requests.cookies.create_cookie(domain=cookie['domain'],name=cookie['name'],value=cookie['value'])
            session.cookies.set_cookie(cookie_obj)
        print(session.cookies)
    return session

def get_cookies_with_selenium(creds):
    login_url= creds['login_url']
    email= creds['email']
    password= creds['password']

    driver = webdriver.Chrome()
    driver.get(login_url)
    
    email_field = driver.find_element_by_id("email")
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element_by_id("password")
    password_field.clear()
    password_field.send_keys(password)

    submit_button = driver.find_element_by_xpath('//input[@type="submit"]')

    submit_button.click()
    print(f"got cookie with selenium: {driver.get_cookies()}")
    return driver.get_cookies()


    