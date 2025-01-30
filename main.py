"""Imports"""
import time
from termcolor import *
import os
import json

# Константы
DIALOG_DELAY = 2
COLORS = {
    'player': 'yellow',
    'system': 'light_blue',
    'enemy': 'red',
    'friend': 'green',
    'unknown': 'dark_grey'
}

# Добавим новые константы
SAVE_FILE = "game_save.json"
SAVE_POINTS = {
    'start': 'Начало игры',
    'flower': 'Встреча с цветком',
    'cat': 'Встреча с котом',
    'fox_house': 'Дом Фокса',
    'fox_battle': 'Битва с Фоксом'
}

class Achievements:
    def __init__(self):
        self.achievements = {
            'pacifist': {
                'name': 'Пацифист',
                'description': 'Пройти игру без убийств',
                'unlocked': False
            },
            'murderer': {
                'name': 'Убийца',
                'description': 'Убить всех встреченных персонажей',
                'unlocked': False
            },
            'explorer': {
                'name': 'Исследователь',
                'description': 'Исследовать все комнаты в доме Фокса',
                'unlocked': False
            },
            'speed_runner': {
                'name': 'Спидраннер',
                'description': 'Пройти игру с минимумом исследований',
                'unlocked': False
            },
            'cat_friend': {
                'name': 'Друг котов',
                'description': 'Подружиться с котом',
                'unlocked': False
            },
            'survivor': {
                'name': 'Выживший',
                'description': 'Выжить с 1 HP',
                'unlocked': False
            }
        }
    
    def unlock(self, achievement):
        if achievement in self.achievements and not self.achievements[achievement]['unlocked']:
            self.achievements[achievement]['unlocked'] = True
            print(colored(f"\nДостижение разблокировано: {self.achievements[achievement]['name']}!", COLORS['system']))
            print(colored(f"Описание: {self.achievements[achievement]['description']}", COLORS['system']))
    
    def show_achievements(self):
        print(colored("\n=== ДОСТИЖЕНИЯ ===", COLORS['system']))
        unlocked_count = 0
        total_count = len(self.achievements)
        
        for achievement_id, achievement in self.achievements.items():
            status = "✓" if achievement['unlocked'] else "✗"
            color = 'green' if achievement['unlocked'] else 'red'
            if achievement['unlocked']:
                unlocked_count += 1
            print(colored(f"{status} {achievement['name']}: {achievement['description']}", color))
        
        print(colored(f"\nПрогресс: {unlocked_count}/{total_count} ({(unlocked_count/total_count)*100:.1f}%)", COLORS['system']))

class Player:
    def __init__(self, name, health=100, inventory=None, lvl=0):
        self.name = name
        self.health = health
        self.inventory = inventory or ["First", "poition"]
        self.lvl = lvl
        self.achievements = Achievements()
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return print(colored(f'На вас было совершено покушение, вы потеряли {damage} хп, у вас осталось {self.health} хп', COLORS['system']))

    def heal_to_full(self):
        self.health = 100
        print(colored("Ваше ХП наполнено до предела!", COLORS['system']))

    def new_room(self, room_name, has_loot=False, loot=None):
        print(colored(f"Вы попали в комнату: {room_name}", COLORS['player']))
        time.sleep(1)
        if not has_loot:
            print(colored("В данной комнате нету лута :(", COLORS['player']))
        else:
            print(f"В комнате есть лут: {loot}")

    def get_up_lvl(self, prev_lvl, new_lvl):
        if new_lvl < prev_lvl:
            print(colored("Ошибка: новый уровень не может быть ниже предыдущего!", COLORS['system']))
            return
        
        self.lvl = new_lvl
        print(colored("У вас повышение УР", COLORS['system']))
        for i in range(new_lvl):
            prev_lvl += i
            lvl_color = colored(str(prev_lvl), "black", "on_light_cyan")
            if prev_lvl >= new_lvl:
                colored_lvl = colored(str(new_lvl), "black", "on_light_cyan")
                print(colored(f"ваш УР: {colored_lvl}", COLORS['system'], "on_blue"))
                break
            print(colored(f"ваш УР: {lvl_color}", COLORS['system'], "on_blue"))
            time.sleep(0.1)

def print_colored_dialog(speaker, text, color):
    print(colored(f"{speaker}: {text}", color))
    time.sleep(DIALOG_DELAY)

def get_player_choice(prompt, options=None):
    while True:
        try:
            if options:
                for i, option in enumerate(options, 1):
                    print(f"{i}. {option}")
            choice = int(input(prompt))
            if options and (choice < 1 or choice > len(options)):
                print(colored("Пожалуйста, выберите существующий вариант!", COLORS['system']))
                continue
            return choice
        except ValueError:
            print(colored("Пожалуйста, введите число!", COLORS['system']))

def wait_ending():
    messages = [
        "Вы решили сидеть на одном месте в надежде на спасение",
        "Прошёл час",
        "Прошло 2 часа",
        "Прошло 4 часа",
        "Прошло 10 часов, вам это надоедает",
        "Прошли первые сутки, вы познакомились с пауками",
        "Прошли вторые сутки, вы поссорились с пауками",
        "Прошло 3 дня и вы умерли от обезвоживания",
        "КОНЕЦ, А НАДО БЫЛО ИДТИ ЗА НЕЗНАКОМЦЕМ >:D"
    ]
    
    for message in messages:
        print(colored(message, COLORS['system']))
        time.sleep(DIALOG_DELAY)
    exit()

def follow_stranger(player):
    print_colored_dialog("Система", "Вы побежали за неизвестным, но вам по пути попадается цветок", COLORS['system'])
    print_colored_dialog(player.name, "Хм, красивый цветок", COLORS['player'])
    
    choice = get_player_choice("Хотите потрогать цветок? (1 - Да; 2 - нет): ")
    if choice == 1:
        flower_encounter(player)
    else:
        print_colored_dialog(player.name, "Я не буду этого делать!", COLORS['player'])
        continue_journey(player)

def flower_encounter(player):
    print_colored_dialog("Триш", "РУКИ УБРАЛ ОТ МЕНЯ Я ВООБЩЕ-ТО ЖИВАЯ!", COLORS['friend'])
    print_colored_dialog(player.name, "ААААААААА, ЧТО ТЫ ТАКОЕ???", COLORS['player'])
    print_colored_dialog("Триш", "Вообще-то я живая, меня зовут Триш", COLORS['friend'])
    print_colored_dialog("Триш", "Я тут для того, чтобы рассказать про то, как устроен этот мир", COLORS['friend'])
    
    choice = get_player_choice("Дотронуться до лепестков Триш? (1 - Да; 2 - нет): ")
    if choice == 1:
        combat_with_trish(player)
    else:
        print_colored_dialog(player.name, "Я не буду этого делать!", COLORS['player'])
        continue_journey(player)

def show_tutorial():
    print(colored("В игре есть очень много текста, и его цвет имеет значение"))
    print(colored("Жёлтый - Ваши слова", COLORS['player']))
    print(colored("Красный - Враги", COLORS['enemy']))
    print(colored("Зелёный - Друзья", COLORS['friend']))
    print(colored("Голубой - Система ", COLORS['system']))

def show_credits():
    print(colored("Создатель игры: Стёпа | Fiikus. Игра Сделана с любовью <3", 
                 COLORS['system'], "on_blue"))

def start_game():
    name = input("Введите ваше имя: ").strip()
    while not name:
        print(colored("Имя не может быть пустым!", COLORS['system']))
        name = input("Введите ваше имя: ").strip()
    player = Player(name)
    game_intro(player)
    return player

def game_intro(player):
    print_colored_dialog("Неизвестный", "Неужели это наконец-то случилось?", COLORS['unknown'])
    print_colored_dialog(player.name, "Что случилось? Кто ты? Где я?", COLORS['player'])
    print_colored_dialog("Неизвестный", "Это не важно. Тебе надо выбраться отсюда, а мне надо уйти по делам, так-что удачи тебе", COLORS['unknown'])
    
    choice = get_player_choice("Пойти за неизвестным? (1 - Идти; 2 - не идти): ")
    if choice == 1:
        follow_stranger(player)
    else:
        wait_ending()

def main():
    player = None
    while True:
        options = ["Начать игру", "Загрузить игру", "Достижения", "Создатель", "Туториал", "Выход"]
        choice = get_player_choice("\nВыберите действие: ", options)
        
        if choice == 1:
            player = start_game()
        elif choice == 2:
            loaded_player = load_game()
            if loaded_player:
                player = loaded_player
        elif choice == 3:
            # Создадим временного игрока для просмотра достижений, если игра еще не начата
            if not player:
                temp_player = Player("Temp")
                temp_player.achievements.show_achievements()
            else:
                player.achievements.show_achievements()
        elif choice == 4:
            show_credits()
        elif choice == 5:
            show_tutorial()
        elif choice == 6:
            if player:
                save_menu(player, 'start')  # Предложим сохранить игру перед выходом
            print(colored("Спасибо за игру!", COLORS['system']))
            exit()
        else:
            print(colored("Неверный выбор!", COLORS['system']))

def check_player_health(player, message="Вы погибли..."):
    if player.health <= 0:
        game_over(message)
        return True
    return False

def combat_with_trish(player):
    player.take_damage(12)
    check_player_health(player, "Триш оказалась сильнее...")
    
    print_colored_dialog("Триш", "ХАХАХАХ, ТЫ ДУМАЛ,ЧТО ТУТ ВСЁ ЛЕГКО? ТУТ ЛИБО УБИВАЙ ЛИБО БУДЕШЬ УБИТЫМ", COLORS['enemy'])
    
    choice = get_player_choice("Дать отпор Триш? (1 - Да; 2 - нет): ")
    if choice == 1:
        print(colored("Вы едва ударили кулаком Триш, как тут-же она распалась на пылинки", COLORS['system']))
        player.get_up_lvl(1, 2)
        print_colored_dialog(player.name, "Я только-что убил цветка? Это странно, но надо идти дальше", COLORS['player'])
        continue_journey(player)
    else:
        print(colored("Триш поняла, что вы беззащитный и решила вас добить", COLORS['system']))
        time.sleep(DIALOG_DELAY)
        game_over("ИГРА ОКОНЧЕНА")

def continue_journey(player):
    print(colored("Вы идёте дальше", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("Спустя 2 часа долгой ходьбы, вы понимаете, что вы не можете ходить, а за вас ходит система", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    cat_encounter(player)

def cat_encounter(player):
    print(colored("Магическим образом вы появляетесь в коридоре рядом с котёнком", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("У котёнка слишком много шерсти, так-что она у него спадает, а потом отрастает, бесконечный двигатель, не так ли?", COLORS['system']))
    
    choice = get_player_choice("Побить котёнка? (1 - Да; 2 - нет): ")
    cat_killed = False
    
    if choice == 1:
        cat_killed = True
        print(colored("Какой-же вы живодёр! Но с угрызением совести вы ударили котёнка, а он ударил вас в ответ", COLORS['system']))
        player.take_damage(6)
        if check_player_health(player, "Котёнок оказался сильнее, чем вы думали..."):
            return
        print(colored("C ОГРОМНЫМ угрызением совести вы убиваете этого пушистика", COLORS['system']))
        player.get_up_lvl(2, 3)
        print_colored_dialog(player.name, "Воу... Мне это. Нравится? Убивать это ТАК круто!", COLORS['player'])
        player.achievements.unlock('murderer')
    else:
        print(colored("Вместо того, чтобы ударить котёнка, вы его гладите, вы ему нравитесь, вы чувствуете, что ваше ХП повышено до полна!", COLORS['system']))
        player.heal_to_full()
        print_colored_dialog(player.name, "Ладно, мне пора идти котик, удачи тебе!", COLORS['player'])
        print(colored("Уходя от кота вы задумались, а коты умеют говорить на человечьем языке?", COLORS['system']))
        player.achievements.unlock('cat_friend')
    
    fox_house(player, cat_killed)

def fox_house(player, cat_killed):
    print(colored("Идя ещё 2 часа вы находите одинокий домик, вы решаете в него зайти", COLORS['system']))
    print_colored_dialog(player.name, "Тук-тук, есть кто дома?", COLORS['player'])
    print(colored("К вам подходит большой пёсик, он не похож на фурри", COLORS['system']))
    
    fox_dialog(player)
    explore_house(player)
    fox_battle(player, cat_killed)

def game_over(message):
    print(colored(message, COLORS['system']))
    exit()

def good_ending(player):
    messages = [
        "Вы идёте до конца коридора и видите дверь в белую пустоту",
        "Войдя в неё вы просыпаетесь у себя на кровати в обычном мире...",
        f"{player.name}: Это был всего лишь сон?",
        "????: Наверное :) ",
        "Игра окончена!",
        "Вы получили: Хорошую концовку!",
        "Cпасибо за игру :D"
    ]
    
    for msg in messages:
        if "????" in msg:
            print(colored(msg, COLORS['enemy']))
        elif player.name in msg:
            print_colored_dialog(player.name, msg.split(": ")[1], COLORS['player'])
        else:
            print(colored(msg, COLORS['system']))
        time.sleep(DIALOG_DELAY)
    exit()

def bad_ending(player):
    messages = [
        f"Арач: Я - это ты",
        f"{player.name}: Всмысле?",
        "Арач: Ты пробудил меня из мёртвых",
        f"{player.name}: Как?",
        "Арач: Твоё желание убивать, это и пробудило меня из мёртвых",
        f"{player.name}: Что ты хочешь?",
        "Арач: Давай сотрём этот мир вместе?",
        f"{player.name}: Давай!",
        "Арач достаёт нож",
        "Вы атаковали первым",
        f"{player.name}: Прощай... {player.name}",
        "Игра окончена!",
        "Вы получили: Плохую Концовку",
        "Cпасибо за игру :D"
    ]
    
    for msg in messages:
        if "Арач:" in msg:
            print_colored_dialog("Арач", msg.split(": ")[1], COLORS['enemy'])
        elif player.name in msg:
            print_colored_dialog(player.name, msg.split(": ")[1], COLORS['player'])
        else:
            print(colored(msg, COLORS['system']))
        time.sleep(DIALOG_DELAY)
    exit()

def fox_dialog(player):
    dialogs = [
        ("Фокс", "Привет! Меня зовут Фокс, как ты тут оказался?", COLORS['friend']),
        (player.name, "Привет, а я {}, я не помню, как я тут оказался...".format(player.name), COLORS['player']),
        ("Фокс", "Не вешай нос! Если ты ничего не помнишь, то можешь начать всё с чистого листа! Если хочешь, можешь пока-что остаться у меня", COLORS['friend']),
        (player.name, "Спасибо большое, можно же пойти осмотреться в доме?", COLORS['player']),
        ("Фокс", "Конечно! Я не возражаю, а я пока-что пойду за дровами, ведь зима суровое время!", COLORS['friend'])
    ]
    
    for speaker, text, color in dialogs:
        print_colored_dialog(speaker, text, color)

def explore_house(player):
    visited_rooms = set()
    total_rooms = 4
    print(colored("Вы решили осмотреться", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    
    while True:
        options = ["На кухню", "В гостиную", "В библиотеку", "На второй этаж", "Вернуться в прихожую"]
        
        # Показываем прогресс исследования
        print(colored(f"Исследовано комнат: {len(visited_rooms)}/{total_rooms}", COLORS['system']))
        
        for i, option in enumerate(options[:-1], 1):
            status = " (Осмотрено)" if i in visited_rooms else ""
            print(f"{i}. {option}{status}")
        print(f"{len(options)}. {options[-1]}")
        
        choice = get_player_choice("Куда пойдём? ")
        
        if choice == 5:
            if len(visited_rooms) < total_rooms:
                print(colored(f"Вы осмотрели не все комнаты ({len(visited_rooms)}/{total_rooms})", COLORS['system']))
                if get_player_choice("1 - Продолжить осмотр; 2 - Всё равно уйти: ") == 2:
                    break
                continue
            break
            
        if choice in [1, 2, 3, 4]:
            if choice in visited_rooms:
                print(colored("Вы уже были в этой комнате. Осмотреть снова?", COLORS['system']))
                if get_player_choice("1 - Да; 2 - Нет: ") != 1:
                    continue
            
            visited_rooms.add(choice)
            if choice == 1:
                explore_kitchen(player)
            elif choice == 2:
                explore_living_room(player)
            elif choice == 3:
                explore_library(player)
            elif choice == 4:
                explore_second_floor(player)

        if len(visited_rooms) == total_rooms:
            player.achievements.unlock('explorer')
        elif len(visited_rooms) <= 1:
            player.achievements.unlock('speed_runner')

def explore_kitchen(player):
    print(colored("Вы идёте на кухню", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("На кухне вы находите много различных предметов", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("Но на ваш взгляд упал холодильник", COLORS['system']))
    
    if get_player_choice("Заглянуть в него? (1 - Да; 2- нет): ") == 1:
        print(colored("В холодильнике лежит одна собачья еда", COLORS['system']))
        time.sleep(DIALOG_DELAY)
        print(colored("Компания производящая данную еду называется <Еда для собак Corporation>", COLORS['system']))
        time.sleep(DIALOG_DELAY)
        print(colored("На банке написано: <ЕДА ТОЛЬКО ДЛЯ СОБАК! Гав>", COLORS['system']))
        time.sleep(DIALOG_DELAY)
    
    print(colored("Вы решаете вернуться в двери и дождаться Фокса", COLORS['system']))

def explore_living_room(player):
    messages = [
        "Вы идёте в гостиную",
        "В гостиной вы находите большой диван и телевизор, на нём стоит стол",
        "Да, на телевизоре стоит стол, а у вас не так?",
        "Вы нашли диван на котором вы решили прилечь",
        "Спустя время вы вернулись к двери, чтобы дождаться Фокса"
    ]
    
    for msg in messages:
        print(colored(msg, COLORS['system']))
        time.sleep(DIALOG_DELAY)

def explore_library(player):
    print(colored("Вы идёте в библиотеку (в таком маленьком доме есть библиотека? Что) ", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("В библиотеке вы нашли книгу: <Как устроен мир Подземелья для чайников. Том 1>", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("Вы видите, что вся полка обставлена этими книгами (их всего 3)", COLORS['system']))
    
    if get_player_choice("Прочитать первый том? (1 - Да; 2 - нет): ") == 1:
        messages = [
            "В книге написано: <Если вы увидели человека, то немедленно сообщите королевской страже об этом>",
            "В недоумении вы читаете дальше",
            "<Люди очень опасны! Если вы понимаете, что их УР высокий, то вам стоит бежать КАК МОЖНО БЫСТРЕЕ.>",
            "Вы закрываете книгу, думая, что это выдумки"
        ]
        for msg in messages:
            print(colored(msg, COLORS['system']))
            time.sleep(DIALOG_DELAY)
    
    print(colored("Вы вернулись к двери, чтобы дождаться Фокса", COLORS['system']))

def explore_second_floor(player):
    print(colored("Вы идёте на второй этаж", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("Вы находите табличку: <Извините, но сегодня второй этаж не работает :p >", COLORS['system']))
    time.sleep(DIALOG_DELAY)
    print(colored("Вы вернулись к двери, чтобы дождаться Фокса", COLORS['system']))

def fox_battle(player, cat_killed):
    print_colored_dialog("Фокс", "Слушай, нам надо по быстрому пойти в одно место, так-что иди за мной", COLORS['friend'])
    print(colored("Вы следуете за фоксом", COLORS['system']))
    print_colored_dialog("Фокс", "Я не хочу делать из этого трагедию, но мне придётся это сделать", COLORS['friend'])
    print(colored("Между вами и Фоксом появилось напряжение", COLORS['system']))
    print(colored("Фокс атакует!", COLORS['system']))
    
    player.take_damage(27)
    print_colored_dialog(player.name, "АЙ! ФОКС, ЗА ЧТО?", COLORS['player'])
    print_colored_dialog("Фокс", "Прости, мне придётся убить тебя, либо ты меня, либо я тебя", COLORS['friend'])
    
    battle_sequence(player, cat_killed)

def battle_sequence(player, cat_killed):
    def check_battle_health(player):
        return check_player_health(player, "Фокс оказался сильнее...")
    
    if check_battle_health(player):
        return
    
    # Добавим возможность диалога перед боем
    print_colored_dialog(player.name, "Может мы можем поговорить?", COLORS['player'])
    
    if not cat_killed and player.lvl <= 1:
        print_colored_dialog("Фокс", "Хм... Возможно ты не такой как остальные...", COLORS['friend'])
        if get_player_choice("1 - Попытаться убедить Фокса; 2 - Атаковать: ") == 1:
            peaceful_resolution(player)
            return
    
    choice = get_player_choice("Что делать?", ["Атаковать", "Попытаться договориться", "Попытаться убежать"])
    
    if choice == 3:  # Попытка убежать
        escape_chance = player.lvl >= 3 or (not cat_killed and player.health > 50)
        if escape_chance:
            print(colored("Вам удаётся убежать!", COLORS['system']))
            good_ending(player)
            return
        else:
            print(colored("Фокс оказался быстрее вас!", COLORS['system']))
            player.take_damage(15)
            if check_battle_health(player):
                return

    if choice == 1:
        print_colored_dialog("Фокс", "Ну что-ж, я надеялся на то, что ты добровольно помрёшь, но ты сам этого захотел", COLORS['friend'])
    else:
        print_colored_dialog(player.name, "ФОКС! ОДУМАЙСЯ", COLORS['player'])
        print(colored("Фокс молчит", COLORS['system']))
    
    player.take_damage(24)
    check_player_health(player)
    
    choice = get_player_choice("Подумайте об своей безопасности! Стоит ли атаковать Фокса в ответ? (1 - Да; 2 - нет): ")
    if choice not in [1, 2]:
        print(colored("Пока вы колеблетесь, Фокс атакует снова!", COLORS['system']))
        player.take_damage(10)
        check_player_health(player)
    
    if choice == 1:
        print(colored("Вы чувствуете, что осталось атаковать его ещё 1 раз", COLORS['system']))
    else:
        handle_peaceful_approach(player, cat_killed)
    
    check_player_health(player)
    final_choice(player)

def handle_peaceful_approach(player, cat_killed):
    print_colored_dialog(player.name, "ПОДУМАЙ ОБ ЭТОМ Я НИЧЕГО НЕ СДЕЛАЛ!", COLORS['player'])
    if cat_killed:
        print_colored_dialog("Фокс", "По дороге домой, я увидел своего кота <Шурика> УБИТОГО!", COLORS['friend'])
    else:
        print_colored_dialog("Фокс", "Я не хочу повторить ошибки прошлого...", COLORS['friend'])
    player.take_damage(24)

def final_choice(player):
    if player.health <= 0:
        game_over("Вы не смогли дожить до финала...")
        return
    print(colored("У фокса изменилось лицо, его защита очень ослабла, стоит его убить?", COLORS['system']))
    if get_player_choice("1 - Да; 2 - нет: ") == 1:
        handle_violent_ending(player)
    else:
        handle_peaceful_ending(player)

def handle_violent_ending(player):
    print(colored("Вы убили Фокса!", COLORS['system']))
    player.get_up_lvl(3, 10)
    player.heal_to_full()
    bad_ending(player)

def handle_peaceful_ending(player):
    print_colored_dialog(player.name, "ФОКС ПОЖАЛУЙСТА, НЕ ДЕЛАЙ ЭТОГО", COLORS['player'])
    player.take_damage(24)
    
    if check_player_health(player, "Вы погибли, пытаясь достучаться до Фокса..."):
        return
    
    # Улучшим логику мирного решения
    peaceful_chance = (
        player.lvl <= 1 or  # Игрок был милосерден
        (not cat_killed and player.health <= 5) or  # Игрок не убил кота и на грани смерти
        player.health == 1  # Игрок в критическом состоянии
    )
    
    if peaceful_chance:
        print(colored("Что-то внутри вас даёт силы держаться...", COLORS['system']))
        player.health = 1
        
        # Добавим выбор финальной фразы
        options = [
            "Пожалуйста, давай просто поговорим...",
            "Я не хочу никому причинять боль!",
            "Мы можем решить всё мирно..."
        ]
        choice = get_player_choice("Выберите, что сказать: ", options)
        print_colored_dialog(player.name, options[choice-1], COLORS['player'])
        
        peaceful_resolution(player)
    else:
        game_over("Ваша жестокость не позволила вам найти силы для спасения...")

    if not cat_killed and player.health <= 1:
        player.achievements.unlock('survivor')
        player.achievements.unlock('pacifist')

def peaceful_resolution(player):
    messages = [
        "Фокс отдаёт вам банку компании <Еда для собак Corporation>",
        "На банке написано <Еда не только для собак. :3 >",
        "Вы съели всю банку, ваше ХП наполнено до предела"
    ]
    
    for msg in messages:
        print(colored(msg, COLORS['system']))
        time.sleep(DIALOG_DELAY)
    
    player.heal_to_full()
    print_colored_dialog("Фокс", "Иди в сторону замка, его трудно не заметить, ты спокойно сможешь войти и попасть на <Суд>", COLORS['friend'])
    print_colored_dialog(player.name, "Суд?", COLORS['player'])
    print_colored_dialog(player.name, "Над кем?", COLORS['player'])
    print_colored_dialog("Фокс", "Над тобой", COLORS['friend'])
    
    good_ending(player)

# Добавим функции для сохранения/загрузки
def save_game(player, checkpoint):
    save_data = {
        'name': player.name,
        'health': player.health,
        'inventory': player.inventory,
        'lvl': player.lvl,
        'checkpoint': checkpoint,
        'achievements': {k: v['unlocked'] for k, v in player.achievements.achievements.items()}
    }
    
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
    
    print(colored(f"\nИгра сохранена! Контрольная точка: {SAVE_POINTS[checkpoint]}", COLORS['system']))

def load_game():
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        
        player = Player(save_data['name'], save_data['health'], save_data['inventory'], save_data['lvl'])
        
        # Загружаем достижения
        for achievement, unlocked in save_data['achievements'].items():
            if unlocked:
                player.achievements.achievements[achievement]['unlocked'] = True
        
        print(colored(f"\nИгра загружена! Контрольная точка: {SAVE_POINTS[save_data['checkpoint']]}", COLORS['system']))
        
        # Возвращаем к нужной точке сохранения
        if save_data['checkpoint'] == 'start':
            game_intro(player)
        elif save_data['checkpoint'] == 'flower':
            flower_encounter(player)
        elif save_data['checkpoint'] == 'cat':
            cat_encounter(player)
        elif save_data['checkpoint'] == 'fox_house':
            fox_house(player, False)  # Предполагаем, что кот жив
        elif save_data['checkpoint'] == 'fox_battle':
            fox_battle(player, False)
        
        return player
    except FileNotFoundError:
        print(colored("Сохранение не найдено!", COLORS['system']))
        return None

# Добавим функцию для меню сохранения
def save_menu(player, checkpoint):
    print(colored("\nМеню сохранения:", COLORS['system']))
    options = ["Сохранить и продолжить", "Сохранить и выйти", "Продолжить без сохранения"]
    choice = get_player_choice("Выберите действие: ", options)
    
    if choice in [1, 2]:
        save_game(player, checkpoint)
        if choice == 2:
            print(colored("Спасибо за игру!", COLORS['system']))
            exit()
    return choice == 3

if __name__ == "__main__":
    main()
