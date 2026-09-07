import random


print("Добро пожаловать в казино")
print("Как тебя зовут?")
name = input()
print(f"Рад знакомству, {name}")
coin = 100
print(f'Ваш баланс {coin}')
print(f"готов делать ставки, {name}?")
a = input()
symbols = ["🍒", "🍋", "💎", "⭐"]
def casino_game():
    user = []
    for i in range(0,3):
        drum = random.choice(symbols)
        user.append(drum)


    print(f"🎰 На барабане выпало: {user}")
if a == "да":
    casino_game()
    
