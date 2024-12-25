from task1.models import Buyer, Game
from django.db import transaction

# Создаем покупателей
with transaction.atomic():
    buyer1 = Buyer.objects.create(name="Alice", balance=1000.00, age=25)
    buyer2 = Buyer.objects.create(name="Bob", balance=500.00, age=17)  # Младше 18
    buyer3 = Buyer.objects.create(name="Charlie", balance=750.00, age=30)

# Создаем игры
with transaction.atomic():
    game1 = Game.objects.create(title="Adventure Quest", cost=49.99, size=5.2, description="An exciting adventure game", age_limited=12)
    game2 = Game.objects.create(title="Puzzle Master", cost=29.99, size=2.1, description="A challenging puzzle game", age_limited=0)  # Без ограничения возраста
    game3 = Game.objects.create(title="Space Shooter", cost=39.99, size=3.7, description="An action-packed space game", age_limited=16)

# Связываем игры с покупателями
with transaction.atomic():
    # Alice владеет всеми играми
    game1.buyer.set([buyer1, buyer3])
    game2.buyer.set([buyer1, buyer2, buyer3])  # Bob может играть в эту игру, так как она без возрастного ограничения
    game3.buyer.set([buyer1, buyer3])  # Bob не может играть в эту игру из-за возрастного ограничения

print("Data created successfully!")

