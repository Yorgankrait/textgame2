class Sword:

        # У параметра material указано значение по умолчанию.
    # Параметры со значениями по умолчанию всегда указываются в конце.
    def __init__(self, name, blade_length, grip, material='сталь'):
        self.name = name
        self.blade_length = blade_length
        self.material = material
        self.grip = grip
        print(f'Новый меч {name} выкован!')
    
    def slashing_blow(self):
        ...

    def piercing_strike(self):
        ...

    def sharpen(self):
        ...