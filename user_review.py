import csv
class User:
    def __init__(self, user_info):
        self.name = user_info[0]
        self.surname = user_info[1]
        self.gender = user_info[2]
        self.age = user_info[3]
        self.phone_number = user_info[4]
        self.email = user_info[5]
        self.password = user_info[6]


    def __repr__(self):    # метод, который выводит основную информацию о пользователях
        return(f'''
        User Name: {self.name} 
        User Surname: {self.surname} 
        Gender: {self.gender}
        Age: {self.age}
        Phone Number: {self.phone_number}
        Email: {self.email}''')

    def dict_create(filename='users_dict.csv'):  # создание пользовательской директории
        with open(filename, 'w', encoding="utf-8", newline='') as ud:
            writer = csv.DictWriter(ud, fieldnames=(
            'User_Name', 'User_Surname', 'Gender', 'Age', 'Phone_Number', 'Email', 'Password'))
            writer.writeheader()

    def registration(filename='users_dict.csv'):  # метод, который добавляет нового пользователя в users_dict.csv
        def user_exists(phone_number, email):  # метод, который проверяет, оригинальность телефона и почты
            with open(filename, 'r', encoding="utf-8", newline='') as ud:
                reader = csv.DictReader(ud)
                for row in reader:
                    if row['Phone_Number'] == phone_number or row['Email'] == email:
                        return True
            return False

        user_info = {'User_Name': None, 'User_Surname': None, 'Gender': None, 'Age': None, 'Phone_Number': None,
                     'Email': None, 'Password': None}
        user_info['User_Name'] = (input('Введите имя').title())
        user_info['User_Surname'] = (input('Введите фамилию').title())
        gender_choice = input('''
        Выберите Ваш пол:
        1 - Мужской
        2 - Женский''')
        while gender_choice != '1' and gender_choice != '2':
            gender_choice = input('''
        Введен некорректный ответ. Повторите попытку.    
        Выберите Ваш пол:
        1 - Мужской
        2 - Женский''')
        if gender_choice == '1':
            user_info['Gender'] = 'M'
        else:
            user_info['Gender'] = 'F'
        user_info['Age'] = int(input('Введите возраст'))
        user_info['Phone_Number'] = input('Введите номер телефона')
        user_info['Email'] = input('Введите Email')
        user_info['Password'] = input('Введите пароль')
        if not user_exists(user_info['Phone_Number'], user_info['Email']):
            with open(filename, 'a', encoding="utf-8", newline='') as ud:
                writer = csv.DictWriter(ud, fieldnames=user_info.keys())
                writer.writerow(user_info)
        else:
            print('Пользователь с таким номером телефона или Email уже усществует')


class Review:
    def __init__(self, user_name, user_surname, market_id, rating, comment):
        self.user_name = user_name
        self.user_surname = user_surname
        self.market_id = market_id
        self.rating = rating
        self.comment = comment


    def __repr__(self):
        return (f'''Review:
        User Name: {self.user_name}
        User Surname: {self.user_surname}
        Shop  Id: {self.market_id}
        Rating: {self.rating}
        Comment: {self.comment}''')

    def to_dict(self):
        return {
            'User_Name': self.user_name,
            'User_Surname': self.user_surname,
            'Market_ID': self.market_id,
            'Rating': self.rating,
            'Comment': self.comment
        }

    def dict_create(filename='review_dict.csv'):  # создание директории с рецензиями
        with open(filename, 'w', encoding="utf-8", newline='') as ud:
            writer = csv.DictWriter(ud, fieldnames=('User_Name', 'User_Surname', 'Market_ID', 'Rating', 'Comment'))
            writer.writeheader()

    def add_to_dict(self, filename='review_dict.csv'):  # метод, который записывает рецензию в review_dict.csv
        fieldnames = {'gamer_name': None, 'total_games': 0, 'total_wins': 0, 'gamer_status': None}
        with open(filename, 'a', encoding="utf-8", newline='') as gd:
            writer = csv.DictWriter(gd, fieldnames=('User_Name', 'User_Surname', 'Market_ID', 'Rating', 'Comment'))
            writer.writerow({'User_Name': self.user_name, 'User_Surname': self.user_surname, 'Market_ID': self.market_id, 'Rating': self.rating, 'Comment': self.comment})