def generate_password(n):
    result = ""
    for i in range(1, 21):
        for j in range(i, 21):
            if n % (i + j) == 0 and i != j:
                result += str(i) + str(j)
    return result

while True:
    n = int(input("Введите число от 3 до 20: "))
    if 3 <= n <= 20:
        password = generate_password(n)
        print(f"Нужный пароль для {n}: {password}")
        break
    else:
        print("Число вне диапазона")
        continue
