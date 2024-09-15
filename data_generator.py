import csv
import random


def generate_recsys_data(users=100, items=50, interactions=500, filename="data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "item_id", "rating"])

        for _ in range(interactions):
            user_id = random.randint(1, users)  # ID пользователя
            item_id = random.randint(1, items)  # ID товара
            rating = random.randint(1, 5)  # Рейтинг (от 1 до 5)

            writer.writerow([user_id, item_id, rating])


generate_recsys_data(users=100, items=50, interactions=500, filename="data.csv")
