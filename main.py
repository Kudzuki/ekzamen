from jokes import tell_jokes
from mech_mony import merch

def main():
    while True:
        print("Добро пожаловать в Бота-Помощника. Выбери желаемый контент:")
        print("1 - Анекдот \n2 - Купить мерч \n3 - Выход")
        choice = input("Выберите действие 1-3: ")
        if (choice == "1"):
            print(tell_jokes())
        elif (choice == "2"):
            print(merch())
        elif (choice == "3"):
            print("Вы вышли из программы.")
            break
        else:
            print("Вероятно вы сделали неправильный выбор! Попробуйте снова")

if __name__ == "__main__":
    main()
