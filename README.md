# Артем.Афиша - карта интересных мест 
Это проект для создания сайта с картой интересных мест. 

## Как установить

1. Скачайте код
2. Для работы скрипта нужен Python версии не ниже 3.7
3. Установите зависимости, указанные в файле ``requirements.txt`` командой:

 ```pip install -r requirements.txt```
 
4. Создайте файл .env с данными:

```
ALLOWED_HOSTS=разрешенные хосты
DEBUG=False
SECRET_KEY=секретный ключ 
```
5. Примените миграции командой:

```python3 manage.py migrate```

6. Создайте супер-пользователя для доступа к админке Django командой:

```python3 manage.py createsuperuser```


## Начало работы

Для начала запустите сервер командой:

```python3 manage.py runserver```

Для использования карты внесите через админку Django интересные места и вы увидите их на карте!

Попробовать сайт в действии можно по следующей ссылке:

[link](link) 

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

## Автор проекта

Елена Иванова [Leeny_the_bear](https://github.com/leenythebear)