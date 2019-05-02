**Проект OC.KG**

---

## Клонирование проекта
1. В разделе Project > Details в верхнем правом углу нажмите на кнопку 'clone'. 
Скопируйте url.
2. В терминале запустите команду **git clone** + скопированный url.

## Виртуальное окружение

1. В терминале в папке проекта запустите команду python **-m virtualenv -p python3 venv**
2. И активируйте его командой **. venv/bin/activate**

## Зависимости

1. Глобально установите клиент mysql, запустив в терминале команду 
**sudo apt-get install python3-dev libmysqlclient-dev**. Для этого вам понадобятся 
права администратора (пароль пользователя root).
2. Установите зависимости проекта, запустив в терминале команду 
**pip install -r requirements.txt**

## База данных и миграции

1. Для подключения базы данных вы можете воспользоваться 
следующей [инструкцией](https://gitlab.com/sultanchoponov/newoc/wikis/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F-%D0%BD%D0%B0%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B1%D0%B4)
. Примечание: необходимо, чтобы у вас был установлен mysql, подробнее можно почитать [здесь](https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru).

## Локальные настройки

1. Откройте проект в Pycharm. Создайте в папке проекта refactor_oc файл local_settings.py (в той же папке, где находятся основные настройки проекта settings.py)
2. Пропишите в файле local_settings.py локальные настройки базы данных. Пример:

```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinema2',
        'USER': '[ваш юзер]',
        'PASSWORD': '[ваш пароль от базы данных]',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}
```

## Коммиты

1. Про то, как правильно делать коммиты, можно почитать [здесь](https://gitlab.com/sultanchoponov/newoc/wikis/Git:-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BA%D0%BE%D0%BC%D0%BC%D0%B8%D1%82).