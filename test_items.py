import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def is_element_present(browser):
    try:
	browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector('.btn-add-to-basket')
        return True
    except:
        return False 
time.sleep(5)
def test_guest_should_see_add_basket_button(browser):
	browser.get(link) 
	assert is_element_present(browser)==True, "Button is not found"
