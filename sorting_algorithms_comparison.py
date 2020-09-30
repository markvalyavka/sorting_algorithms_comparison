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
        print(experiment)

        num_of_experiments = 1

        if experiment == 'general_array':
            num_of_experiments = 5
        elif experiment == 'repeated_val_array':
            num_of_experiments = 3

        for size_in_power_of_two in range(7, 12):
            print(size_in_power_of_two)
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
    import pprint
    #res = {'general_array': {'selection_sort': {7: (0.001307058334350586, 8128), 8: (0.004175996780395508, 32640), 9: (0.01593489646911621, 130816), 10: (0.05778827667236328, 523776), 11: (0.21744127273559571, 2096128)}, 'insertion_sort': {7: (0.001368570327758789, 4396), 8: (0.002829742431640625, 16918), 9: (0.01839737892150879, 66231), 10: (0.04711828231811523, 268435), 11: (0.18866519927978515, 1037760)}, 'merge_sort': {7: (0.0006341934204101562, 730), 8: (0.0007372379302978515, 1715), 9: (0.002758359909057617, 3939), 10: (0.003852367401123047, 8799), 11: (0.008013677597045899, 19537)}, 'shell_sort': {7: (0.00024313926696777343, 1023), 8: (0.0006405830383300782, 2651), 9: (0.0025667667388916014, 4938), 10: (0.006068706512451172, 18213), 11: (0.014835405349731445, 61189)}}, 'sorted_array': {'selection_sort': {7: (0.0007889270782470703, 8128), 8: (0.0031540393829345703, 32640), 9: (0.012814998626708984, 130816), 10: (0.05362081527709961, 523776), 11: (0.21036481857299805, 2096128)}, 'insertion_sort': {7: (2.002716064453125e-05, 127), 8: (4.00543212890625e-05, 255), 9: (9.441375732421875e-05, 511), 10: (0.00019788742065429688, 1023), 11: (0.00040602684020996094, 2047)}, 'merge_sort': {7: (0.0002758502960205078, 448), 8: (0.000591278076171875, 1024), 9: (0.0012691020965576172, 2304), 10: (0.0027740001678466797, 5120), 11: (0.00605010986328125, 11264)}, 'shell_sort': {7: (9.489059448242188e-05, 0), 8: (0.0002181529998779297, 0), 9: (0.0005559921264648438, 0), 10: (0.0013129711151123047, 0), 11: (0.0029909610748291016, 0)}}, 'reverse_sorted_array': {'selection_sort': {7: (0.0008161067962646484, 8256), 8: (0.0031311511993408203, 32896), 9: (0.013335943222045898, 131328), 10: (0.0538942813873291, 524800), 11: (0.2222428321838379, 2098176)}, 'insertion_sort': {7: (0.001280069351196289, 8384), 8: (0.005726814270019531, 33152), 9: (0.02120208740234375, 131840), 10: (0.0924379825592041, 525824), 11: (0.3679389953613281, 2100224)}, 'merge_sort': {7: (0.00030493736267089844, 456), 8: (0.0006191730499267578, 1033), 9: (0.0013358592987060547, 2314), 10: (0.0029189586639404297, 5131), 11: (0.006440877914428711, 11276)}, 'shell_sort': {7: (0.0001506805419921875, 324), 8: (0.0003571510314941406, 772), 9: (0.0009107589721679688, 1796), 10: (0.0022292137145996094, 4100), 11: (0.004975795745849609, 9220)}}, 'repeated_val_array': {'selection_sort': {7: (0.000785668690999349, 8128), 8: (0.003027677536010742, 32640), 9: (0.013029098510742188, 130816), 10: (0.05391089121500651, 523776), 11: (0.21227033933003744, 2096128)}, 'insertion_sort': {7: (0.0004432996114095052, 2650), 8: (0.001795371373494466, 11279), 9: (0.007248878479003906, 42328), 10: (0.031226634979248047, 173801), 11: (0.12303654352823894, 700304)}, 'merge_sort': {7: (0.0003250439961751302, 684), 8: (0.0006995995839436849, 1559), 9: (0.0015329519907633464, 3474), 10: (0.0037693182627360025, 7749), 11: (0.007506926854451497, 17453)}, 'shell_sort': {7: (0.0001236597696940104, 135), 8: (0.00029460589090983075, 367), 9: (0.0007461706797281901, 958), 10: (0.0017662843068440754, 2043), 11: (0.004210313161214192, 4400)}}}
    res = run_experimenets()
    pprint.pprint(res)
    visualize_results(res)


    #pprint.pprint(run_experimenets())

