import random
import numpy as np
import time
import random

# initialize variables
data_set_size = 0
max_number = 0
time_choice = 0
sort_choice = 0

# error messages
input_int_error = "Please enter an integer"
out_of_range_error = "Please enter an listed option (eg. 1)"
fatal_error = "Fatal error: Please resart the program. If the error persists, please contact the developer"

print("\n" * 100)  # Clear screen

########################################################################################################################


def time_bogo_sort(bogo_data_set):
    i = 0
    start = time.time()
    while bogo_data_set != sorted(bogo_data_set):
        random.shuffle(bogo_data_set)
    end = time.time()
    difference = end - start
    print(f"Bogo sorted data set:\n{bogo_data_set}")
    print(f"Time taken: {difference} seconds")


def time_insertion_sort(insertion_data_set):
    start = time.time()
    print("Not implemented yet")


def time_numpy_sort(numpy_data_set):  # Default numpy sort no arguments
    start = time.time()
    numpy_sorted_data_set = np.sort(numpy_data_set)
    end = time.time()
    difference = end - start
    print(f"Numpy sorted data set:\n{numpy_sorted_data_set}")
    print(f"Time taken: {difference} seconds\n")


def set_size():
    global data_set_size
    data_set_size = input("\nData set size? (Recomended 10-100)\n")  # Get data set size
    if data_set_size.isdigit() == False:  # Check if input is a number
        set_size()


def set_max_number():
    global max_number
    max_number = input("\nMax number? (Recomended 1000)\n")  # Get max number
    if max_number.isdigit() == False:  # Check if input is a number
        set_max_number()


def set_time_choice():
    global time_choice
    time_choice = int(input("\nPlease select a timing method:\n1. Timing with time.time()\n2. Timing with other\n"))  # Get timing method
    if time_choice != 1 or 2:  # Check if input is valid
        set_time_choice()


def set_sort_choice():
    global sort_choice
    sort_choice = input("\nPlease select a sorting method:\n1. Bogo sort\n2. Insertion sort\n3. Numpy sort\n")  # Get sorting method
    if sort_choice != 1 or 2 or 3:  # Check if input is valid
        set_sort_choice()


def main():
    data_set = []  # Initialize data set
    set_size()  # Get data set size
    set_max_number()  # Get max number

    for i in range(int(data_set_size)):  # Generate data set
        data_set.append(random.randint(0, int(max_number)))

    print(f"\nUnsorted data set:\n{data_set}")  # Print unsorted data set

    set_time_choice()  # Get timing method
    set_sort_choice()  # Get sorting method

    if time_choice == 1:
        if sort_choice == 1:
            time_bogo_sort(data_set)
        elif sort_choice == 2:
            time_insertion_sort(data_set)
        elif sort_choice == 3:
            time_numpy_sort(data_set)
        else:
            print(fatal_error)
    elif time_choice == 2:
        if sort_choice == 1:
            print("Not implemented yet")
        if sort_choice == 2:
            print("Not implemented yet")
        if sort_choice == 3:
            print("Not implemented yet")


main()
