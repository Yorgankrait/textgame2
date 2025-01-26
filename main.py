"""Imports"""
import time
from termcolor import *
import os
class Player:

    def __init__(self, name, health, inventory, lvl):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.lvl = lvl
    
    def take_damage(self, take_damage):
        self.health -= take_damage
        return print(colored(f'На вас было совершено покушение,вы потеряли {take_damage} хп, у вас осталось {self.health} хп'
                ,"light_blue"))

    def new_room(self, room_name, loot):
        print(colored(f"Вы попали в комнату: {room_name}", "yellow"))
        time.sleep(1)
        if loot == False:
            print(colored(f"В данной комнате нету лута :(", "yellow"))
        else:
            print(f"В комнате есть лут: {loot}")
    def get_up_lvl(self, prev_lvl, new_lvl):
         self.lvl = new_lvl
         print(colored(f"У вас повышение УР", "light_blue"))
         for i in range(new_lvl):
            prev_lvl+=i
            lvl_color = colored(f"{prev_lvl}", "black", "on_light_cyan")
            if prev_lvl >= new_lvl:
                colored_lvl = colored(new_lvl, "black", "on_light_cyan")
                print(colored(f"ваш УР: {colored_lvl}", 'light_blue', "on_blue"))
                break
            else:
                print(colored(f"ваш УР: {lvl_color}", 'light_blue', "on_blue"))
                time.sleep(0.1)

while True:
    print("\nВыберите действие:")
    print("1. Начать игру")
    print("2. Создатель")
    print("3  Туториал")
    catKilled = False

    choice = int(input("Ваш выбор: "))
    if choice == 1:
        name = input("Введите ваше имя: ")
        plr = Player(name,
                             100,
                             ["First","poition"],
                             0,)
        print(colored(f"Неизвестный: Неужели это наконец-то случилось?", "dark_grey"))
        time.sleep(2)
        print(colored(f"{name}: Что случилось? Кто ты? Где я?", "yellow"))
        time.sleep(2)
        print(colored(f"Неизвестный: Это не важно. Тебе надо выбраться отсюда, а мне надо уйти по делам, так-что удачи тебе","dark_grey"))
        time.sleep(2)
        print(colored(f"{name}: Всмысле? Постой. Как отсюда выбраться? ", "yellow"))
        time.sleep(2)
        print(colored(f"{name}: Надо пойти за ним! ", "yellow"))
        time.sleep(2)
        print(colored(f" Пойти за неизвестным?", "light_blue"))
        choiceR = int(input("Ваш выбор 1 - Идти; 2 - не идти: "))
        if choiceR == 1:
            print(colored(f"Вы побежали за неизвестным,но вам по пути поподается цветок", "light_blue"))
            time.sleep(2)
            print(colored(f"{name}: Хм, красивый цветок", "yellow"))
            time.sleep(2)
            print(colored(f"Хотите потрогать цветок?", "light_blue"))
            choice1 = int(input("1 - Да; 2- нет: "))
            if choice1 == 1:
                print(colored(f"РУКИ УБРАЛ ОТ МЕНЯ Я ВООБЩЕ-ТО ЖИВАЯ!", "dark_grey"))
                time.sleep(2)
                print(colored(f"{name}: ААААААААА, ЧТО ТЫ ТАКОЕ???", "yellow"))
                time.sleep(2)
                print(colored(f"Триш: Вобще-то я живая, меня зовут Триш,", "green"))
                time.sleep(2)
                print(colored(f"Триш: Я тут для того, чтобы рассказать про то, как устроен этот мир", "green"))
                time.sleep(2)
                print(colored(f"Триш: У тебя есть один навык, он называется УР. Что такое УР? Уровель радости конечно!", "green"))
                time.sleep(2)
                print(colored(f"Триш: Чтобы повысить свой УР, тебе надо дотронуться до моих лепестков", "green"))
                time.sleep(2)
                print(colored(f"Дотронуться до лепестков Триш?", "light_blue"))
                choice2 = int(input("1 - Да; 2- нет: "))
                if choice2 == 1:
                    plr.take_damage(12)
                    print(colored(f"Триш: ХАХАХАХ, ТЫ ДУМАЛ,ЧТО ТУТ ВСЁ ЛЕГКО? ТУТ ЛИБО УБИВАЙ ЛИБО БУДЕШЬ УБИТЫМ", "red"))
                    time.sleep(2)
                    print(colored(f"Дать отпор Триш?", "light_blue"))
                    choice3 = int(input("1 - Да; 2- нет: "))
                    if choice2 == 1:
                        print(colored("Вы едва ударили кулаком Триш, как тут-же она распалась на пылинки", "light_blue"))
                        plr.get_up_lvl(1,2)
                        print(colored(f"{name}: Я только-что убил цветка? Это странно, но надо идти дальше", "yellow"))
                    else:
                        print(colored("Триш поняла, что вы беззасчитный и решилаа вас добить", "light_blue"))
                        time.sleep(2)
                        print(colored("ИГРА ОКОНЧЕНА", "light_blue"))
                        exit()
            time.sleep(2)
            print(colored("Вы идёте дальше", "light_blue"))
            time.sleep(2)
            print(colored("Спустя 2 часа долгой ходьбы, вы понимаете, что вы не можете ходить, а за вас ходит система", "light_blue"))
            time.sleep(2)
            print(colored("Магическим образом вы появляетесь в корридоре рядом с котёнком", "light_blue"))
            time.sleep(2)
            print(colored("У котёнка слишком много шерсти, так-что она у него спадает, а потом отростает, бесконечный двигаеть, не так ли?", "light_blue"))
            time.sleep(2)
            print(colored(f"Побить котёнка?", "light_blue"))
            сhoice4 = int(input("1 - Да; 2- нет: "))
            if сhoice4 == 1:
                catKilled = True
                print(colored(f"Какой-же вы живодёр! Но с угрызением совести вы ударили котёнка, а он ударил вас в ответ", "light_blue"))
                time.sleep(2)
                plr.take_damage(6)
                print(colored(f"C ОГРОМНЫМ угрызением совести вы убиваете этого пушистика", "light_blue"))
                plr.get_up_lvl(2,3)
                time.sleep(2)
                print(colored(f"{name}: Воу... Мне это. Нравится? Убивать это ТАК круто!", "yellow"))
            else:
                print(colored(f"Вместо того, чтобы ударить котёнка, вы его гладите, вы ему нравитесь, вы чувствуете, что ваше ХП повышено до полна!", "light_blue"))
                plr.health = 100
                time.sleep(2)
                print(colored(f"{name}: Ладно, мне пора идти котик, удачи тебе!", "yellow"))
                time.sleep(2)
                print(colored(f"Уходя от кота вы задумались, а коты умеют говорить на человечьем языке?", "light_blue"))
            print(colored(f"Идя ещё 2 часа вы находите одинокий домик, вы решаете в него зайти", "light_blue"))
            time.sleep(2)
            print(colored(f"{name}: Тук-тук, есть кто дома?", "yellow"))
            time.sleep(2)
            print(colored(f"К вам подходит большой пёсик, он не похож на фурри", "light_blue"))
            time.sleep(2)
            print(colored(f"Фокс: Привет! Меня зовут Фокс, как ты тут оказался?", "green"))
            time.sleep(2)
            print(colored(f"{name}: Привет, а я {name}, я не помню, как я тут оказался...", "yellow"))
            time.sleep(2)
            print(colored(f"Фокс: Не вешай нос! Если ты ничего не помнишь, то можешь начать всё с чистого листа! Если хочешь, можешь пока-что остаться у меня", "green"))
            time.sleep(2)
            print(colored(f"{name}: Спасибо большое, можно же пойти осмотреться в доме?", "yellow"))
            time.sleep(2)
            print(colored(f"Фокс: Конечно! Я не возражаю, а я пока-что пойду за дровами, ведь зима суровое время!", "green"))
            time.sleep(2)
            print(colored(f"Вы решили осмотреться", "light_blue"))
            time.sleep(2)
            print("У вас есть возможность пойти:")
            print("1. На кухню")
            print("2. В гостинную")
            print("3. В библиотеку")
            print("4. На второй этаж")
            choice5 = int(input("Куда пойдём? "))
            if choice5 == 1:
                print(colored(f"Вы идёте на кухню", "light_blue"))
                time.sleep(2)
                print(colored(f"На кухне вы находите много различных предметов", "light_blue"))
                time.sleep(2)
                print(colored(f"Но на ваш взгляд упал холодильник", "light_blue"))
                print(colored(f"Заглянуть в него?", "light_blue"))
                сhoice6 = int(input("1 - Да; 2- нет: "))
                if сhoice6 == 1:
                    print(colored(f"В холодильнике лежит одна собачья еда", "light_blue"))
                    time.sleep(2)
                    print(colored(f"Компания производящая данную еду называется <Еда для собак Corporation>", "light_blue"))
                    time.sleep(2)
                    print(colored(f"На банке написано: <ЕДА ТОЛЬКО ДЛЯ СОБАК! Гав>", "light_blue"))
                    time.sleep(2)
                print(colored(f"Вы решаете вернуться в двери и дождаться Фокса", "light_blue"))
            elif choice5 == 2:
                print(colored(f"Вы идёте в гостинную", "light_blue"))
                time.sleep(2)
                print(colored(f"В гостинной вы находите большой диван и телевизор, на нём стоит стол", "light_blue"))
                time.sleep(2)
                print(colored(f"Да, на телевизоре стоит стол, а у вас не так?", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы нашли диван на котором вы решили прилечь", "light_blue"))
                time.sleep(2)
                print(colored(f"Спустя время вы вернулись к двери, чтобы дождаться Фокса", "light_blue"))
            elif choice5 == 3:
                print(colored(f"Вы идёте в библиотеку (в таком маленьком доме есть библиотека? Что) ", "light_blue"))
                time.sleep(2)
                print(colored(f"В библиотеке вы нашли книгу: <Как устроен мир Подземелья для чайников. Том 1>", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы видите, что вся полка обставлена этими книгами (их всего 3)", "light_blue"))
                time.sleep(2)
                print(colored(f"Прочитать первый том?", "light_blue"))
                сhoice7 = int(input("1 - Да; 2- нет: "))
                if сhoice7 == 1:
                    print(colored(f"В книге написано: <Если вы увидели человека, то немедленно сообщите королевской страже об этом>", "light_blue"))
                    time.sleep(2)
                    print(colored(f"В недоумении вы читаете дальше", "light_blue"))
                    time.sleep(2)
                    print(colored(f"<Люди очень опсаны! Если вы понимаете, что их УР высокий, то вам стоит бежать КАК МОЖНО БЫСТРЕЕ.>", "light_blue"))
                    time.sleep(2)
                    print(colored(f"Вы закрываете книгу, думая, что это выдумки", "light_blue"))
                    time.sleep(2)
                    print(colored(f"Вы вернулись к двери, чтобы дождаться Фокса", "light_blue"))
            elif choice5 == 4:
                print(colored(f"Вы идёте на второй этаж", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы находите табличку: <Извините, но сегодня второй этаж не работает :p >", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы вернулись к двери, чтобы дождаться Фокса >", "light_blue"))
            else:
                print(colored(f"Вы решили присесть на стул и дождаться Фокса", "light_blue"))
                time.sleep(2)
            print(colored(f"Спустя время к вам приходит Фокс", "light_blue"))
            time.sleep(2)
            print(colored(f"Фокс: Слушай, нам надо по быстрому пойти в одно место, так-что иди за мной", "green"))
            time.sleep(2)
            print(colored(f"Вы следуете за фоксом", "light_blue"))
            time.sleep(2)
            print(colored(f"Фокс: Я не хочу делать из этого трагедию, но мне придёться это сделать", "green"))
            time.sleep(2)
            print(colored(f"Между вами и Фоксом появилось напряжение", "light_blue"))
            time.sleep(2)
            print(colored(f"Фокс аттакует!", "light_blue"))
            plr.take_damage(27)
            print(colored(f"{name}: АЙ! ФОКС, ЗА ЧТО?", "yellow"))
            time.sleep(2)
            print(colored(f"Фокс: Прости, мне придёться убить тебя, либо ты меня, либо я тебя", "green"))
            time.sleep(2)
            print(colored(f"Аттаковать фокса в ответ?", "light_blue"))
            сhoice8 = int(input("1 - Да; 2- нет: "))
            if сhoice8 == 1:
                print(colored(f"Фокс: Ну что-ж, я надеялся на то, что ты добровольно помрёшь, но ты сам этого захотел", "green"))
            else:
                print(colored(f"{name}: ФОКС! ОДУМАЙСЯ", "yellow"))
                time.sleep(2)
                print(colored(f"Фокс молчит", "light_blue"))
            print(colored(f"Фокс продолжает аттаковать вас!", "light_blue"))
            plr.take_damage(24)
            print(colored(f"Подумайте об своей безопастности! Стоит ли аттаковать Фокса в ответ?", "light_blue"))
            сhoice9 = int(input("1 - Да; 2- нет: "))
            if сhoice9 == 1:
                print(colored(f"Вы чувствуете, что осталось аттаковать егё ещё 1 раз", "light_blue"))
                time.sleep(2)
                print(colored(f"Фокс молчит", "light_blue"))
            else:
                print(colored(f"{name}: ПОДУМАЙ ОБ ЭТОМ Я НИЧЕГО НЕ СДЕЛАЛ!", "yellow"))
                if catKilled == True:
                    print(colored(f"Фокс: По дороге домой, я увидел своего кота <Шурика> УБИТОВО!", "green"))
                else:
                    print(colored(f"Фокс: Я не хочу повторить ошибки прошлого...", "green"))
                plr.take_damage(24)
            print(colored(f"У фокса изменилось лицо, его засчита очень ослабла, стоит его убить?", "light_blue"))
            сhoice10 = int(input("1 - Да; 2- нет: "))
            if сhoice10 == 1:
                print(colored(f"Вы убили Фокса!", "light_blue"))
                plr.get_up_lvl(3,10)
                print(colored(f"Ваше ХП наполнено до предела!", "light_blue"))
                plr.health = 100
            else:
                print(colored(f"{name}: ФОКС ПОЖАЛУЙСТА, НЕ ДЕЛАЙ ЭТОГО", "yellow"))
                plr.take_damage(24)
                time.sleep(2)
                print(colored(f"У вас осталось 1 хп...", "light_blue"))
                time.sleep(2)
                print(colored(f"Фокс останавливается", "light_blue"))
                time.sleep(2)
                print(colored(f"Фокс: Ладно, я тебе верю", "green"))
                time.sleep(2)
                print(colored(f"Фокс отдаёт вам банку компании <Еда для собак Corporation> ", "light_blue"))
                time.sleep(2)
                print(colored(f"На банке написано <Еда не только для собак. :3 > ", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы съели всю банку, ваше ХП наполнено до предела", "light_blue"))
                plr.health = 100
                print(colored(f"Фокс: Иди в сторону замка, его трудно не заметить, ты спокойно сможешь войти и попасть на <Суд>", "green"))
                time.sleep(2)
                print(colored(f"{name}: Суд?", "yellow"))
                time.sleep(2)
                print(colored(f"{name}: Над кем?", "yellow"))
                time.sleep(2)
                print(colored(f"Над тобой", "green"))
                time.sleep(2)
            print(colored(f"Набравшись решимости, вы отправляетесь к замку ", "light_blue"))
            time.sleep(2)
            print(colored(f"Спуста ещё 2 часа вы нашли замок, все двери в нём открыты", "light_blue"))
            time.sleep(2)
            print(colored(f"И вы видите длинный корридор с большими колоннами и окнами ", "light_blue"))
            time.sleep(2)
            print(colored(f"{name}: Напоминает одно место, только где я его видел?", "yellow"))
            time.sleep(2)
            print(colored(f"Вы видите странный силуэт, похожий на. Скелета? Что", "light_blue"))
            time.sleep(2)
            print(colored(f"Дойдя до него у вас завязался диалог", "light_blue"))
            time.sleep(2)
            print(colored(f"Снас: Даров, я Снас, ты попал на свой суд.", "green"))
            time.sleep(2)
            print(colored(f"{name}: Всмысле?", "yellow"))
            time.sleep(2)
            print(colored(f"Снас: Помнишь про свой УР? Так-вот.", "green"))
            time.sleep(2)
            print(colored(f"Снас: УР - Это Уровень Резни.", "green"))
            if plr.lvl <= 1:
                time.sleep(2)
                print(colored(f"Снас: Но ты, никого не убивал, так-что ты чист чувак", "green"))
                time.sleep(2)
                print(colored(f"Снас: Короче, тебе стоит пройти дальше по корридору и ты сможешь вернуться домой", "green"))
                time.sleep(2)
                print(colored(f"Вы идёте до конца корридора и видите дверь в белую пустоту", "light_blue"))
                time.sleep(2)
                print(colored(f"Войдя в неё вы просыпаетесь у себя на кровати в обычном мире...", "light_blue"))
                time.sleep(2)
                print(colored(f"{name}: Это был всего лишь сон?", "yellow"))
                time.sleep(2)
                print(colored(f"????: Наверное :) ", "red"))
                time.sleep(2)
                print(colored(f"Игра окончена!", "light_blue"))
                print(colored(f"Вы получили: Хорошую концовку!", "light_blue"))
                print(colored(f"Cпасибо за игру :D", "light_blue"))
                exit()
            else:
                time.sleep(2)
                print(colored(f"Снас: Ты убийца, который любит убивать", "red"))
                time.sleep(2)
                print(colored(f"Снас: Какой чудестный сегодня день", "red"))
                time.sleep(2)
                print(colored(f"Снас: Птички поют", "red"))
                time.sleep(2)
                print(colored(f"Снас: Цветочки благоухают", "red"))
                time.sleep(2)
                print(colored(f"Снас: В такие дни, такие люди как ты", "red"))
                time.sleep(2)
                print(colored(f"Снас: Должны гореть в аду...", "red"))
                time.sleep(2)
                print(colored(f"Не раздумываясь, вы аттакуете снаса первыми", "light_blue"))
                time.sleep(2)
                print(colored(f"Одним ударом вы довобите снаса до полусмерти", "light_blue"))
                time.sleep(2)
                print(colored(f"Снас: Просто, не говори, что я тебя не предупреждал", "red"))
                time.sleep(2)
                print(colored(f"Снас разлетелся на песчинки", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы идёте до конца корридора и видите дверь в белую пустоту", "light_blue"))
                time.sleep(2)
                print(colored(f"Арач: Привет :) ", "red"))
                time.sleep(2)
                print(colored(f"{name}: Кто ты?", "yellow"))
                time.sleep(2)
                print(colored(f"Арач: Я - это ты", "red"))
                time.sleep(2)
                print(colored(f"{name}: Всмысле?", "yellow"))
                time.sleep(2)
                print(colored(f"Арач: Ты пробудил меня из мёртвых", "red"))
                time.sleep(2)
                print(colored(f"{name}: Как?", "yellow"))
                time.sleep(2)
                print(colored(f"Арач: Твоё желание убивать, это и пробудило меня из мёртвых", "red"))
                time.sleep(2)
                print(colored(f"{name}: Что ты хочешь?", "yellow"))
                time.sleep(2)
                print(colored(f"Арач: Давай сотрём этот мир вместе?", "red"))
                time.sleep(2)
                print(colored(f"{name}: Давай!", "yellow"))
                time.sleep(2)
                print(colored(f"Арач достаёт нож", "light_blue"))
                time.sleep(2)
                print(colored(f"Вы аттаковали первым", "light_blue"))
                time.sleep(2)
                print(colored(f"{name}: Прощай... {name}", "red"))
                time.sleep(2)
                print(colored(f"Игра окончена!", "light_blue"))
                print(colored(f"Вы получили: Плохую Концовку", "light_blue"))
                print(colored(f"Cпасибо за игру :D", "light_blue"))
                exit()

        else:
            print(colored(f"Вы решили сидеть на одном месте в надежде на спасение","light_blue"))
            time.sleep(2)
            print(colored(f"Прошёл час","light_blue"))
            time.sleep(2)
            print(colored(f"Прошло 2 часа","light_blue"))
            time.sleep(2)
            print(colored(f"Прошло 4 часа","light_blue"))
            time.sleep(2)
            print(colored(f"Прошло 10 часов, вам это надоедает","light_blue"))
            time.sleep(2)
            print(colored(f"Прошли первые суткии, вы познакомились с пауками","light_blue"))
            time.sleep(2)
            print(colored(f"Прошли вторые сути, вы поссорились с пауками","light_blue"))
            time.sleep(2)
            print(colored(f"Прошло 3 дня и вы умерли от обезвоживания","light_blue"))
            time.sleep(2)
            print(colored(f"КОНЕЦ, А НАДО БЫЛО ИДТИ ЗА НЕЗНАКОМЦЕМ >:D","light_blue"))
            exit()
    elif choice == 2:
        print(
            colored(
                f"Создатель игры: Стёпа | Fiikus.Игра Сделана с любовью <3", 'light_blue', "on_blue"
            )
        )
    elif choice == 3:
        print(
            colored(
                f"В игре есть очень много текста, и его цвет имеет значение"
            )
        )
        print(
            colored(
                f"Жёлтый - Ваши слова", "yellow"
            )
        )
        print(
            colored(
                f"Красный - Враги", "red"
            )
        )
        print(
            colored(
                f"Зелёный - Друзья", "green"
            )
        )
        print(
            colored(
                f"Голубой - Система ", "light_blue"
            )
        )
