"""
Utility functions
"""


import random
from plotly.subplots import make_subplots


def generate_array(experiment_type, size_power_of_two):
    """
    Generate random array of certain size according to experiment type

    :param experiment_type: type of the experiment
    :param size_power_of_two: size (number of elements)
           of the array ( 2 ** {size_power_of_two})
    :return: randomly generated array
    """
    if experiment_type == "general_array":
        randomlist = random.sample(
            range(1, (2 ** size_power_of_two) + 1), 2 ** size_power_of_two
        )
    elif experiment_type == "sorted_array":
        randomlist = [num for num in range(2 ** size_power_of_two)]
    elif experiment_type == "reverse_sorted_array":
        randomlist = [num for num in range(2 ** size_power_of_two, -1, -1)]
    elif experiment_type == "repeated_val_array":
        randomlist = [random.randint(1, 3) for _ in range(2 ** size_power_of_two)]
    else:
        return []

    return randomlist


def visualize_results(result_data):
    """
    Function to visualize results
    """

    line_colors = {
        "selection_sort": "rgb(69, 144, 185)",
        "insertion_sort": "rgb(253, 174, 97)",
        "merge_sort": "rgb(153, 112, 171)",
        "shell_sort": "rgb(239, 106, 76)"
    }

    fig = make_subplots(rows=4, cols=2,
                        subplot_titles=("Random array (Runtime)", "Random array (Comparisons)",
                                        "Sorted array (Runtime)", "Sorted array (Comparisons)",
                                        "Reverse sorted array (Runtime)", "Reverse sorted array (Comparisons)",
                                        "Repeated values array (Runtime)", "Repeated values array (Comparisons)"),
                        horizontal_spacing=0.07)

    fig.update_layout(title_text=f"Sorting algorithms comparison", height=1500)

    current_row = 1
    show_legend_flag = False
    for experiment_type in result_data.keys():

        for sorting_algorithm in result_data[experiment_type]:

            x_values = list(result_data[experiment_type][sorting_algorithm].keys())
            y_values = list(result_data[experiment_type][sorting_algorithm].values())

            if current_row == 1:
                show_legend_flag = True

            fig.add_scatter(x=x_values,
                            y=[y_value[0] for y_value in y_values],
                            name=sorting_algorithm,
                            legendgroup=sorting_algorithm,
                            showlegend=show_legend_flag,
                            line=dict(color=line_colors[sorting_algorithm]),
                            row=current_row, col=1)

            show_legend_flag = False

            fig.add_scatter(x=x_values,
                            y=[y_value[1] for y_value in y_values],
                            name=sorting_algorithm,
                            legendgroup=sorting_algorithm,
                            showlegend=show_legend_flag,
                            line=dict(color=line_colors[sorting_algorithm]),
                            row=current_row, col=2)

            fig.update_xaxes(title_text=f"Array Size (power of 2)", row=current_row, col=1)
            fig.update_xaxes(title_text=f"Array Size (power of 2)", row=current_row, col=2)
            fig.update_yaxes(title_text="Runtime in seconds (s)", row=current_row, col=1)
            fig.update_yaxes(title_text="Number of comparisons", row=current_row, col=2)

        current_row += 1

    fig.show()