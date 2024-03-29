# cookbook
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=5fe620)](https://www.djangoproject.com/)

### Краткое описание:
Web-приложение поварской книги.
В базе данных приложения хранится список продуктов. Продукт имеет название, а также целочисленное поле, хранящее информацию о том, сколько раз было приготовлено блюдо с использованием этого продукта. Также в базе данных хранятся рецепты блюд. Рецепт имеет название, а также набор входящих в рецепт продуктов, с указанием веса в граммах.

### Технологии проекта
* Python — высокоуровневый язык программирования.
* Django — высокоуровневый Python веб-фреймворк, который позволяет быстро создавать безопасные и поддерживаемые веб-сайты.

### Web-приложение предоставляет следующие HTTP функции, получающие параметры методом GET:
* add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.

* cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

* show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.

### Шаблон наполнения .env

```bash
# секретный ключ Django
SECRET_KEY=
```

### Как запустить проект (на Windows):

Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:usdocs/cookbook.git
cd cookbook 
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```

Обновить менеджер пакетов pip:
```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Перейти в каталог с manage.py
```bash
cd cookbook
```

Выполнить миграции:
```bash
python manage.py migrate
```

Запустить проект:
```bash
python manage.py runserver
```

## Примеры работы приложения:

Функция добавления продукта в рецепт.
```bash
http://127.0.0.1:8000/add_product_to_recipe/?recipe_id=1&product_id=2&weight=100
```

Функция увеличения количества приготовленных блюд для каждого продукта, входящего в указанный в параметре рецепт.
```bash
http://127.0.0.1:8000/cook_recipe/?recipe_id=1
```

Функция отображения id и названия всех рецептов, в которых указанный в параметре продукт отсутствует, или присутствует в количестве меньше 10 грамм.
```bash
http://127.0.0.1:8000/show_recipes_without_product/?product_id=1
```

### Разработчик проекта

Автор: Andrey Balakin  
E-mail: [usdocs@ya.ru](mailto:usdocs@ya.ru)