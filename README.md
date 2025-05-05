# SimpleBlog - простой блог

Проект является тестовым заданием.

## Функции проекта
* Доступны: главная страница, страница отдельной статьи.
* Есть возможность регистрации через форму, вход/выход для пользователя.
* Выкладывание статей, работа с ними (редактирование, удаление).
* Редактировать и удалять статьи может только автор, чтение - доступно всем.
* Приложение имеет API на основе REST API, аутентификация осуществляется при 
помощи JWT-токена. Для неаутентифицированных пользователей доступ к API только 
на чтение.

## Стек технологий
* [Python 3.10.12](https://www.python.org/)
* [Django 5.2](https://www.djangoproject.com/)
* [DRF 3.16](https://www.django-rest-framework.org/)
* [Djoser 2.3.1](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [SQLite3](https://www.sqlite.org/)
* [Pytest](https://docs.pytest.org/en/stable/)

## Как развернуть проект
1. Клонируйте репозиторий и перейдите в директорию SimpleBlog:
```bash
git clone git@github.com:igorKolomitseff/SimpleBlog.git
cd SimpleBlog
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux и macOS
source venv/Scripts/activate  # Для Windows
```

3. Обновите pip и установите зависимости проекта:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейдите в директорию simple_blog и примените миграции:
```bash
cd simple_blog/
python3 manage.py migrate
```

5. Создайте .env файл в директории simple_blog и заполните его данными в соответствии с файлом .env.example

6. Создайте суперпользователя, укажите запрашиваемые данные:
```bash
python3 manage.py createsuperuser
```

6. Запустите проект:
```bash
python3 manage.py runserver
```

Для запуска тестов:
```bash
pytest
```

Откройте браузер и перейдите по адресу 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) для доступа главной странице 
проекта и [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) для 
доступа к административной панели

## Документация API

Техническая документация к API доступна при запущенном проекте по ссылкам:
* [Swagger](http://127.0.0.1:8000/api/schema/swagger-ui/)
* [ReDoc](http://127.0.0.1:8000/api/schema/redoc/)

Документация без развёртывания проекта:

[Техническая документация к API](https://github.com/igorKolomitseff/SimpleBlog/blob/main/docs/openapi.yaml)

### Автор

[Игорь Коломыцев](https://github.com/igorKolomitseff)