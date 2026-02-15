""" Шаблонізатор Jinja

Щоб відрендерити шаблон, у нього потрібно викликати метод render та 
передати туди набір іменованих аргументів. Важливо, щоб імена аргументів 
у шаблоні і ті, які передали, збігалися. Ще один важливий момент, Jinja 
сприймає звернення до атрибутів елемента через крапку всередині шаблону 
та звернення до елементів словника через квадратні дужки як одне й те саме:"""

from jinja2 import Template

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

rows_tmp = Template("""{% for person in persons -%}
    {{ person.name }} {{ person.age }}
{% endfor %}""")

print(rows_tmp.render(persons=persons))
