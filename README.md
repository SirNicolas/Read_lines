# About
Веб-сервис для последовательного чтения лога частями в формате json
## Пример лога
{'message': Some message, 'level': DEBUG}

{'message': Some message, 'level': INFO}

## Запуск
### С помощью докера:

docker build -t app ./

docker start -p 8000:8000 app
### Вручную:
#### Установка зависимостей
python pip install -r requirements.txt
#### Создагие тестового лога
python create_test_data.py
#### Запуск сервиса
python server.py
