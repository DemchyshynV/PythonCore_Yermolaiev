"""
реализовать записную книжку покупок:
- каждая запись должна содержать название покупки и ее цену
-сделать менюшку для работы с записной книжкой:
    '1) Создать запись'
    '2) Список все записей'
    '3) Общая сумма всех покупок'
    '4) Самая дорогая покупка'
    '5) Поиск по названию покупки'
    '9) Выход'
- можете придумать свои пункты
"""
notebook = []
while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')

    choice = input("Сделайте свой выбор: ")

    if choice not in '1234569':
        continue

    if choice == '1':
        item = input('Введите название покупки: ')
        cost = int(input('введите цену покупки: '))
        notebook.append({'item': item, 'cost': cost})

    elif choice == '2':
        print()
        for item in notebook:
            print(item)
        print()

    elif choice == '3':
        sum = 0
        print()
        for item in notebook:
            sum += item['cost']
        print('Общая сумма покупок равна ' + str(sum))
        print()

    elif choice == '4':
        if notebook:
            max_dict = {'index': 0, 'cost': 0}
            for i in range(len(notebook)):
                if max_dict['cost'] < notebook[i]['cost']:
                    max_dict['cost'] = notebook[i]['cost']
                    max_dict['index'] = i
            print(notebook[max_dict['index']])
        else:
            print('У вас нет покупок')

    elif choice == '5':
        name = input("Введите название покупки: ")
        for item in notebook:
            if item['item'] == name:
                print(item)
    elif choice == '9':
        break
