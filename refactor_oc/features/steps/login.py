from behave import given, when, then


@given(u'Я открыл страницу входа')
def open_login_page(context):
    context.browser.get('http://127.0.0.1:8000/webauth/login/')


@when(u'Я кликаю на иконку входа "{name}"')
def click_into_login(context, name):
    context.browser.find_element_by_class_name(name).click()


@then(u'Я должен быть на главной странице')
def should_be_at_main(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/'


@then(u"Я должен быть на странице входа")
def should_be_at_login(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/webauth/login/'


@then(u'Я должен видеть сообщение об ошибке с текстом "{text}"')
def see_error_with_text(context, text):
    error = context.browser.find_element_by_class_name('errorlist')
    assert error.text == text
