# weather_web

Порядок становки:  

1 - клонировать проект на рабочий стол (git clone https://github.com/Tig-Lakt/weather_web)  
2 - устанавливить зависимости (pip install -r requirements.txt)  
3 - в папке проекта web_weather (возле файла manage.py) создать файл .env с переменной WEATHER_API_KEY="YOUR_API_KEY"  
4 - создать миграции - python manage.py makemigrations  
5 - применить миграции - python manage.py migrate  
6 - запустить проект - python manage.py runserver  

В проекте использованы:  
1 - фреймворк Django  
2 - библиотека requests для запросов к http://api.weatherapi.com  
3 - django-environ для работы с переменными окружения  

Для хранения истории запросов используется простая таблица в sqlite3, для хранения сессий пользователя можно использовать PostgreSQL
