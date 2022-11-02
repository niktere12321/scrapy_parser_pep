# Асинхронный парсер PEP

### Описание
В проекте реализован асинхронный парсер [документов PEP](https://peps.python.org/ "Index of Python Enhancement Proposals (PEPs)") на базе фреймворка Scrapy.
Вывод собранной информации осуществляется в два файла ```.csv```:
- файл со списком PEP;
- файл со сводкой по статусам документов.  

Файлы сохраняются в директорию ```results``` в корневой папке проекта.

### Технологии
- Python 3.7.9
- Scrapy 2.5.1

### Запуск проекта
- Клонируйте репозиторий и перейдите в папку проекта:
```
git clone https://github.com/niktere12321/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```
- Установите и активируйте виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Запустите проект командой:
```
scrapy crawl pep
```

---
## Об авторе

Терехов Никита Алексеевич 
