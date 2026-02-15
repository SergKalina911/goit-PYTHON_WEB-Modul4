""" Шаблонізатор Jinja 

Але найчастіше ми виконуємо підстановку якихось даних в HTML документі. Наприклад, 
вказаний список person необхідно вивести списком на сторінці html. Основним компонентом 
Jinja є клас Environment.

Коли шаблони зберігаються у файлах, ми створюємо середовище Jinja за допомогою 
FileSystemLoader. Туди ми можемо передати шлях, який вказує на папку наших шаблонів. 
Тепер, замість передачі рядка, ми завантажуємо файл persons.html у якості шаблону.

# файл-шаблон persons.html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<ul>
    {% for person in persons -%}
    <li>{{ person.name }} {{ person.age }}</li>
    {% endfor %}
</ul>
</body>
</html>

Як тільки ваш шаблон завантажено, ви можете використовувати його знову і знову, 
щоб заповнити його вмістом. Наприклад, за допомогою наступного скрипту.

Шаблони є важливим компонентом повнофункціональної веб-розробки. За допомогою Jinja 
можна створювати багаті, повноцінні шаблони, які забезпечують інтерфейс веб-застосунків 
на Python. Але в основному вони використовуються з веб-фреймворками."""

from jinja2 import Environment, FileSystemLoader
# створюємо середовище Jinja, вказуючи папку, де зберігаються шаблони
# (у цьому випадку поточна папка)
env = Environment(loader=FileSystemLoader('.'))
print(env.list_templates())  # виводимо список доступних шаблонів у поточній папці
# завантажуємо шаблон з файлу persons.html
template = env.get_template("persons.html")

# створюємо список осіб, який ми хочемо вивести на сторінці
persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]
# виконуємо рендеринг шаблону, передаючи список осіб як змінну persons
output = template.render(persons=persons, )
# виводимо результат на екран
print(output)
# записуємо результат у новий HTML файл new_persons.html
with open("new_persons.html", "w", encoding='utf-8') as fh:
    fh.write(output)

# В результаті виконання цього скрипту буде створено файл new_persons.html,
# який містить список осіб з їхніми іменами та віком. Ви можете відкрити цей
# файл у веб-браузері, щоб побачити результат. У цьому прикладі ми використовуємо
# цикл for для ітерування по списку persons і виводимо кожну особу у вигляді
# елемента списку (li) з їхніми іменами та віком. Jinja дозволяє легко створювати
# динамічні HTML документи, використовуючи шаблони та дані.
