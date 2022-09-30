# Пульт охраны банка

Это сайт, который показывает охраннику все активные карты доступа. Также сайт показывает, кто находитя в хранилище и все визиты человека.

### Как установить

Все ключи для подключения к базе данных хранилища уже вшиты в код. 

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

Чтобы запустить сайт, нужно ввести команду:
```powershell
python main.py runserver
```
Далее переходим на адрес: `http://127.0.0.1:8000/`. Там и будет наш пульт охраны.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
