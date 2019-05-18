from behave import given, when, then


@when(u'Я кликаю на кнопку регистрации')
def click_into_signup(context):
    context.browser.find_element_by_link_text('Зарегистрироваться').click()


@then(u'Я должен быть на странице сообщения подтверждения по эмейлу')
def should_be_at_active_email(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/webauth/signup/signup_complete/'


@given(u"Я открыл страницу регистрации")
def open_signup_page(context):
    context.browser.get('http://127.0.0.1:8000/webauth/signup/')


@then(u"Я должен быть на странице регистрации")
def should_be_at_signup(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/webauth/signup/'


@then(u'Я должен видеть сообщение об ошибке регистрации с текстом "{text}"')
def see_error_with_text(context, text):
    error = context.browser.find_element_by_class_name('errormessage')
    assert error.text == text
