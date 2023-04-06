def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read().title())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ').lower()
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ').lower()
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Введите данные для поиска: ')
    print(search(tel_book, data).title())


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def change_data() -> None:
    '''Изменяет значения в справочнике'''
    with open ('book.txt', 'r', encoding='utf-8') as f:
        old_data = f.read()
        print(old_data)
    data = input('Введите данные которые хотите изменить: ')
    new_data = old_data.replace(data, input('Введите новые данные: '), 1)
    with open ('book.txt', 'w') as f:
        f.write(new_data)

def delete_data() -> None:
    '''Удаляет файлы из справочника'''
    with open ('book.txt', 'r', encoding='utf-8') as f:
        old_data = f.read()
        print(old_data)
    data = input('Введите данные которые хотите удалить: ')
    new_data = old_data.replace(data, '', 1)
    with open ('book.txt', 'w') as f:
        f.write(new_data)


# def edited(text: str) -> str:
#     fio = input('Введите ФИО: ')
#     fon = input('Введите номер телефона: ')
#     if len(fio) == 0:
#         fio = text.split(' | ')[0]
#     if len(fon) == 0:
#         fon = text.split(' | ')[1]
#     return f'{fio} | {fon}'


# def change_data() -> None:
#     '''Изменяет значения в справочнике'''
#     with open('book.txt', 'r', encoding='utf-8') as f:
#         changes = f.read()
#         changes = changes.split('\n')
#         # changes = list(enumerate(changes.split('\n')))
#         print(changes)
#     data = input('Введите данные которые хотите изменить: ')
#     changes[changes.index(data)] = edited(data)
#     print(changes)
#     changes = str(changes)
#     with open('book.txt', 'w', encoding='utf-8') as f:
#         f.write(changes)
    

    
# def delete_data() -> None:
#     '''Удаляет файлы из справочника'''
#     with open('book.txt', 'r', encoding='utf-8') as f:
#         changes = f.read()
#         changes = changes.split('\n')
#         print(changes)
#     data = input('Введите данные которые хотите удалить: ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # data = input('Введите данные которые хотите изменить: ').lower()
    # with open('book.txt', 'r', encoding='utf-8') as f:
    # 	changes_book = f.read()
# print(changes)
#     changes2 =  list(enumerate(changes, 1))
#     print(changes2)
