"""Тема 10. Лінійне програмування (PuLP): максимізація виробництва напоїв.

Потрібна PuLP 2.x (як у конспекті): pip install "pulp<3".
У PuLP 4 змінився API LpVariable, і цей код там не запуститься.
"""

import pulp

model = pulp.LpProblem("Maximize_Drinks", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: загальна кількість продуктів
model += lemonade + fruit_juice, "Total_Products"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

model.solve(pulp.PULP_CBC_CMD(msg=False))

print("Статус:", pulp.LpStatus[model.status])
print("Лимонад:", int(lemonade.value()))
print("Фруктовий сік:", int(fruit_juice.value()))
print("Всього продуктів:", int(pulp.value(model.objective)))

print("\nВикористання ресурсів:")
print(f"  Вода: {2 * lemonade.value() + fruit_juice.value():.0f} / 100")
print(f"  Цукор: {lemonade.value():.0f} / 50")
print(f"  Лимонний сік: {lemonade.value():.0f} / 30")
print(f"  Фруктове пюре: {2 * fruit_juice.value():.0f} / 40")
