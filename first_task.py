import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('fruit juice', lowBound=0, cat='Integer')

# Функція цілі
model += lemonade + fruit_juice, "Total Production"

# Додавання обмежень
model += 2 * lemonade + 1 * fruit_juice <= 100  # Обмеження для води
model += 1 * lemonade <= 50  # Обмеження для цукру
model += 1 * lemonade <= 30  # Обмеження для лимонного соку
model += 2 * fruit_juice <= 40  # Обмеження для фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів lemonade:", lemonade.varValue)
print("Виробляти продуктів fruit juice:", fruit_juice.varValue)
