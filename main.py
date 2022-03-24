import random
import numpy as np
import time
import random


def bogo_sort(bogo_data_set):
    i = 0
    start = time.time()
    while bogo_data_set != sorted(bogo_data_set):
        random.shuffle(bogo_data_set)
    end = time.time()
    difference = end - start
    print(f"Bogo sorted data set:\n{bogo_data_set}")
    print(f"Time taken: {difference} seconds")


def insertion_sort(insertion_data_set):
    start = time.time()


def numpy_sort(numpy_data_set):  # Default numpy sort no arguments
    start = time.time()
    numpy_sorted_data_set = np.sort(numpy_data_set)
    end = time.time()
    difference = end - start
    print(f"Numpy sorted data set:\n{numpy_sorted_data_set}")
    print(f"Time taken: {difference} seconds\n")


def user_choices():
    print("\n" * 100)  # Clear screen

    data_set = []  # Initialize data set

    data_set_size = input("Data set size? (Recomended 10-100)\n")  # Get data set size
    while data_set_size.isdigit() == False:  # Check if input is a number
        print("Error: Please enter an integer.")
        data_set_size = input("Data set size? (Recomended 10-100)\n")

    max_number = input("Max number? (Recomended 1000)\n")  # Get max number
    while max_number.isdigit() == False:  # Check if input is a number
        print("Error: Please enter an integer.")
        data_set_size = input("Max number? (Recomended 1000)\n")

    for i in range(int(data_set_size)):  # Generate data set
        data_set.append(random.randint(0, int(max_number)))

    print(f"\nUnsorted data set:\n{data_set}")  # Print unsorted data set

    time_choice = input("\nPlease select a timing method:\n1. Timing with time.time()\n2. Timing with other\n")  # Get timing method
    while time_choice != 1 or 2:  # Check if input is valid
        print("Error: Please enter 1 or 2.")
        time_choice = input("\nPlease select a timing method:\n1. Timing with time.time()\n2. Timing with other\n")

    sort_choice = input("\nPlease select a sorting method:\n1. Bogo sort\n2. Insertion sort\n3. Numpy sort\n")  # Get sorting method
    while sort_choice != 1 or 2 or 3:  # Check if input is valid
        print("Error: Please enter 1, 2 or 3.")
        sort_choice = input("\nPlease select a sorting method:\n1. Bogo sort\n2. Insertion sort\n3. Numpy sort\n")


user_choices()
