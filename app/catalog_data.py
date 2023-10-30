from enum import Enum


class Categories(Enum):
    romantic = 'про любов'
    fantasy = 'фантастика'
    # SEAFOOD = 'з морепродуктами'


menu = [
    {
        'title': 'Дівчина онлайн. Всі 3 книги.(Зої Загг)',
        'image': 'book1.png',
        'price': 820,
        'categories': [Categories.romantic.value]
    },
    {
        'title': 'Галант. (В.Е. Шваб)',
        'image': 'book2.png',
        'price': 500,
        'categories': [Categories.fantasy.value]
    },
    {
        'title': 'Енн. 8 книг(Люсі Мод Монтгомері',
        'image': 'book3.png',
        'price': 1300,
        'categories': [Categories.romantic.value]
    },
    {
        'title': 'Незриме життя Аді Лярю. (В.Е. Шваб)',
        'image': 'book4.png',
        'price': 500,
        'categories': [Categories.romantic.value, Categories.fantasy.value]
    },
    {
        'title': '9 листопада. (Коллін Гувер)',
        'image': 'book5.png',
        'price': 420,
        'categories': [Categories.romantic.value]
    },
    {
        'title': 'Серце часу. 3 книга.(Моніка Лец)',
        'image': 'book6.png',
        'price': 300,
        'categories': [Categories.romantic.value, Categories.fantasy.value]
    },
    {
        'title': 'Серце часу. 1 книга.(Моніка Лец)',
        'image': 'book7.png',
        'price': 300,
        'categories': [Categories.romantic.value, Categories.fantasy.value]
    },
    {
        'title': 'Серце часу. 2 книга.(Моніка Лец)',
        'image': 'book8.png',
        'price': 300,
        'categories': [Categories.romantic.value, Categories.fantasy.value]
    },
    {
        'title': 'Тисячу памя"тних поцілунків(Тілі Коул)',
        'image': 'book9.png',
        'price': 400,
        'categories': [Categories.romantic.value]
    },
    {
        'title': 'Шпигунки з притулку Артеміда(Наталія Довгопол)',
        'image': 'book10.png',
        'price': 200,
        'categories': [Categories.fantasy.value]
    },
    {
        'title': 'Наші приховані дари(Керолайн О"дногіо)',
        'image': 'book11.png',
        'price': 300,
        'categories': [Categories.fantasy.value]
    },
    {
        'title': 'Локвуд&Ко (Джонатан Страуд)',
        'image': 'book12.png',
        'price': 300,
        'categories': [Categories.fantasy.value]
    },
]
