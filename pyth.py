<<<<<<< HEAD
import time
from termcolor import *
print(colored('Привет мир!', 'red', attrs=['underline']))
print('Привет, я люблю тебя!')
cprint('Вывод с помощью cprint', 'green', 'on_blue')
prev_lvl = 1
new_lvl = 99
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
=======
import time
from termcolor import *
print(colored('Привет мир!', 'red', attrs=['underline']))
print('Привет, я люблю тебя!')
cprint('Вывод с помощью cprint', 'green', 'on_blue')
prev_lvl = 1
new_lvl = 99
print(colored(f"У вас повышение уровня!", "light_blue"))
for i in range(new_lvl):
    prev_lvl+=i
    lvl = colored(f"{prev_lvl}", "red")
    if prev_lvl >= new_lvl:
        print(colored(f"ваш уровень: {new_lvl}", 'light_blue', "on_blue"))
        break
    else:
        print(colored(f"ваш уровень: {lvl}", 'light_blue', "on_blue"))
        time.sleep(0.01)
>>>>>>> 1b5387a1c59e9229ae778ec2ba98069996a990c0
