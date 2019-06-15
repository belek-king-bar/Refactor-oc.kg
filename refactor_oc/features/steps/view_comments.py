from behave import given, when, then

@given(u"Я открыл страницу фильма с id 15401")
def open_movie_page(context):
    context.browser.get('http://127.0.0.1:8000/movie/15401')

@when(u"Я кликаю на кнопку Показать больше")
def show_more(context):
    context.browser.find_element_by_id('show_all_comments_btn').click()

@then(u"Я нажимаю на кнопку Все комментарии")
def show_all_comments(context):
    context.browser.find_element_by_id('comments_page_btn').click()

@then(u"Я оказываюсь на странице комментариев")
def open_comments_page(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/movie/15401/comments'

