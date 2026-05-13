# Лабораторна робота 9: Регулярні вирази

# Реалізуйте завдання тут
# Лабораторна робота №9
import re

def is_valid_phone(phone: str) -> bool:
    # Видаляємо пробіли, дефіси та дужки
    normalized = re.sub(r'[\s\-\(\)]', '', phone)

    pattern = r'^(?:\+380\d{9}|0\d{9})$'
    return bool(re.fullmatch(pattern, normalized))


# Ввід даних
phone = input("Введіть телефонний номер: ")

# Перевірка
if is_valid_phone(phone):
    print("Рядок є коректним телефонним номером.")
else:
    print("Рядок НЕ є коректним телефонним номером.")