# This function takes a sorted list and an element to search for as input
def binary_search(list, element):
    middle = 0     # Initialize the middle index
    start = 0      # Initialize the start index
    end = len(list)  # Initialize the end index to the length of the list
    steps = 0      # Initialize the step count to 0

    # Continue searching as long as the start index is less than or equal to the end index
    while (start <= end):
        # Print the current step number and the current sublist being searched
        print(f"Step:{steps},{list[start:end+1]}")

        steps += 1   # Increment the step count
        middle = (start + end) // 2   # Calculate the middle index

        # If the middle element is the target, return its index
        if element == list[middle]:
            return middle
        # If the target is less than the middle element, search the left half of the list
        if element < list[middle]:
            end = middle - 1
        # If the target is greater than the middle element, search the right half of the list
        else:
            start = middle + 1

    # If the target element is not found, return -1
    return -1


# Test the function with a sample list and target element
my_list = [1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 14

binary_search(my_list, target)