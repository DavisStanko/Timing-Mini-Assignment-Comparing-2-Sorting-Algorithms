import random
import numpy as np
import time
# data set random number generation
data_set = []
data_set_size = 100
max_number = 10000

for i in range(data_set_size):
    data_set.append(random.randint(0, max_number))

print(f"\nUnsorted data set:\n{data_set}\n")

# timing variables
start = 0
end = 0
difference = 0

# Default numpy sort no arguments
start = time.time()
sorted_data_set = np.sort(data_set)
end = time.time()
difference = end - start
print(f"Sorted data set:\n{sorted_data_set}")
print(f"Time taken: {difference} seconds")
