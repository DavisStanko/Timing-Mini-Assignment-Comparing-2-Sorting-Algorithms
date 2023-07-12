# Timing-Mini-Assignment-Comparing-2-Sorting-Algorithms

This program was made to compare the efficiency of different sorting algorithms in python.

## Getting Started

### Prerequisites

Please be sure to install the following before running the program.

- Python 3.x

## Usage

Start the program by executing the main.py file.

## Timing Methods

### time.time()

Runs `time.time()` before and after the sorting algorithm has run and returns the difference. `time.time()` returns the time in seconds since the epoch (varies between systems but generally 1 January 1970 00:00:00) as a floating point number. Learn more [here](https://docs.python.org/3/library/time.html#time.time).

### time.perf_counter()

Runs `time.perf_counter()` before and after the sorting algorithm has run and returns the difference. `time.perf_counter()` has no relation to 'human' time and should only be used to mesure the difference in time between two points. Learn more [here](https://docs.python.org/3/library/time.html#time.perf_counter).

## Sorting Methods

### Bogo Sort --> Fun

Randomly sorts the given data until it is sorted correctly. This means with luck it could be successful the first attempt. On the other hand, there is a small chance that the list continuously gets sorted in an incorrect way and will take infinitely long. It is recommend that you use a small data set to maximize the chance of the sorting algorithm succeeding quickly. Max number has no effect as Bogo sort does not consider it.

This programs implementation of Bogo sort is purely for fun and should not be used for any real world applications. To check whether the random sort worked, I used pythons built-in function to sort the list and compare it with the Bogo results. However, this means that before the timer even starts for Bogo sort, the list has already been sorted! Therefore, even in the best case scenario using my implementation, Bogo sort is a waste of time.

### Radix Sort --> Speed

Theoretically the fastest sorting algorithm in this program. It works by grouping elements by their single digit place values and then ordering them. In this program, it uses counting sort as the intermediate sorting algorithm. Max number and data set size both have an effect on this algorithm but it should not struggle with any reasonable data set. However, due to the nature of Radix sort, it can be very memory intensive in a worst case scenario due to the temporary storage of elements sorted by single digits.

### Numpy Sort --> Lightweight

Built into python and is sufficient for most use cases. It attempt to provide the best of both speed and memory usage. The default sorting mechanism is Quicksort but this can be changed with arguments. This program uses Quicksort. This should be able to sort any reasonable data set but will take longer than Radix sort on average.

## Accuracy of results

The speed at which a list is sorted is highly dependant on the host computer and as such results should not be compared across machines. Furthermore, the computer's CPU clock speed and temperature should be the same between runs to guarantee accuracy. These algorithms should not cause CPU throttling but even so some may occur (eg. Some Intel CPUs stop boosting after a specific time limit regardless of temperature). For this reason, attempting to sort a large data set using multiple trials may cause the later trials to run slower thus rasing the average time needed to sort the data set. To mitigate this effect when comparing algorithms directly, be sure to run the program with the exact same settings (data set size, max number, number of trials, timing method). Lastly, for performance reasons the list of unsorted numbers is only generated once regardless of the number of trials. This means that if the generated data set is favorable of unfavorable for the algorithm being used the effect will continue throughout all trials.

## License

This project is licensed under the [GPL-3.0](LICENSE.md)
GNU General Public License - see the [LICENSE.md](LICENSE.md) file for
details.
