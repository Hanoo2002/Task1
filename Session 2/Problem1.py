def binary_search(arr,left, right, key):
 
    if right >=left:
        mid = (right +left) // 2

        if arr[mid] == key:
            return mid
 
        elif arr[mid] > key:
            return binary_search(arr,left, mid - 1, key)
 
        else:
            return binary_search(arr, mid + 1, right, key)
 
    else:
        return -1
    


arr = [ 1, 2, 4, 9 , 15, 20, 36 , 43  ]

result = binary_search(arr, 0, len(arr)-1, 20)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")