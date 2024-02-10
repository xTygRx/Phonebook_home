def surname_input():
    return input("Введите фамилию контакта: ").title()
def name_input():
    return input("Введите имя контакта: ").title()
def patronymic_input():
    return input("Введите отчество контакта: ").title()
def phone_input():
    return input("Введите телефон контакта: ")
def address_input():
    return input("Введите адрес(город) контакта: ").title()
def create_contact():
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()
    return f"{surname} {name} {patronymic}: {phone} \n {address}\n \n"

def add_contact():
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(create_contact())

def print_contacts():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contactr_str = file.read()

    contact_list = contactr_str.rstrip().split('\n \n')

    for n, contact in enumerate(contact_list, 1):
        print(n, contact)

def copy_all():

    new_phonebook = input("Введите название нового справочника: ")

    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contactr_str = file.read()

        with open(new_phonebook, "a", encoding="utf-8") as file2:
            for contact in contactr_str:
                file2.write(contact)

    print('Контакты успешно скопированы')
    interface()



def copy_one():

    new_phonebook = input("Введите название нового справочника: ")
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contactr_str = file.read()
        contact_list = contactr_str.rstrip().split('\n \n')
        with open(new_phonebook, "a", encoding="utf-8") as file2:
            print()
            count = 0
            count_for_max = ''
            s = list()
            for n, contact in enumerate(contact_list, 1):
                s.append(contact)
                count += 1
                count_for_max += str(count)
                print(n, contact)
            choice_contact = input('Выберите контакт для копирования: ')
            while  choice_contact not in count_for_max:
                print("некоректный ввод")
                choice_contact = input('Выберите контакт для копирования: ')

            choice_contact = int(choice_contact) - 1
            file2.write(s[choice_contact])
            file2.write('\n')

    print('Контакт успешно скопирован')
    interface()

def search_contact():
    print(
        "Возможные варианты поиска: \n"
        "1. По фамилии \n"
        "2. По имени \n"
        "3. По отчеству \n"
        "4. По телефону \n"
        "5. По адресу (городу)"
    )
    var = input("Выберите вариант действия: ")
    while var not in ('1', '2', '3', '4', '5'):
        print("некоректный ввод")
        var = input("Выберите вариант действия: ")
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contactr_str = file.read()
    contact_list = contactr_str.rstrip().split('\n \n')

    for str_contact in contact_list:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[i_var]:
           print(str_contact)

def copy_contact():
    var = 0
    while var != '4':

        print("Выберите варианты копирования: \n"
              "1. Просмотреть список контактов \n"
              "2. Копировать один контакт \n"
              "3. Копировать все контакты \n"
              "4. Отмена(возврат в главное меню) \n")

        var = input("Выберите вариант действия: ")
        while var not in ('1', '2', '3', '4'):
            print("некоректный ввод")
            var = input("Выберите вариант действия: ")
        print()

        match var:
            case '1':
                print_contacts()
            case '2':
                copy_one()
            case '3':
                copy_all()
            case '4':
                print('Открываю главное меню')
                print()

    print()


def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    var = 0
    while var != '5':

        print(
            "Возможные варианты: \n"
            "1. Добавить контакт \n"
            "2. Вывести на экран \n"
            "3. Поиск контакта \n"
            "4. Копирование контакта \n"
            "5. Выход"
        )
        print()
        var = input("Выберите вариант действия: ")
        while var not in ('1', '2', '3', '4', '5'):
            print("некоректный ввод")
            var = input("Выберите вариант действия: ")
        print()
        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print('Всего наилучшего')
        print()

if __name__ == "__main__":
    interface()
