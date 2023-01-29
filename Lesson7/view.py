def main_menu() -> int:
    print('\tГлавное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Найти контакт',
                 'Выход'
                 ]
    for i, item in enumerate(menu_list):
        print(f'\t\t{i + 1}. {item}')
    while True:
        try:
            user_input = int(input('\tВведи команду >: '))
            print()
            break
        except:
            print('ERROR ')
    return user_input




def contact_selection(db):
    show_all(db)
    while True:
        try:
            u_input = int(input('\tВыбери контакт по номеру: ')) - 1
            if u_input <= len(db):
                return u_input 
            else:
                print('Номер контакта указан перен firstname')
        except:
            print('Необходимо ввести именно номер')
           
def feed_back():
    inp = input('\t\tНажмите ENTER чтобы продолжить работу с книжкой\n\t\tЛибо напишите q чтобы закончить работу с программой\n\t: ')
    if inp == 'q':
        exit_program()
    elif inp == '':
        print()
    else:
        feed_back()
 
def db_success(db: list):
    if db:
        return True
    else:
        print('\tТелефонная книга пуста или не открыта\n')
        return False




def show_all(db: list):
        if not db:
            print('\t\tКнига закрыта или контактов нет')
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()
        print()

def save_db(new_db, path):
    if db_success(new_db):
        with open(path, 'w') as file:
            for item in new_db:
                file.write(f"{item['lastname']};{item['firstname']};{item['phone']};{item['comment']}\n")
        print('\tФайл сохранён')  


def create_contact(db):
    if db_success(db):
        print('\tСоздание нового контакта.')
        new_contact = dict()

        new_contact['lastname'] = input('\t\tВведите фамилию >: ')
        new_contact['firstname'] = input('\t\tВведите имя >: ')
        new_contact['phone'] = input('\t\tВведите телефон >: ')
        new_contact['comment'] = input('\t\tВведите комментарий >: ')
        feed_back()
        return new_contact

def edit_contact(db):
    if db_success(db):
        u_input = contact_selection(db)
        for key, value in db[u_input].items():
            print(f'Последнее значение:  {key}:  {value}')
            new_value = input(f'\tВведите новое значение для {key}: ')            
            db[u_input][key] = new_value            

def delete_contact(db):
    if db_success(db):
        u_input = int(contact_selection(db))
        db.remove(db[u_input])
        print('\tContact is deleted')
    feed_back()

def find_contact(db):
    if db_success(db):
        find = input('\tВведите имя/фам/номер: ')
        print()
        flag = True
        for i, item in enumerate(db):
            if find in item.values():
                print('\tНомер находится под индексом:', i + 1, item, '\n')
                flag = False
        if flag:
            print('\tТакого контакта нет\n')
    feed_back()     

def exit_program():
    print('\tЗавершение программы.')
    exit()







