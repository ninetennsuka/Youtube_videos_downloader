#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор случайных данных
Создает тестовые данные для разработки
"""

import random
import string
from datetime import datetime, timedelta
import json

class DataGenerator:
    def __init__(self):
        self.first_names_male = ["Александр", "Максим", "Артем", "Дмитрий", "Никита", "Илья", "Андрей", "Роман", "Сергей", "Владимир"]
        self.first_names_female = ["Анна", "Мария", "Елена", "Ольга", "Екатерина", "Татьяна", "Наталья", "Ирина", "Светлана", "Юлия"]
        self.last_names = ["Иванов", "Петров", "Сидоров", "Козлов", "Смирнов", "Попов", "Соколов", "Лебедев", "Козлов", "Новиков"]
        self.domains = ["gmail.com", "yandex.ru", "mail.ru", "yahoo.com", "outlook.com"]
        self.cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань", "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону"]
        self.companies = ["ТехноСофт", "ИнноваЛаб", "ДигиталПро", "СмартСистемс", "ФьючерТек", "МегаДев", "КодЛаб", "ИТ-Решения", "ТехноВейв", "СофтВорк"]

    def generate_name(self, gender=None):
        """Генерирует случайное имя"""
        if gender == "male":
            first_name = random.choice(self.first_names_male)
        elif gender == "female":
            first_name = random.choice(self.first_names_female)
        else:
            first_name = random.choice(self.first_names_male + self.first_names_female)
        
        last_name = random.choice(self.last_names)
        return f"{first_name} {last_name}"

    def generate_email(self, name=None):
        """Генерирует email адрес"""
        if name:
            username = name.lower().replace(" ", ".").replace("ё", "e")
        else:
            username = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        
        domain = random.choice(self.domains)
        return f"{username}@{domain}"

    def generate_phone(self):
        """Генерирует телефонный номер"""
        return f"+7{''.join(random.choices(string.digits, k=10))}"

    def generate_password(self, length=12):
        """Генерирует случайный пароль"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=length))

    def generate_date(self, start_year=1990, end_year=2025):
        """Генерирует случайную дату"""
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)
        
        time_between = end_date - start_date
        days_between = time_between.days
        random_days = random.randrange(days_between)
        
        return start_date + timedelta(days=random_days)

    def generate_address(self):
        """Генерирует адрес"""
        city = random.choice(self.cities)
        street = f"ул. {random.choice(['Ленина', 'Пушкина', 'Гагарина', 'Советская', 'Центральная'])}"
        house = random.randint(1, 200)
        apartment = random.randint(1, 100)
        
        return f"{city}, {street}, д. {house}, кв. {apartment}"

    def generate_lorem_ipsum(self, words_count=50):
        """Генерирует Lorem Ipsum текст"""
        lorem_words = [
            "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
            "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
            "magna", "aliqua", "enim", "ad", "minim", "veniam", "quis", "nostrud",
            "exercitation", "ullamco", "laboris", "nisi", "aliquip", "ex", "ea", "commodo",
            "consequat", "duis", "aute", "irure", "in", "reprehenderit", "voluptate",
            "velit", "esse", "cillum", "fugiat", "nulla", "pariatur", "excepteur", "sint"
        ]
        
        text = []
        for _ in range(words_count):
            text.append(random.choice(lorem_words))
        
        return ' '.join(text).capitalize() + '.'

    def generate_user_data(self, count=1):
        """Генерирует данные пользователей"""
        users = []
        for _ in range(count):
            gender = random.choice(["male", "female"])
            name = self.generate_name(gender)
            
            user = {
                "id": random.randint(1000, 9999),
                "name": name,
                "email": self.generate_email(name),
                "phone": self.generate_phone(),
                "gender": gender,
                "birth_date": self.generate_date(1970, 2005).strftime("%Y-%m-%d"),
                "address": self.generate_address(),
                "company": random.choice(self.companies),
                "salary": random.randint(30000, 150000),
                "registration_date": self.generate_date(2020, 2025).strftime("%Y-%m-%d")
            }
            users.append(user)
        
        return users

    def generate_product_data(self, count=1):
        """Генерирует данные товаров"""
        products = []
        categories = ["Электроника", "Одежда", "Книги", "Спорт", "Дом", "Красота"]
        
        for _ in range(count):
            product = {
                "id": random.randint(100, 9999),
                "name": f"Товар {random.randint(1, 1000)}",
                "category": random.choice(categories),
                "price": round(random.uniform(100, 50000), 2),
                "in_stock": random.randint(0, 100),
                "rating": round(random.uniform(1, 5), 1),
                "description": self.generate_lorem_ipsum(20)
            }
            products.append(product)
        
        return products

    def generate_json_data(self, data_type, count):
        """Генерирует данные в JSON формате"""
        if data_type == "users":
            return self.generate_user_data(count)
        elif data_type == "products":
            return self.generate_product_data(count)
        else:
            return []

def main():
    generator = DataGenerator()
    
    print("=== ГЕНЕРАТОР ТЕСТОВЫХ ДАННЫХ ===\n")
    
    while True:
        print("1. Случайное имя")
        print("2. Email адрес")
        print("3. Телефон")
        print("4. Пароль")
        print("5. Дата")
        print("6. Адрес")
        print("7. Lorem Ipsum")
        print("8. Данные пользователей (JSON)")
        print("9. Данные товаров (JSON)")
        print("10. Выход")
        
        choice = input("\nВыберите тип данных: ")
        
        if choice == "1":
            gender = input("Пол (male/female/любой): ").lower()
            gender = gender if gender in ["male", "female"] else None
            name = generator.generate_name(gender)
            print(f"👤 Имя: {name}")
            
        elif choice == "2":
            name = input("Имя для email (или Enter для случайного): ")
            name = name if name else None
            email = generator.generate_email(name)
            print(f"📧 Email: {email}")
            
        elif choice == "3":
            phone = generator.generate_phone()
            print(f"📱 Телефон: {phone}")
            
        elif choice == "4":
            try:
                length = int(input("Длина пароля (по умолчанию 12): ") or "12")
                password = generator.generate_password(length)
                print(f"🔒 Пароль: {password}")
            except ValueError:
                print("❌ Некорректная длина")
                
        elif choice == "5":
            try:
                start_year = int(input("Начальный год (по умолчанию 1990): ") or "1990")
                end_year = int(input("Конечный год (по умолчанию 2025): ") or "2025")
                date = generator.generate_date(start_year, end_year)
                print(f"📅 Дата: {date.strftime('%d.%m.%Y')}")
            except ValueError:
                print("❌ Некорректный год")
                
        elif choice == "6":
            address = generator.generate_address()
            print(f"🏠 Адрес: {address}")
            
        elif choice == "7":
            try:
                words = int(input("Количество слов (по умолчанию 50): ") or "50")
                text = generator.generate_lorem_ipsum(words)
                print(f"📝 Текст: {text}")
            except ValueError:
                print("❌ Некорректное количество слов")
                
        elif choice == "8":
            try:
                count = int(input("Количество пользователей: ") or "5")
                users = generator.generate_user_data(count)
                
                print(f"\n👥 ДАННЫЕ ПОЛЬЗОВАТЕЛЕЙ ({count})")
                print("=" * 40)
                for user in users:
                    print(f"ID: {user['id']}")
                    print(f"Имя: {user['name']}")
                    print(f"Email: {user['email']}")
                    print(f"Компания: {user['company']}")
                    print("-" * 20)
                
                save = input("Сохранить в JSON файл? (y/n): ")
                if save.lower() == 'y':
                    filename = input("Имя файла: ") or "users.json"
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(users, f, ensure_ascii=False, indent=2)
                    print(f"✅ Данные сохранены в {filename}")
                    
            except ValueError:
                print("❌ Некорректное количество")
                
        elif choice == "9":
            try:
                count = int(input("Количество товаров: ") or "5")
                products = generator.generate_product_data(count)
                
                print(f"\n🛍️ ДАННЫЕ ТОВАРОВ ({count})")
                print("=" * 40)
                for product in products:
                    print(f"ID: {product['id']}")
                    print(f"Название: {product['name']}")
                    print(f"Цена: {product['price']} руб.")
                    print(f"Рейтинг: {product['rating']}")
                    print("-" * 20)
                
                save = input("Сохранить в JSON файл? (y/n): ")
                if save.lower() == 'y':
                    filename = input("Имя файла: ") or "products.json"
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(products, f, ensure_ascii=False, indent=2)
                    print(f"✅ Данные сохранены в {filename}")
                    
            except ValueError:
                print("❌ Некорректное количество")
                
        elif choice == "10":
            break
            
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
