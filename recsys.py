import pandas as pd
import random

data = pd.read_csv("data.csv")

print(data.head())

users = data['user_id'].unique()
items = data['item_id'].unique()

# строки — пользователи, столбцы — товары
q_table = pd.DataFrame(0, index=users, columns=items)


alpha = 0.1
gamma = 0.9
epsilon = 0.1


def choose_action(user_id):
    if random.uniform(0, 1) < epsilon:
        return random.choice(items)
    else:
        # рекомендация товара с наивысшей Q-оценкой
        return q_table.loc[user_id].idxmax()


# Обновление Q-таблицы
def update_q_table(user_id, item_id, reward):
    # Получаем текущее предсказание
    predict = q_table.loc[user_id, item_id]

    # Обновляем Q-значение
    q_table.loc[user_id, item_id] += alpha * (reward - predict)


# Обучение системы на данных
for interaction in data.itertuples():
    user_id = interaction.user_id
    item_id = interaction.item_id
    rating = interaction.rating

    # Выбираем товар для рекомендации
    recommended_item = choose_action(user_id)

    # Обновляем Q-таблицу на основе рейтинга
    update_q_table(user_id, recommended_item, rating)

print("Обученная Q-таблица:")
print(q_table)


def recommend(user_id):
    # Выбираем товар с максимальной Q-оценкой
    recommended_item = q_table.loc[user_id].idxmax()
    return recommended_item


user_id = 10
recommended_item = recommend(user_id)
print(f"Рекомендованный товар для пользователя {user_id}: {recommended_item}")
