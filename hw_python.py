
def func_data(func, *args):
    func_read = func.__name__.replace("_", " ")
    print(f'{func_read}', end=" ")
    for arg in args:
        print(arg, end=" ")
    print()


def open_browser(browser_name):
    func_data(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_data(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_data(find_registration_button_on_login_page, page_url, button_text)


open_browser("Chrome")
go_to_companyname_homepage("https://mail.yandex.ru")
find_registration_button_on_login_page("https://mail.yandex.ru", "Войти в Почту")