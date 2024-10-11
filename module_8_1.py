def add_everything_up(a, b):
    # Если a и b разных типов, возвращаем их строковое представление
    if type(a) != type(b):
        return str(a) + str(b)
    else:
        return a + b

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Результат: "123.456строка"
print(add_everything_up('яблоко', 4215))     # Результат: "яблоко4215"
print(add_everything_up(123.456, 7))         # Результат: 130.456
