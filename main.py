"""//Import\\"""
import time
from termcolor import *  
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
    def get_up_lvl(self,prev_lvl,new_lvl):
        print(colored(f"У вас повышение уровня!", "light_blue"))
        for i in range(new_lvl):
            prev_lvl+=i
            lvl = colored(f"{prev_lvl}", "magenta")
            if prev_lvl >= new_lvl:
                print(colored(f"ваш уровень: {new_lvl}", 'light_blue', "on_blue"))
                break
            else:
                print(colored(f"ваш уровень: {lvl}", 'light_blue', "on_blue"))
                time.sleep(0.01)
    def __str__(self):
        return (f"hihihih"
                )
    
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
    print("1. Начать игру")
    print("2. Выход")

    choice = int(input("Ваш выбор: "))
    if choice == 1:
        first_thing = Player("Test",
                             100,
                             ["First","poition"],
                             0,)
        print(first_thing.take_damage(12))
        first_thing.get_up_lvl(1,99)
        time.sleep(10)
    elif choice == 27142215:
        print(colored(f"А тут пасхалка :) ", "red", "on_light_red"))
