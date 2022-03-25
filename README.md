# Timing-Mini-Assignment-Comparing-2-Sorting-Algorithms

This program was made to compare the efficiency of different sorting algorithms in python.

## Getting Started

### Prerequisites

Please be sure to install the following before running the program.

- Python 3.x

## Usage

Start the program by executing the main.py file.

### Bogo Sort
Bogo sort randomly sorts the given data untill it is sorted correctly. This means with luck it could be successful the first attempt. On the other hand, there is a small chance that the list continuesly gets sorted in an incorrect way and will take infinitly long. It is reccomened that you use a small data set to maximize the chance of the sorting algorithm suceeding quickly. Max number has no effect as bogo sort does not consider it.

My implementation of bogo sort is purely for fun and should not be used for any real world applications. To check whether the random sort worked, I used pythons built-in function to sort the list and compare the 

### Radix Sort
Radix sort is theoretically the fastest sorting algorithm in this program. It works by grouping elements by their single digit place values and then ordering them. In this program, it uses counting sort as the intermidiate sorting algorithm. Max number and data set size both have an effect on this algorithm but it should not struggle with any reasonable data set. However, due to the nature of radix sort, it can be very memory intensive in a worst case scenario due to the temporary storage of elements sorted by single digits.  

### Numpy Sort
Numpy sort is built into python and is sufficent for most use cases. It attempt to provide the best of both speed and memory useage. The default sorting mechanism is quicksort but this can be changed with arguments. This program uses quicksort. This should be able to sort any reasonable data set but will take longer than radix sort on average.


## Author

- **Davis Stanko** - *Lead Developer* -
    [Website](https://davisstanko.com)

## License

This project is licensed under the [GPL-3.0](LICENSE.md)
GNU General Public License - see the [LICENSE.md](LICENSE.md) file for
details