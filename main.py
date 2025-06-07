from functions import is_palindrome, generate_password, factorial, add_numbers

def main():
    print("Добро пожаловать! Проверим ваши данные и подготовим их к регистрации.")

    # 1. Проверка имени на палиндром
    name = input("Введите ваше имя: ")
    if is_palindrome(name):
        print("Ваше имя — палиндром! Это интересно!")
    else:
        print("Ваше имя — не палиндром.")

    # 2. Генерация пароля
    length = int(input("Введите длину пароля (рекомендуется от 8): "))
    password = generate_password(length)
    print("Ваш пароль:", password)

    # 3. Проверка сложности пароля (по длине — факториал, для примера)
    # Например, если длина пароля — 8, то считаем факториал 8 для интереса
    print("Для длины пароля", length, "факториал:", factorial(length))

    # 4. Сложение чисел для кода подтверждения
    a = int(input("Введите первое число для кода подтверждения: "))
    b = int(input("Введите второе число для кода подтверждения: "))
    code = add_numbers(a, b)
    print("Ваш код подтверждения:", code)

    print("Регистрация завершена!")

if __name__ == "__main__":
    main()
