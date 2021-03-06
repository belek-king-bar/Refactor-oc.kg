Feature: Вход

  Scenario: Вход под админом
    Given Я открыл любую страницу
    When Я кликаю на иконку входа "sign_in"
    And Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на главной странице

  Scenario: Не успешный вход
    Given Я открыл страницу входа
    When Я ввожу текст "qweqwe" в поле "username"
    And Я ввожу текст "123123" в поле "password"
    And Я отправляю форму
    Then Я должен быть на странице входа
    And Я должен видеть сообщение об ошибке с текстом "Пожалуйста, введите правильные Логин и пароль. Оба поля могут быть чувствительны к регистру."
