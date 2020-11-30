link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_check_cart_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button[class='btn.btn-lg.btn-primary.btn-add-tobasket']")
    #button.click()
    self.assertTrue(button!=None, "No such element")
    time.sleep(10)
