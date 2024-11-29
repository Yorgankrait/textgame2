class test:
    def __init__(self,name,item,hp):
        self.name = name
        self.item = item
        self.hp = hp
        print(f"очень прятно {name} ваши предметы {item}")
    def __str__(self):
        return(
                f"у вас теперь {self.hp} хп"
            )
a = test(
    "Fiikus",
    "Меч",
    100
)
print(a)
