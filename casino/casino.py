import random
class casinorandom:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "💎", "⭐"]
        self.name = ""
        self.coin = 100
    def privet(self):
        """приветствие"""
        print("Добро пожаловать в казино")
        print("Как тебя зовут?")
        self.name = input()
        print(f"Рад знакомству, {self.name}")
        print(f'Ваш баланс {self.coin}')
    def baraban(self):
        """логика барабана"""
        user = []
        for i in range(0,3):
            drum = random.choice(self.symbols)
            user.append(drum)

        print(f"🎰 На барабане выпало: {user}")
    def start(self):
        """запуск"""
        self.privet()

        print(f"готов делать ставки, {self.name}?")
        a = input()

        if a == "да":
            self.baraban()
game = casinorandom()
game.start()