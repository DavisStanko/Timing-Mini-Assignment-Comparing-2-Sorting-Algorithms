import random
import numpy as np
import time
import random

# initialize variables
data_set_size = 0
max_number = 0
trials = 0
time_choice = 0
sort_choice = 0
total_time = 0

# error messages
input_int_error = "Please enter an integer"
out_of_range_error = "Please enter an listed option (eg. 1)"
fatal_error = "Fatal error: Please resart the program. If the error persists, please contact the developer"

print("\n" * 100)  # Clear screen

############################################ time.time() Sorting Algorithms ############################################


def time_bogo_sort(bogo_data_set, sorted_data_set):  # Bogo sort timed with time.time()
    global total_time
    temp_data_set = bogo_data_set.copy()
    start = time.time()
    while temp_data_set != sorted_data_set:
        random.shuffle(temp_data_set)
    end = time.time()
    difference = round(end - start, 10)
    print(f"\nBogo sorted data set:\n{temp_data_set}")
    print(f"\nTime taken: {difference} seconds")
    total_time = total_time + difference


# Radix sort timed with time.time()
# Using counting sort to sort the elements in the basis of significant places
def countingSort(temp_data_set, place):
    size = len(temp_data_set)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = temp_data_set[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = temp_data_set[i] // place
        output[count[index % 10] - 1] = temp_data_set[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        temp_data_set[i] = output[i]


# Main function to implement radix sort
def time_radix_sort(radix_data_set):
    global total_time
    temp_data_set = radix_data_set.copy()
    start = time.time()
    # Get maximum element
    max_element = max(temp_data_set)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(temp_data_set, place)
        place *= 10
    end = time.time()
    difference = round(end - start, 10)
    print(f"Radix sorted data set:\n{temp_data_set}")
    print(f"\nTime taken: {difference} seconds")
    total_time = total_time + difference


def time_numpy_sort(numpy_data_set):  # Default numpy sort no arguments timed with time.time()
    global total_time
    temp_data_set = numpy_data_set.copy()
    start = time.time()
    numpy_sorted_data_set = np.sort(temp_data_set)
    end = time.time()
    difference = round(end - start, 10)
    print(f"\nNumpy sorted data set:\n{numpy_sorted_data_set}")
    print(f"\nTime taken: {difference} seconds\n")
    total_time = total_time + difference

######################################## time.perf_counter() Sorting Algorithms ########################################


def perf_bogo_sort(bogo_data_set, sorted_data_set):  # Bogo sort timed with time.perf_counter()
    global total_time
    temp_data_set = bogo_data_set.copy()
    start = time.perf_counter()
    while temp_data_set != sorted_data_set:
        random.shuffle(temp_data_set)
    end = time.perf_counter()
    difference = round(end - start, 10)
    print(f"\nBogo sorted data set:\n{temp_data_set}")
    print(f"\nTime taken: {difference} seconds")
    total_time = total_time + difference


# Radix sort timed with time.perf_counter()
def countingSort(temp_data_set, place):  # Using counting sort to sort the elements in the basis of significant places
    size = len(temp_data_set)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = temp_data_set[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = temp_data_set[i] // place
        output[count[index % 10] - 1] = temp_data_set[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        temp_data_set[i] = output[i]


# Main function to implement radix sort
def perf_radix_sort(radix_data_set):
    global total_time
    temp_data_set = radix_data_set.copy()
    start = time.perf_counter()
    max_element = max(temp_data_set)  # Get maximum element

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(temp_data_set, place)
        place *= 10
    end = time.perf_counter()
    difference = round(end - start, 10)
    print(f"Radix sorted data set:\n{temp_data_set}")
    print(f"\nTime taken: {difference} seconds")
    total_time = total_time + difference


def perf_numpy_sort(numpy_data_set):  # Default numpy sort no arguments timed with time.perf_counter()
    global total_time
    temp_data_set = numpy_data_set.copy()
    start = time.perf_counter()
    numpy_sorted_data_set = np.sort(temp_data_set)
    end = time.perf_counter()
    difference = round(end - start, 10)
    print(f"\nNumpy sorted data set:\n{numpy_sorted_data_set}")
    print(f"\nTime taken: {difference} seconds\n")
    total_time = total_time + difference

###################################################### User Input ######################################################


def set_size():
    global data_set_size
    data_set_size = input("\nData set size? (Recommended 10-100)\n")  # Get data set size
    if data_set_size.isdigit() == False:  # Check if input is a number
        print(input_int_error)
        set_size()


def set_max_number():
    global max_number
    max_number = input("\nMax number? (Recommended 1000)\n")  # Get max number
    if max_number.isdigit() == False:  # Check if input is a number
        print(input_int_error)
        set_max_number()


def set_trials():
    global trials
    trials = input("\nNumber of trials? (Recommended 1-10)\n")  # Get number of trials
    if trials.isdigit() == False:  # Check if input is a number
        print(input_int_error)
        set_trials()


def set_time_choice():
    global time_choice
    time_choice = int(input("\nPlease select a timing method:\n1. Timing with time.time()\n2. Timing with time.perf_counter (Recommended)\n"))  # Get timing method
    if time_choice == 1 or time_choice == 2:  # Check if input is valid
        return
    else:
        print(out_of_range_error)
        set_time_choice()


def set_sort_choice():
    global sort_choice
    sort_choice = int(input("\nPlease select a sorting method:\n1. Bogo sort\n2. Radix sort\n3. Numpy sort (Recommended)\n"))  # Get sorting method
    if sort_choice == 1 or sort_choice == 2 or sort_choice == 3:  # Check if input is valid
        return
    else:
        print(out_of_range_error)
        set_sort_choice()


def main():
    global total_time
    data_set = []  # Initialize data set
    set_size()  # Get data set size
    set_max_number()  # Get max number
    set_trials()  # Get number of trials

    for i in range(int(data_set_size)):  # Generate data set
        data_set.append(random.randint(0, int(max_number)))

    print(f"\nUnsorted data set:\n{data_set}")  # Print unsorted data set

    set_time_choice()  # Get timing method
    set_sort_choice()  # Get sorting method

    if time_choice == 1:
        if sort_choice == 1:
            sorted_data_set = sorted(data_set.copy())  # This is really stupid. It sorts the data set to see if it sorted correctly. Therefore it's quicker to just user sorted() by itself. I have left it out of the timing method to remove it's impact from the overall time.
            for i in range(int(trials)):
                time_bogo_sort(data_set, sorted_data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")
        elif sort_choice == 2:
            for i in range(int(trials)):
                time_radix_sort(data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")
        elif sort_choice == 3:
            for i in range(int(trials)):
                time_numpy_sort(data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")
        else:
            print(fatal_error)
    elif time_choice == 2:
        if sort_choice == 1:
            sorted_data_set = sorted(data_set.copy())  # This is really stupid. It sorts the data set to see if it sorted correctly. Therefore it's quicker to just user sorted() by itself. I have left it out of the timing method to remove it's impact from the overall time.
            for i in range(int(trials)):
                perf_bogo_sort(data_set, sorted_data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")
        if sort_choice == 2:
            for i in range(int(trials)):
                perf_radix_sort(data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")
        if sort_choice == 3:
            for i in range(int(trials)):
                perf_numpy_sort(data_set)
            print(f"\nAverage time taken: {float(total_time)/float(trials)} seconds")


main()
