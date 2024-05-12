import time

# *** SORTING ALGORITHMS ***

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data


def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data


def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [i for i in data[1:] if i <= pivot]
    right = [i for i in data[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def heap_sort(data):
    def heapify(data, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # See if left child is larger than root
        if left < n and data[i] < data[left]:
            largest = left

        # See if right child is larger than largest so far
        if right < n and data[largest] < data[right]:
            largest = right

        # If largest is not root
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            # Recursively heapify the affected sub-tree
            heapify(data, n, largest)

    n = len(data)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)

    return data


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def radix_sort(data):
    # Only sort for positive numbers
    if min(data) < 0:
        raise ValueError("Radix sort only works for positive numbers")

    max_value = max(data)
    exp = 1
    while max_value // exp > 0:  # Loop through each digit position
        output = [0] * len(data) 
        count = [0] * 10  # Counting sort based on digit

        for i in range(len(data)):
            index = data[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):  # Cumulative sum to find output index
            count[i] += count[i - 1] 

        i = len(data) - 1
        while i >= 0:  # Place numbers in sorted order
            index = data[i] // exp
            output[count[index % 10] - 1] = data[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(data)):  # Copy output array to original array
            data[i] = output[i]

        exp *= 10
    return data

def cocktail_sort(data):
    swapped = True
    start = 0
    end = len(data) - 1
    while swapped:
        swapped = False
        # Forward pass
        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:
            break

        # Backward pass
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        start += 1
    return data

# *** USER INTERFACE ***
algorithm_choices = {
    "1": bubble_sort,
    "2": merge_sort,
    "3": quick_sort,
    "4": heap_sort,
    "5": insertion_sort,
    "6": selection_sort,
    "7": radix_sort,
    "8": cocktail_sort
}

while True:
    print("\nChoose a sorting algorithm:")
    for key, value in algorithm_choices.items():
        print(f"{key}. {value.__name__}")  # Display algorithm names
    choice = input("Enter your choice (or 'q' to quit): ")

    if choice == 'q':
        break

    if choice in algorithm_choices:
        break
    else:
        print("Invalid choice. Please try again.")

# *** FILE READING ***
try:
    with open("numbers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]
except FileNotFoundError:
    print("Error: File 'numbers.txt' not found.")
    exit()  

# *** TIMING AND SORTING ***
start_time = time.time()
sorted_numbers = algorithm_choices[choice](numbers.copy())  # Pass a copy to avoid modifying the original
end_time = time.time()

print("Sorted Numbers:", sorted_numbers)
print("Execution time:", end_time - start_time, "seconds")
