import Main
class View:
    def __init__(self, controller):
        self.controller = controller


    def print_promt():
        return print('Введите команду (look, find, reviews, end): ')
    def print_command(command):
        return print(command)
    def print_invalid_command():
        return print('Такой команды нет!')
    def print_exit():
        print("Done")


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
