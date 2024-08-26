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

# Generate a random list of 20 numbers
source=[]
n=20
for i in range(n):
    source.append(random.randint(1,1000))

# Print the unsorted list
print("Original source: ", source)

# Sort the list
ins_sort(source)

# Print the sorted list
print("Sorted monotonic decreasing source: ", source)