from math import floor
target = 2
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]

def pivotbinary(nums):
    L = 0
    R = len(nums)-1
    while(L <= R):
        mid = floor((L+R)/2)+1
        print(L, R, mid)
        if nums[L] <= nums[mid-1] and nums[mid] <= nums[R]:
            return mid
        elif nums[L] > nums[mid-1]:
            R = mid-1
        elif nums[mid] > nums[R]:
            L = mid

def binarysearch(nums, target):
    L, R = 0, len(nums)-1
    while(L <= R):
        mid = floor((L+R)/2)
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            L = mid +1
        elif nums[mid] > target:
            R = mid-1
    return False

pivot = pivotbinary(nums)
print(pivot)


#bool_1 = binarysearch(nums[0:pivot], target)
#bool_2 = binarysearch(nums[pivot:], target)

#print(bool_1, bool_2)
