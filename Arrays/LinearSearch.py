# Program: Linear Search in Python
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(col, key):
    """
    Search for key in array using Linear Search
    Returns index if found, else -1
    """
    for i in range(len(col)):
        if col[i] == key:
            return i
    return -1 # Return -1 if not found

col = eval(input("Enter the list: "))
key = int(input("Enter the key: "))

res = linear_search(col, key)

if res!= -1:
    print(f"Element {key} found at index {res}")
else:
    print(f"Element {key} not found in array")
    
