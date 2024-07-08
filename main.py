from farmers_market import read_file, del_table_info, add_markets_in_class, search
from user_review import User, Review

FERMERS_MARKETS_LIBRARY_NAME = 'Export.csv'

FERMERS_MARKETS_LIST = read_file(FERMERS_MARKETS_LIBRARY_NAME)
FERMERS_MARKETS_LIST = del_table_info(FERMERS_MARKETS_LIST)
FERMERS_MARKETS_CLASSES_LIST = add_markets_in_class(FERMERS_MARKETS_LIST)

def push(command):
    if command == 'look':
        for market in FERMERS_MARKETS_CLASSES_LIST:
            print(market.show_products())
    elif command == 'find':
        print(search(FERMERS_MARKETS_CLASSES_LIST))
    elif command == 'reviews':
        User.dict_create()
        User.registration()
        Review.dict_create()
        # создание и добавление отзывов

com = "" # переменная для команд
while com != 'end':
    com = input('Введите команду (look, find, reviews, end): ')
    com = com.strip().lower()
    if com == "look" or com == "find" or com == 'reviews':
        push(com)
    elif com != 'end':
        print('Такой команды нет!')
print('Done')




