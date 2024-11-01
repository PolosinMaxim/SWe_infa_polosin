import datetime as dt
import random as rn

def getBirthdays(numberOfBirthdays):
    return [dt.date(2001, 1, 1) + dt.timedelta(rn.randrange(365)) for i in range(numberOfBirthdays)]
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)): return None
    for a in birthdays:
        if birthdays.count(a) > 1: return a

print('''Парадокс дней рождения. Автор: Эл Свейгарт (al@inventwithpython.com)
Согласно Парадоксу дней рождения, шансы того, что в некой группе людей
у двух человек окажется одинаковый день рождения на удивление большие.
Для исследования этой идеи я проведу симулацию Монте Карло,
т.е. проведу случайную симуляцию заданное число раз.
(Вообще, это не совсем парадокс, а скорее занятное наблюдение.)
''')
MONTHS = ('Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек')
print('Сколько дней рождения сгенерировать? (от 2 до 100 включительно)')
while True:
    response = input('> ')
    if response.isdecimal(): #and (0 < int(response) <= 100):
        numBDays = max(min(int(response), 100), 2)
        break

print(chr(10) + 'Вот Ваши {} дней рождения'.format(numBDays))
birthdays = getBirthdays(numBDays)
print(', '.join(['{} {}'.format(MONTHS[i.month - 1], i.day) for i in birthdays]))

match = getMatch(birthdays)
print('В этой симуляции ', end = '')
if match != None: print('у нескольких людей день рождения - {} {}'.format(MONTHS[match.month - 1], match.day))
else: print('не было совпадающих дней рождения.')

print(chr(10) + 'Теперь нужно сгенерировать {} случайных дней рождения 100,000 раз.'.format(numBDays))
input('Press Enter to begin...')
print('Поехали.')
simMatch = 0
for i in range(100_000):
    if not i % 10_000: print(i, 'симуляций пройдено.')
    if getMatch(getBirthdays(numBDays)) != None: simMatch += 1
print('100,000 симуляций пройдено.')

print('''
Из 100,000 симуляций групп из {} человек
совпадающий день рождения наблюдался {} раз.
Значит, у группы из {} людей есть {}% шанс на то,
что у хотя бы 2 людей будут совпадать дни рождения.
Наверняка больше, чем могло показаться!
'''.format(numBDays, simMatch, numBDays, round(simMatch / 100_000 * 100, 2)))
input("Press Enter to exit...")