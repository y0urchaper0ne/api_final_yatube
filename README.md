### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/y0urchaper0ne/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Функционал проекта

Для неавторизованных пользователей доступны GET-запросы по следующим путям:

```
http://127.0.0.1:8000/api/v1/posts
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments
http://127.0.0.1:8000/api/v1/groups
```

Для авторизованных пользователей пользователей доступны POST/GET-запросы по следующим путям:

```
http://127.0.0.1:8000/api/v1/posts
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments
http://127.0.0.1:8000/api/v1/groups
http://127.0.0.1:8000/api/v1/follow
```

Для авторизованных пользователей пользователей-авторов доступны 
POST/GET/PUT/PATCH/DELETE-запросы по следующим путям:

```
http://127.0.0.1:8000/api/v1/posts
http://127.0.0.1:8000/api/v1/posts/<post_id>/comments
http://127.0.0.1:8000/api/v1/groups
http://127.0.0.1:8000/api/v1/follow
```