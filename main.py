import random

def ins_sort(arr: list) -> None:
    # Loop through the array starting from the second element
    for currentIndex in range(1, len(arr)):
        currentValue = arr[currentIndex]
        previousIndex = currentIndex - 1 # Start from the previous element
        while previousIndex >= 0 and currentValue > arr[previousIndex]: # While the previous element is greater than the current value
            # Shift the previous element to the right
            arr[previousIndex + 1] = arr[previousIndex]
            previousIndex -= 1
        arr[previousIndex + 1] = currentValue # Insert the currentValue in the correct position

# Source array
arr = [4, 5, 1, 2, 3]

# Sort the array
ins_sort(arr)

# Print the sorted array
print(arr)
