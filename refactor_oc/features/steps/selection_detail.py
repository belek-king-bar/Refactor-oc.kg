from behave import given, when, then


@given(u'Я открываю страницу подборок')
def open_selections_page(context):
    context.browser.get('http://127.0.0.1:8000/selections/')


@when(u'Я кликаю на понравившуюся подборку и перехожу на соответсвующую подборку')
def open_selections_detail(context):
    context.browser.find_element_by_id('catalog_film_1').click()


@then(u'Я выбираю нужный мне фильм и должен перейти на страницу фильма')
def open_selection_film(context):
    context.browser.get('http://127.0.0.1:8000/movie/138')


@given(u'Я открываю страницу подборки')
def open_selections_page(context):
    context.browser.get('http://127.0.0.1:8000/selections/2r4')


@then(u'Я открываю подборку с id 2r4 которой не сущестует')
def open_page(context):
    context.browser.get('http://localhost:8000/selections/2r4')


@then(u'Я должен попасть на страницу с ошибкой 404')
def open_page(context):
    context.browser.get('http://localhost:8000/selections/2r4')
