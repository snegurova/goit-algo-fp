"""Module providing a functions to analyze Monte-Carlo method."""
import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_dice_simulation(num_rolls):
    """
    Simulates rolling two dice a specified number of times using the Monte Carlo method.
    """
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums_count[roll_sum] += 1

    probabilities = {sum_: count / num_rolls for sum_, count in sums_count.items()}
    return probabilities

def plot_probabilities(probabilities, title):
    """
    Plots the probabilities of the sums of two dice rolls.
    """
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title(title)
    plt.xticks(sums)
    plt.ylim(0, max(probs) * 1.2)
    plt.show()

def analytical_probabilities():
    """
    Returns the analytical probabilities for the sums of two dice rolls.
    """
    probabilities = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    return probabilities

def compare_probabilities(monte_carlo_probs, analytical_probs):
    """
    Compares Monte Carlo probabilities with analytical probabilities by plotting them together.
    """
    sums = list(analytical_probs.keys())
    monte_carlo = [monte_carlo_probs[sum_] for sum_ in sums]
    analytical = [analytical_probs[sum_] for sum_ in sums]

    bar_width = 0.35
    index = np.arange(len(sums))

    plt.bar(index, monte_carlo, bar_width, label='Monte Carlo', color='skyblue')
    plt.bar(index + bar_width, analytical, bar_width, label='Analytical', color='orange')
    
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Comparison of Monte Carlo and Analytical Probabilities')
    plt.xticks(index + bar_width / 2, sums)
    plt.legend()
    plt.show()

def calculate_errors(monte_carlo_probs, analytical_probs):
    """
    Calculates the errors between Monte Carlo probabilities and analytical probabilities.
    """
    errors = {sum_: abs(monte_carlo_probs[sum_] - analytical_probs[sum_]) / analytical_probs[sum_]\
               * 100 for sum_ in analytical_probs}
    return errors

def print_summary(monte_carlo_probs, analytical_probs, errors):
    """
    Prints a summary of Monte Carlo and analytical probabilities along with their errors.
    """
    print("Sum | Monte Carlo Probability | Analytical Probability | Error (%)")
    print("----|-------------------------|-------------------------|----------")
    for sum_ in sorted(monte_carlo_probs.keys()):
        mc_prob = monte_carlo_probs[sum_]
        an_prob = analytical_probs[sum_]
        error = errors[sum_]
        print(f"{sum_:>3} | {mc_prob:>23.4f} | {an_prob:>23.4f} | {error:>8.2f}")

    average_error = sum(errors.values()) / len(errors)
    print(f"\nAverage Error: {average_error:.2f}%")

def main():
    """Main function presenting analyze"""
    num_rolls = 1000000
    monte_carlo_probs = monte_carlo_dice_simulation(num_rolls)
    analytical_probs = analytical_probabilities()
    errors = calculate_errors(monte_carlo_probs, analytical_probs)

    print("Monte Carlo Probabilities:")
    for sum_, prob in monte_carlo_probs.items():
        print(f"Sum {sum_}: {prob:.4f}")

    print("\nAnalytical Probabilities:")
    for sum_, prob in analytical_probs.items():
        print(f"Sum {sum_}: {prob:.4f}")

    print("\nErrors:")
    for sum_, error in errors.items():
        print(f"Sum {sum_}: {error:.2f}%")

    print_summary(monte_carlo_probs, analytical_probs, errors)

    plot_probabilities(monte_carlo_probs, "Monte Carlo Probabilities for Dice Rolls")
    compare_probabilities(monte_carlo_probs, analytical_probs)

if __name__ == "__main__":
    main()
