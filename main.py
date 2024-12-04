class Player:

    def __init__(self, name, health, inventory, lvl):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.lvl = lvl
        print(f'Новый меч {name} выкован!')
    
    def take_damage(self, take_damage):
        self.health -= take_damage
        return (f'На вас было совершено покушение,вы потеряли {take_damage} хп, у вас осталось {self.health} хп'
                )


    def piercing_strike(self):
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')
class enemy:
    def __init__(self, attack, health, lvl):
        self.attack = attack
        self.health = health
        self.lvl = lvl
        print(f"Перед вами монстр! {self.name} {self.lvl} ур.")

    def attack(self):
        return (f"вам был нанесён урон: {self.attack}")


while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Просмотреть все заметки")
    print("5. Поиск заметок")
    print("6. Выход")

    choice = int(input("Ваш выбор: "))
    if choice == 1:
        first_thing = Player("Test",
                             100,
                             ["First","poition"],
                             0,)
        print(first_thing.take_damage(12))
