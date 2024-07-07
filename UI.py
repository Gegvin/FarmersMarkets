
com = "" #переменная для команд
#Выбор комманды
while com != 'end':
    com = input('Введите команду (look, find, reviews, end): ')
    com = com.strip().lower()
    if com == "look" or com == "find" or com == 'reviews':
        push(com)
    elif com != 'end':
        print ('Такой команды нет!')
print('Done')


