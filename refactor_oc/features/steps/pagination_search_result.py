from behave import given, when, then


@given(u'Я нахожусь на странице результатов поиска "{name}"')
def should_be_at_search_result(context, name):
    context.browser.get('http://127.0.0.1:8000/search/list?q=' + name)


@when(u'Я кликаю на страницу "{id}"')
def click_number_page(context, id):
    context.browser.find_element_by_id(id).click()


@then(u'Я должен быть на странице c номером "{id}"')
def number_page(context, id):
    url = 'http://127.0.0.1:8000/search/list?q=джо&page=' + id
    context.browser.get(url)


@when(u'Я кликаю на последнюю страницу "{last_page}"')
def click_last_page(context, last_page):
    context.browser.find_element_by_id(last_page).click()


@then(u'Я должен быть на последней странице "{last_page}"')
def last_page(context, last_page):
    context.browser.get('http://127.0.0.1:8000/search/list?q=джо&page=' + last_page)
