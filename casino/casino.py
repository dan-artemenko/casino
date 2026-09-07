import random

p = ["да", "yes", "y", "д"]

class casinorandom:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "💎", "⭐"]
        self.name = ""
        self.coin = 10
    def privet(self):
        """приветствие"""
        print("Добро пожаловать в казино")
        print("Как тебя зовут?")
        self.name = input()
        print(f"Рад знакомству, {self.name}")
        print(f'Ваш баланс {self.coin} рублей')
    def baraban(self):
        """логика барабана"""

        while self.coin > 0:
            user = []
            for i in range(0,4):
                drum = random.choice(self.symbols)
                user.append(drum)


            print(f"🎰 На барабане выпало: {user}")
            if len(set(user)) == 1:
                print("Поздравляю ДЖЕКПОТ!")
                
                self.change_coin(50)
            elif len(set(user)) == 2:
                print("Поздравляю!")
                
                self.change_coin(20)
            elif len(set(user)) > 2:
                print("К сожалению вы проиграли")
                self.change_coin(-10)

            print("Продолжаем играть?")
            a = input()
            if a.lower() in p:
                continue
            else:             
                print("пока")
                break
        if self.coin <= 0:
            self.bal()

    def bal(self):
        print(f"К сожалению для вас игра окончена! Ваш баланс равен {self.coin}!")
        print(f"Желаете ли вы {self.name} внести депозит?")
        if input().lower() in p:
            print("На какую сумму?")
            self.coin += int(input())
            self.baraban()
        else:
            print("Удачи!")
    def change_coin(self, amount):
        self.coin += amount 
        if amount < 0:
            print(f"Списано за ставку {abs(amount)} рублей")
            print(f"Ваш баланс {self.coin} рублей")
        else:
            print(f"Начислено{amount} рублей.")
            print(f"Ваш баланс {self.coin} рублей")


    def start(self):
        """запуск"""
        self.privet()

        print(f"готов делать ставки, {self.name}?")
        a = input()

        if a.lower() in p:
            self.baraban()
        else:
            print("Пока")
game = casinorandom()
game.start()