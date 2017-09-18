import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, credentials):
    driver.get("https://www.angieslist.com/")
    try:
        #Buscar el boton sign in
        print('Searching SignIn button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btnSignin")))
        print('Searching SignIn button done')
        button.click()
        print('Click on {}'.format('Sign In'))

        print('Searching and fill login form begin')
        email = driver.wait.until(EC.presence_of_element_located(
            (By.ID, "email")))

        password = driver.wait.until(EC.presence_of_element_located(
            (By.ID, "password")))
        email.send_keys(credentials['email'])
        print('Fill input {}'.format('Emaill'))

        password.send_keys(credentials['password'])
        print('Fill input {}'.format('password'))
        print('Searching login form done')

        print('Searching submit begin')
        submit = driver.wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "login-form_submit")))
        print('Searching submit done')
        submit.click()
        print('Click on {}'.format('submit'))

        print('Searching categories menu begin')
        menu_house = driver.wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "categories_tab--member")))
        print('Searching categories menu done')
        menu_house.click()
        print('Click on first menu: {}'.format('HOUSE MENU'))

        print('Searching HOUSE MENU submenus begin')
        plumbing_menu_item = driver.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".categories_dropdown--house > li:nth-child(2) > a:nth-child(1)")))
        print('Searching HOUSE MENU submenus done')
        plumbing_menu_item.click()
        print('Click on first menu item {}'.format('house menu item #1'))

        print('Searching results list begin')
        results_plumbing = driver.find_element_by_id('spsearch--results-list')
        print('Searching results list done')

        results_plumbing_text = results_plumbing.text
        results_plumbing_html = results_plumbing.get_attribute('innerHTML')
        results_plumbing_soup = BeautifulSoup(results_plumbing_html, 'html.parser')
        for item in results_plumbing_soup.find_all('li'):
            if (len(item.div.div.a.find_all('div')[1].find_all('div')) > 0):
                print('Searching title and desription for each post begin')
                title = item.div.div.a.find_all('div')[1].find_all('div')[0].getText()
                description = item.div.div.a.find_all('div')[1].find_all('div')[2].get_text()
                print('Searching title and desription for each post done')
                print('Title: {}'.format(title))

                print('Description: {}'.format(description))
        # results_plumbing = driver.wait.until(EC.presence_of_element_located(
        #     (By.ID, "spsearch--results-list")))
        # print('Fill input {}'.format(results_plumbing))



    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    credentials = {
        'email': 'ivansfy@gmail.com',
        'password': 'slipknotforyou'
    }
    print('Begin scrapping')
    lookup(driver, credentials)
    print('Scrapping done')
    # time.sleep(5)
    # driver.quit()
