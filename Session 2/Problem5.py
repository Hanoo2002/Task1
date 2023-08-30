def find_sum(arr, target):
    arr.sort()
    left = 0
    right = len(arr) -1
    while left < right :
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return False

nums = input("Enter ")
nums = nums.split(" ")
nums = [eval(i) for i in nums]
target = int(input("Enter Target "))
out = find_sum(nums, target)
if not out :
    print("NO")
else:
    print(f"Yes, {out[0]} + {out[1]} = {target}")