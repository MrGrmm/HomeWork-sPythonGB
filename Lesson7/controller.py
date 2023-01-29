import model
import view


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('DataForLes7.txt')
            view.db_success(model.db_list)
        case 3:
            view.save_db(model.db_list, 'DataForLes7.txt')
        case 4:
            model.db_list.append(view.create_contact(model.db_list))
        case 5:
            view.edit_contact(model.db_list)
        case 6:
            view.delete_contact(model.db_list)
        case 7:
            view.find_contact(model.db_list)
        case 8:
            view.exit_program()

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
