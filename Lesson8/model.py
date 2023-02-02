journal = {}
subject = ''
path = ''
password = 'password'
all_subjects = 'математика информатика русский язык'
student = ''

#TODO добавить проверку посещаемости


def set_class(classes_path: str):
    global path
    path = 'Lesson8\\' + classes_path + '.txt'

def set_subject(our_subject: str):
    global subject
    subject = our_subject

def check_password(u_password: str):
    global password
    if u_password == password:
        return True
    else:
        print('Неверный пароль!!')
        return False
    
def set_student(student_name: str):
    global student
    student = student_name
    
def set_absent(student_name: str):
    if student_name in journal and student_name != 'next':
        journal[student_name].append('н')
        print('Отметка поставлена! ')
        return True
    else:
        return False




def open_file():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(str, study.split(':')[1].split()))

def student_mark(student: str, mark: int):
    marks = list(journal.get(student))
    marks.append(mark)
    journal[student] = marks

def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
            item = []
            for student, marks in journal.items():
                item.append(student + ':' + ' '.join(list(map(str, marks))))
            item = subject + ';' + ', '.join(item)
            new_file.append(item)
            with open(path, 'w', encoding='UTF-8') as data:
                data.write('\n'.join(new_file))


def get_student():
    return student

def get_journal():
    return journal

