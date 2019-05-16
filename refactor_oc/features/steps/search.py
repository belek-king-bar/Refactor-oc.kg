from behave import given, when, then


@given(u'Я открыл любую страницу')
def open_page(context):
    context.browser.get('http://127.0.0.1:8000/')


@when(u'Я кликаю на иконку поиска "{name}"')
def input_text(context, name):
    context.browser.find_element_by_name(name).click()


@when(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_name(name).send_keys(text)


@when(u'Выпадает живой поиск "{name}" из трёх фильмов и трёх актёров подходящих слову джо')
def live_search(context, name):
    context.browser.find_element_by_id(name)


@when(u'Я отправляю форму')
def submit_form(context):
    context.browser.find_element_by_css_selector('button').click()


@then(u'Я должен быть на странице результатов поиска, результаты должны быть все где есть символы "{name}"')
def should_be_at_search_result(context, name):
    context.browser.get('http://127.0.0.1:8000/search/list?q=' + name)


@given(u'Я должен быть на любой странице')
def random_page(context):
    context.browser.get('http://127.0.0.1:8000/')


@then(u'Я кликаю на иконку поиска "{name}"')
def input_text(context, name):
    context.browser.find_element_by_name(name).click()


@then(u'Я ввожу текст "{text}" в поле "{name}"')
def enter_text(context, text, name):
    context.browser.find_element_by_name(name).send_keys(text)


@then(u'Выпадает живой поиск "{name}" с текстом по Вашему запросу ничего не найдено')
def live_search(context, name):
    context.browser.find_element_by_id(name)


@then(u'Я должен быть на странице результатов поиска "{name}", на странице должен быть текст ничего не найдено, попробуйте изменить запрос')
def no_found_search_result(context, name):
    context.browser.get('http://127.0.0.1:8000/search/list?q=' + name)

