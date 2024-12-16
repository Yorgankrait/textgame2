class Sword:

    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        # Задаём стартовую прочность для всех мечей (всех объектов).
        self.strength = 100
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return (f'Нанесён рубящий удар мечом {self.name}. '
                f'Радиус поражения: {self.blade_length}.')

    def piercing_strike(self):
        # При пронзающем ударе уменьшаем прочность меча на 5.
        self.strength -= 5
        return (f'Нанесён пронзающий удар мечом {self.name}. '
                f'Рукоять {self.grip} мягко легла в руку.')

    def sharpen(self):
        # При заточке меча восстанавливаем стартовую прочность меча.
        self.strength = 100
        return (f'Меч "{self.name}" заточен,'
                f' {self.material} отлично поддалась обработке.')


# Создаём экземпляр класса: меч Верный.
katana = Sword('Верный', 1.5,
               'под хват двумя руками')
# Создаём ещё один экземпляр класса: меч Дежурный.
classic_sword = Sword('Дежурный', 1.2,
                      'под хват одной рукой')

# Наносим один удар мечом Верный.
print(katana.slashing_blow())

# Наносим серию ударов мечом Дежурный.
for i in range(5):
    print(classic_sword.piercing_strike())

# После атак узнаём прочность мечей.
print(katana.strength)
print(classic_sword.strength)