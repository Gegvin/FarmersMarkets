Class View():
    def __init__(self):
        pass
    def print_promt(self):
        return print('Введите команду (look, find, reviews, end): ')
    def print_command(command):
        return print(command)
    def print_invalid_command(self):
        return print('Такой команды нет!')
    def print_exit(self):
        print("Done")
    def print_search_parameters(self):
        print(('''
    По какому параметру осуществлять поиск?
    1 - Город
    2 - Штат
    3 - Индекс'''))
    def print_incorrect_parameters(self):
        print('''
            Введен некорректный ответ. Повторите попытку.
            По какому параметру осуществлять поиск?
            1 - Город
            2 - Штат
            3 - Индекс''')
    def print_search_city(self):
        print('Введите название города: ')
    def print_search_state(self):
        print('Введите название штата: ')
    def print_search_zip(self):
        print('Введите индекс: ')
    def print_market_info(self, ID, MarketName, zip, State, Country,City, Street, Website, Facebook, Twitter, OtherMedia):
        print(f'''
        Market ID: {ID}
        Market name: "{MarketName}"
        Adress:
            Index: {zip}
            State: {State}
            Country: {Country}
            City: {City}
            Street: {Street}
        Contacts:
            Website: {Website}
            Facebook: {Facebook}
            Twitter: {Twitter}
            Other Media: {OtherMedia}''')

    def print_products_info(self, ID, MarketName, Organic, Bakedgoods, Cheese, Crafts, Flowers, Eggs, Seafood, Herbs,\
    Vegetables, Honey, Jams, Maple, Meat, Nursery, Nuts, Plants, Poultry, Prepared, Soap, Trees, Wine, Coffee, Beans,\
    Fruits, Grains, Juices, Mushrooms, PetFood, Tofu, WildHarvested):
        print(f'''
        Market ID: {ID}
        Market name: "{MarketName}")
        Products:
            Organic: {Organic}
            Bakedgoods: {Bakedgoods}
            Cheese: {Cheese}
            Crafts: {Crafts}
            Flowers: {Flowers}
            Eggs: {Eggs}
            Seafood: {Seafood}
            Herbs: {Herbs}
            Vegetables: {Vegetables}
            Honey: {Honey}
            Jams: {Jams}
            Maple: {Maple}
            Meat: {Meat}
            Nursery: {Nursery}
            Nuts: {Nuts}
            Plants: {Plants}
            Poultry: {Poultry}
            Prepared: {Prepared}
            Soap: {Soap}
            Trees: {Trees}
            Wine: {Wine}
            Coffee: {Coffee}
            Beans: {Beans}
            Fruits: {Fruits}
            Grains: {Grains}
            Juices: {Juices}
            Mushrooms: {Mushrooms}
            PetFood: {PetFood}
            Tofu: {Tofu}
            WildHarvested: {WildHarvested}''')

    def print_user_info(self, name, surname, gender, age, phone_number, email):
        print(f'''
        User Name: {name} 
        User Surname: {surname} 
        Gender: {gender}
        Age: {age}
        Phone Number: {phone_number}
        Email: {email}''')

    def print_gander_choice:
        print('''
        Выберите Ваш пол:
        1 - Мужской
        2 - Женский''')
    def print_incorrect_gander:
        print('''
        Введен некорректный ответ. Повторите попытку.    
        Выберите Ваш пол:
        1 - Мужской
        2 - Женский''')
    def print_age:
        print('Введите возраст')
    def print_number:
        print('Введите номер телефона')
    def print_email:
        print('Введите Email')
    def print_password:
        print('Введите пароль')
    def print_user_exist:
        print('Пользователь с таким номером телефона или Email уже усществует')

if __name__ == "__main__":
    def push(command):
        if command == 'look':
            for market in Main.FERMERS_MARKETS_CLASSES_LIST:
                print(market.show_products())
        elif command == 'find':
            print(Main.search(Main.FERMERS_MARKETS_CLASSES_LIST))
        elif command == 'reviews':
            Main.User.dict_create()
            Main.User.registration()
            Main.Review.dict_create()

    com = ''
    while com != 'end':
        View.print_promt()
        com = input()
        View.print_command(com)
        com = com.strip().lower()
        if com == "look" or com == "find" or com == 'reviews':
            push(com)
        elif com != 'end':
            View.print_invalid_command()
    View.print_exit()
