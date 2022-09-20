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


# Given two sorted integer arrays, return an array that combines both of them and is also sorted.
def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans


nums2 = [1, 62, 24, 6, 8, 19, 14, 15]
nums2.sort()
print(combine(nums, nums2))
