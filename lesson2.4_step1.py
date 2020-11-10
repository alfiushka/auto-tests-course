from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #for inp in browser.find_elements_by_css_selector(".form-group input"):
    #inp.send_keys("data")
    #for elem_name in ["firstname", "lastname", "email"]:
    #browser.find_element_by_name(elem_name).send_keys(elem_name)
    button = WebDriverWait(browser, 14).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    #button.click()
    button2 = browser.find_element_by_id("book")
    button2.click()
    browser.execute_script("window.scrollBy(0, 100);")
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
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
