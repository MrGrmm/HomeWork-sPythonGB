import view
import model
import os

def start():
    user = view.login()
    if user == 'учитель':
        if model.check_password(view.password()):
            while True:
                model.set_class(view.input_class())
                if os.path.exists(model.path):
                    while True:
                        model.set_subject(view.input_subject())
                        if model.subject in model.all_subjects:
                            model.open_file()
                            while True:         
                                absent = view.who_is_absent()                       
                                if model.set_absent(absent):
                                    continue
                                elif absent == '':
                                    break
                                else:
                                    print('Неправильный ввод')
                            while True:
                                journal = model.get_journal()
                                view.list_of_child(journal)
                                student = view.who_answer()
                                if student == 'exit':
                                    model.save_file()
                                    exit()
                                elif student not in journal:
                                    print('Такого студента нет в этом классе!!\nВнимательно прочтите список учеников:')
                                    continue
                                while True:
                                    mark = int(view.what_mark())
                                    if 0 < mark < 6:
                                        model.student_mark(student, mark)
                                        model.save_file()
                                        break
                                    else:
                                        print('Оценки могут быть от 1 до 5 включительно! ')
                                        continue
                                    
                        else:
                            print('Такой дисциплины нет!!')
                            continue
                else:
                    print('Такого класса нет!!')
                    continue
        else:
            start()
    elif user == 'родитель':
        model.set_class(view.input_class())
        model.set_student(view.who_is_your_child())
        model.open_file()
        journal = model.get_journal()
        student = model.get_student()
        model.get_student_marks('Lesson8\\7B.txt' ,student)

    else:
        print('Неправильный ввод')
        start()

