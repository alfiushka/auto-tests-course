from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #for inp in browser.find_elements_by_css_selector(".form-group input"):
    #inp.send_keys("data")

    input1 = browser.find_element_by_tag_name("input[name=firstname]")
    input1.send_keys("Rus")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk@ya.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element=browser.find_element_by_id("file")
    element.send_keys(file_path)
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")
	#input5 = browser.find_element_by_name( 'first_name' )
	#input5.send_keys("Ivan")
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
