num_tickets = int(input('Введите количество билетов: ')) #  у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
s = 0 #  переменная суммы
for i in range(1, num_tickets + 1):
    age = int(input(f'Введите возраст посетителя для {i} -го билета: ')) # Далее для каждого билета запрашивается возраст посетителя
    if 18 <= age < 25:# От 18 до 25 лет — 990 руб.
        s = s + 990
    elif age > 25:# От 25 лет — полная стоимость 1390 руб.
        s = s + 1390
    elif age <= 0 or age > 200:
        print(f'Вы ввели {age} - это некорректный возраст')
if num_tickets > 3:
    s *= 0.9# При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
print(f'Сумма к оплате: {round(s, 2)} руб.')# 3. В результате программы выводится сумма к оплате.