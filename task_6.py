"""Module providing a functions solving Knapsack problem."""
def greedy_algorithm(items, budget):
    """
    Selects items maximizing the calories to cost ratio within a given 
    budget using a greedy algorithm.
    """
    sorted_items = sorted(items.items(), \
                          key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    selected_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']

    return selected_items

def dynamic_programming(items, budget):
    """
    Computes the optimal set of items to maximize calories within a given 
    budget using dynamic programming.
    """
    n = len(items)
    item_list = list(items.items())

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost, calories = details['cost'], details['calories']
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item, _ = item_list[i - 1]
            selected_items.append(item)
            j -= items[item]['cost']

    selected_items.reverse()
    return selected_items

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    print("Greedy algorithm result:", greedy_result)

    dp_result = dynamic_programming(items, budget)
    print("Dynamic programming result:", dp_result)
