money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0  # Количество месяцев, которое можно протянуть без долгов

while True:
    budget = spend - salary
    if budget > money_capital:
        break

    month += 1
    money_capital -= budget
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)
