from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = 'CecGuoHao'
password = '123456789'
request_cookies = None
def get_cookies(username,password):
    driver = webdriver.Chrome()
    driver.get("http://www.twitter.com/login")
    #driver.get("http://www.twitter.com/lijianzhong135/following")


    login_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')))#'//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')))
    # login_name.clear()
    login_name.send_keys(username)
    login_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')))#'//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')))
    # login_password.clear()
    login_password.send_keys(password)
    login_button =  driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button')
    login_button.click()
    print(driver.get_cookies())
    tweet_click = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[1]/div/div[3]/ul/li[2]/a')))

    tweet_click.click()
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        WebDriverWait(driver, 10)





    # print(driver.get_cookies())
    # print(driver.get_cookie())
    # listCookie = driver.get_cookies()
    # for cookies in listCookie:
    #     driver.add_cookie(cookies)
    # # driver.add_cookie(cookie)
    #driver.get("https://twitter.com/")




def init_cookie():
    request_cookies = get_cookies(username,password)




if __name__ == '__main__':
    get_cookies(username,password)
