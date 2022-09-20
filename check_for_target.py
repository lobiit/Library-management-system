def check_for_target(arr):
    left = 0
    right = len(arr) - 1
    target = 13

    while left < right:
        curr = arr[left] + arr[right]

        if curr == target:
            print(arr[left])
            print(arr[right])
            return True
        if curr > target:
            right -= 1
        else:
            left += 1


nums = [1, 2, 4, 6, 8, 9, 14, 15]
print(check_for_target(nums))
