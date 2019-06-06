from behave import given, when, then

@when(u'Я нажимаю на кнопку в избранное или добавлено и значение должно меняться')
def submit_form(context):
    context.browser.find_element_by_class_name("click_button_favorites").click()


@then(u'Я нажимаю на кнопку в избранное или добавлено и значение должно меняться')
def submit_form(context):
    context.browser.find_element_by_class_name("click_button_favorites").click()


@when(u'Я делаю logout пользователя')
def submit_form(context):
    context.browser.find_element_by_class_name("fa-sign-out").click()

@then(u'Я нажимаю на кнопку в избранное или добавлено и меня перекидывает на страницу входа')
def submit_form(context):
    context.browser.find_element_by_class_name("click_button_favorites").click()

