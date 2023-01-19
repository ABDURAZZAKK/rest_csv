## Первый запуск:

```bash
docker compose up
```


или


Создать виртуальную среду:
``` 
python3 -m venv venv
../rest_csv> . venv/bin/activate
или
../rest_csv> . venv\Scripts\activate 
```

Установить зависимости:
```bash
pip install -r requirements.txt
```

Запустить миграции:
``` bash
python manage.py migrate
```

Создать суперпользователя:
``` bash
python manage.py createsuperuser
```

Запуск:
``` bash
python manage.py runserver
```