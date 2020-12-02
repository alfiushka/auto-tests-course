import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_cart_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
    #button.click()
    assert button > 0, "There is no such element"
    time.sleep(30)
    