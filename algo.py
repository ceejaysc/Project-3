import billionaires
import time

# Load the billionaires dataset
billionaires_data = billionaires.get_billionaire()

# Extract relevant data
worths = [b['wealth']['worth in billions'] for b in billionaires_data]

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Measure performance
def measure_time(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    return sorted_data, end_time - start_time

# Test Quick Sort
sorted_quick, quick_sort_time = measure_time(quick_sort, worths.copy())
print(f"Quick Sort Time: {quick_sort_time:.6f} seconds")

# Test Merge Sort
sorted_merge, merge_sort_time = measure_time(merge_sort, worths.copy())
print(f"Merge Sort Time: {merge_sort_time:.6f} seconds")

# Check if both sorted lists are equal
print("Sorted lists are equal:", quick_sort_time == merge_sort_time)
