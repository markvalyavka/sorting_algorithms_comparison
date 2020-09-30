"""
Comparison and analysis of different sorting algorithms
"""


import time
from sorting_algorithms import selection_sort, insertion_sort, merge_sort, shell_sort
from utils import generate_array, visualize_results


def run_experimenets():
    """
    Main function to run experiments
    """
    results = {}
    experiment_types = [
        "general_array",
        "sorted_array",
        "reverse_sorted_array",
        "repeated_val_array",
    ]

    for experiment in experiment_types:

        num_of_experiments = 1

        if experiment == 'general_array':
            num_of_experiments = 5
        elif experiment == 'repeated_val_array':
            num_of_experiments = 3

        for size_in_power_of_two in range(7, 16):

            for sorting_algorithm, algo_name in [(selection_sort, 'selection_sort'), (insertion_sort, 'insertion_sort'),
                                                 (merge_sort, 'merge_sort'), (shell_sort, 'shell_sort')]:

                total_runtime = 0

                for _ in range(num_of_experiments):

                    test_array = generate_array(experiment, size_in_power_of_two)
                    start_time = time.time()
                    comparisons = sorting_algorithm(test_array)
                    end_time = time.time()

                    total_runtime += end_time - start_time

                avg_runtime = total_runtime / num_of_experiments

                if not experiment in results:
                    results[experiment] = {}
                if not algo_name in results[experiment]:
                    results[experiment][algo_name] = {}
                results[experiment][algo_name][size_in_power_of_two] = (avg_runtime, comparisons)

    return results


if __name__ == "__main__":

    results = run_experimenets()
    visualize_results(results)


