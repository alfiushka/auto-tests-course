from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #for inp in browser.find_elements_by_css_selector(".form-group input"):
    #inp.send_keys("data")
    #for elem_name in ["firstname", "lastname", "email"]:
    #browser.find_element_by_name(elem_name).send_keys(elem_name)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element_by_css_selector("[class='nowrap'][id='input_value']").text)
    print(x)
    y = calc(x)
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
# //button[text()='Submit'] //*[@type="submit"]  //form[@action="#"]/div[6]/button[3]'  //button[contains(text(), 'Отправить')]
#buttons = driver.find_elements_by_xpath("//button")
#for button in buttons:
#    if button.text == 'Submit':
#        button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
