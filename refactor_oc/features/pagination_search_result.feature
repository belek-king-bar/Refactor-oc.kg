# Created by pavel at 5/18/19
Feature: Пагинация страницы результатов поиска

  Scenario: Успешная пагинация
    Given Я нахожусь на странице результатов поиска "джо"
    When Я кликаю на страницу "5"
    Then Я должен быть на странице c номером "5"
    When Я кликаю на последнюю страницу "last_page"
    Then Я должен быть на последней странице "293"
