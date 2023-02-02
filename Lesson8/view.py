
def login():
    return input('Укажите пользователя\nУчитель/Родитель: ').lower()

def password():
    return input('Введите пароль: ').lower()

def input_class():
    return input('Введите класс: ').upper()

def input_subject():
    return input('Какая дисциплина? ').lower()

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def list_of_mark(journal: dict, studend: str):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def who_answer():
    return input('Введите имя студента для вызова к ответу, либо exit для закрытия журнала\nКто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил: ')

def who_is_absent():
    return input('Нажмите ENTER чтобы продолжить либо\nВведите кто отсутствует? ')

def who_is_your_child():
    return input('Введите имя своего ребёнка: ')
