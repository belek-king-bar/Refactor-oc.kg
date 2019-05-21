from behave import given, when, then


@when(u'Я должен быть на главной странице')
def should_be_at_main(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/'


@when(u'Выпадает живой поиск "{name}" из одного фильма подходящих слову лови момент я нажимаю на фильм '
      u'и должен перейти на страницу фильма')
def submit_form(context, name):
    context.browser.find_element_by_id(name).click()


@when(u'Я нажимаю на кнопку смотреть и я должен быть на странице просмотра фильма')
def submit_form(context):
    context.browser.find_element_by_class_name('custom_btn_border').click()


@when(u'Я кликаю на иконку добавление комментария "{name}"')
def input_text(context, name):
    context.browser.find_element_by_id(name).click()


@when(u'Я добавляю комментарий с текстом "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_id(name).send_keys(text)


@then(u'Отправляю форму с кнопкой "{name}" и в странице должен появится новый комментарий')
def submit_form(context, name):
    context.browser.find_element_by_id(name).click()


@when(u'Я добавляю комментарий с пустым текстом в поле "{name}"')
def enter_text(context, name):
    context.browser.find_element_by_id(name).send_keys('')


@when(u'Отправляю форму с кнопкой "{name}" и в странице ничего не произойдет')
def submit_form(context, name):
    context.browser.find_element_by_id(name).click()


@when(u'Я нажимаю на иконку пользователя "{name}"')
def submit_form(context, name):
    context.browser.find_element_by_class_name(name).click()


@then(u'Я делаю logout пользователя')
def submit_form(context):
    context.browser.find_element_by_class_name("fa-sign-out").click()

