import time
import random
print ()
print("Игра: Камень, Ножницы, Бумага")
print("-------------------------------")
time.sleep(2) # Команда из интернета для паузы
print()
print("▎Правила игры:")
print ("1. Игроки: Играют два игрока или один игрок против компьютера.")
time.sleep(2)
print ("2. Выбор: Каждый игрок одновременно выбирает один из трех вариантов: камень, ножницы или бумагу.")
time.sleep(3)
print ("3. Правила выигрыша:")
print ("• Камень (🪨) побеждает ножницы (✂️).")
print ("• Ножницы (✂️) побеждают бумагу (📄).")
print ("• Бумага (📄) побеждает камень (🪨).")
time.sleep(5)
print ("4. Ничья: Если оба игрока делают одинаковый выбор, игра заканчивается ничьей.")
time.sleep(3)
print ("5. Цель: Победить противника, выбрав вариант, который сильнее его выбора.")
time.sleep(3)
print("""         ▎      ▎           /\             ▎      ▎             ▎       ▎              ▎------           ▎\    /▎
         ▎______▎          /__\            ▎_____ ▎             ▎______ ▎              ▎______           ▎  \ / ▎
         ▎      ▎         /    \                  ▎             ▎       ▎              ▎                 ▎      ▎
         ▎      ▎        /      \                 ▎             ▎       ▎              ▎ -----           ▎      ▎""")

print("------------------------------------------------------------------------------------------------------------------")
print ()
mode = input("Выберите режим игры (1 - против компьютера, 2 - против другого игрока): В соответствии с режимом напишите цифру 1/2 ")

if mode == '1':
    print("Вы играете против компьютера.")
    choices = ['камень', 'ножницы', 'бумага']

    while True:
        player_choice = input("Выберите: (Камень, Ножницы, Бумага) или введите 'выход' для завершения игры: ").lower() #Данная структура позволяет принимать на вход например Камень как камень
        if player_choice == 'выход':
            print("Спасибо за игру!")
            break
        if player_choice not in choices:
            print("Неверный ввод. Попробуйте снова.")
            continue #Данная часть кода позволяет проверять ввод пользователя и давать возможность ввести еще раз при ошибке

        computer_choice = random.choice(choices)
        print(f"Вы выбрали : {player_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        if player_choice == computer_choice:
            print("Ничья!")
        elif ((player_choice == 'камень' and computer_choice == 'ножницы') or
                  (player_choice == 'ножницы' and computer_choice == 'бумага') or
                  (player_choice == 'бумага' and computer_choice == 'камень')):
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

elif mode == '2': #Второй режим игры
    print("Вы играете против другого игрока.")
    choices = ['камень', 'ножницы', 'бумага']
    while True:
        player1_choice = input("Игрок 1, выберите (Камень, Ножницы, Бумага) или 'выход' для завершения: ").lower()
        if player1_choice == 'выход':
            print("Спасибо за игру!")
            break
        if player1_choice not in choices:
            print("Неверный ввод. Попробуйте снова.")
            continue
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        # print  пустой, чтобы игрок 1 не увидел, что ввел игрок 2
        player2_choice = input("Игрок 2, Выберите: (Камень, Ножницы, Бумага): ").lower() #Данная структура позволяет принимать на вход например Камень как камень
        if player1_choice == 'выход': #Данная структура позволяет любому из пользователей в любой момент игры закончить ее
            print("Спасибо за игру!")
            break
        if player2_choice not in choices:
            print("Неверный ввод. Попробуйте снова.")
            continue

        print(f"Игрок 1 выбрал: {player1_choice}")
        print(f"Игрок 2 выбрал: {player2_choice}")

        if player1_choice == player2_choice:
            print("Ничья!")
        elif (player1_choice == 'камень' and player2_choice == 'ножницы') or \
                (player1_choice == 'ножницы' and player2_choice == 'бумага') or \
                (player1_choice == 'бумага' and player2_choice == 'камень'):
            print("Игрок 1 выиграл!")
        else:
            print("Игрок 2 выиграл!")

else:
    print("Неверный режим игры. Пожалуйста, перезапустите программу и выберите 1 или 2.") #Данная структура позволяет при некорректном вводе режима сделать выбор режима повторно
