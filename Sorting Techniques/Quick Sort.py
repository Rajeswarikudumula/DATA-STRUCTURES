# Program: Quick Sort in Python
# Time Complexity: O(n log n) avg, O(n^2) worst
# Space Complexity: O(log n) due to recursion
# Note: In-place, NOT stable. Very fast in practice

def partition(arr, low, high):
    """
    Picks last element as pivot, places it at correct position
    Smaller elements left, larger elements right
    """
    pivot = arr[high] # Choosing last element as pivot
    i = low - 1 # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Main function that implements QuickSort
    arr[] --> Array to be sorted
    low --> Starting index
    high --> Ending index
    """
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


  arr = list(map(int, input("Enter array elements with spaces: ").split()))

  print(f"Original array: {arr}")
  quick_sort(arr, 0, len(arr) - 1)
  print(f"Sorted array: {arr}")
