from behave import given, when, then

@when(u'Выпадает живой поиск "{name}" из одного фильма который был без рейтинга подходящих слову лови момент')
def live_search(context, name):
    context.browser.find_element_by_id(name)

@then(u'Я нажимаю на фильм и должен перейти на страницу фильма')
def submit_form(context):
    context.browser.find_element_by_id('search-results').click()

@then(u'Я открываю фильм с id 15k789 которого не сущестует, и я должен попасть на страницу с ошибкой 404')
def open_page(context):
    context.browser.get('http://localhost:8000/movie/15k789')
