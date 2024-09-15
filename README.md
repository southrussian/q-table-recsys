# Recommendation System using Q-Learning

## Overview
This project implements a simple recommendation system using **Q-Learning**, a popular reinforcement learning algorithm. The recommendation system is designed to learn from historical user-item interactions and provide personalized recommendations based on the learned preferences.

The system is implemented using Python, leveraging the **Pandas** library to handle data manipulation and a Q-Learning approach for recommendation logic. The Q-Table is stored as a Pandas DataFrame, where rows represent users and columns represent items, and the values indicate the learned "quality" or preference for a particular item.

## Key Features
- **Q-Learning** algorithm to learn user preferences.
- Personalized recommendations for each user based on historical data.
- Dynamic updates to the recommendation model as new interactions occur.

## How Q-Learning Works
1. **Q-Table**: A table where each row corresponds to a user and each column corresponds to an item. The values represent the Q-values (or learned preferences) for user-item pairs.
2. **Action Selection**: For each user, the algorithm selects an item to recommend. The item can either be selected randomly (exploration) or based on the highest Q-value (exploitation).
3. **Reward Signal**: The Q-Table is updated based on the reward, which in this case is the user's rating of the recommended item.
4. **Update Rule**: The Q-Table is updated iteratively based on the learning rate and the difference between the expected reward and the actual rating received.

## Prerequisites
To run the project, you will need:
- Python 3.x
- Pandas library (`pip install pandas`)

## Input Data
The input data should be a **CSV file** (`data.csv`) containing historical user-item interactions. The file should have the following columns:
- **user_id**: The unique identifier for a user.
- **item_id**: The unique identifier for an item.
- **rating**: The user's rating of the item.

### Example of `data.csv`:

| user_id | item_id | rating |
|---------|---------|--------|
| 1       | 101     | 5      |
| 1       | 102     | 4      |
| 2       | 101     | 2      |
| 3       | 103     | 5      |
| ...     | ...     | ...    |

## Code Structure

### 1. Data Loading
```python
data = pd.read_csv("data.csv")
```
The historical user-item interactions are loaded from the `data.csv` file using **Pandas**.

### 2. Q-Table Initialization
```python
q_table = pd.DataFrame(0, index=users, columns=items)
```
A Q-Table is created where rows represent unique users, columns represent unique items, and all initial Q-values are set to zero.

### 3. Action Selection (Recommendation)
```python
def choose_action(user_id):
    if random.uniform(0, 1) < epsilon:
        return random.choice(items)
    else:
        return q_table.loc[user_id].idxmax()
```
The algorithm selects an item to recommend either through exploration (random choice) or exploitation (item with the highest Q-value for the user).

### 4. Q-Table Update
```python
def update_q_table(user_id, item_id, reward):
    predict = q_table.loc[user_id, item_id]
    q_table.loc[user_id, item_id] += alpha * (reward - predict)
```
The Q-value for the selected user-item pair is updated based on the difference between the predicted and actual reward (user rating).

### 5. Training Loop
```python
for interaction in data.itertuples():
    user_id = interaction.user_id
    item_id = interaction.item_id
    rating = interaction.rating
    recommended_item = choose_action(user_id)
    update_q_table(user_id, recommended_item, rating)
```
The algorithm iterates over the historical data, makes recommendations for each interaction, and updates the Q-Table based on the user's rating.

### 6. Recommendation Function
```python
def recommend(user_id):
    recommended_item = q_table.loc[user_id].idxmax()
    return recommended_item
```
This function returns the item with the highest Q-value for a given user, providing the final recommendation.

## Example Usage

1. **Train the Model**: After loading the data, the system automatically learns user preferences by iterating over the user-item interactions and updating the Q-Table.
2. **Get Recommendations**: Once the model is trained, you can query it for recommendations for a particular user:

```python
user_id = 10
recommended_item = recommend(user_id)
print(f"Recommended item for user {user_id}: {recommended_item}")
```

## Hyperparameters
- **alpha**: Learning rate, controls how much new information overrides old information during updates. Default is `0.1`.
- **gamma**: Discount factor, determines the importance of future rewards. Default is `0.9`.
- **epsilon**: Exploration rate, defines the probability of choosing a random action. Default is `0.1`.

## Conclusion
This recommendation system uses Q-Learning to iteratively improve the quality of recommendations based on user feedback. Over time, the system learns which items users are more likely to enjoy and recommends those with the highest expected reward.

## Future Improvements
- Integrate other features like time of interaction or context.
- Apply deep reinforcement learning for handling large-scale data.
- Explore more sophisticated exploration strategies like **epsilon decay**.

maybe:)
