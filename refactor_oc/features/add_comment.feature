Feature: Добавление комментария

  Scenario: Добавление комментариев к фильму
    Given Я открыл любую страницу
    When Я кликаю на иконку входа "sign_in"
    And Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    And Я должен быть на главной странице
    And Я кликаю на иконку поиска "show_search"
    And Я ввожу текст "Лови момент" в поле "q"
    And Выпадает живой поиск "search-results" из одного фильма подходящих слову лови момент я нажимаю на фильм и должен перейти на страницу фильма
    And Я нажимаю на кнопку смотреть и я должен быть на странице просмотра фильма
    And Я кликаю на иконку добавление комментария "id_text"
    And Я добавляю комментарий с текстом "Тестовый коммент" в поле "id_text"
    Then Отправляю форму с кнопкой "comment_add" и в странице должен появится новый комментарий

    Scenario: Не успешное добавление комментариев к фильму
    Given Я открыл любую страницу
    When Я кликаю на иконку поиска "show_search"
    And Я ввожу текст "Лови момент" в поле "q"
    And Выпадает живой поиск "search-results" из одного фильма подходящих слову лови момент я нажимаю на фильм и должен перейти на страницу фильма
    And Я нажимаю на кнопку смотреть и я должен быть на странице просмотра фильма
    And Я кликаю на иконку добавление комментария "id_text"
    And Я добавляю комментарий с пустым текстом в поле "id_text"
    And Отправляю форму с кнопкой "comment_add" и в странице ничего не произойдет
    And Я нажимаю на иконку пользователя "user_pic_link"
    Then Я делаю logout пользователя