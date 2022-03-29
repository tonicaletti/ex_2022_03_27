nums = [43,5,3,2,6,6]

def fct(nums):

    set_0 = set()

    for elem in nums:
        if elem in set_0:
            return elem
        else:
            set_0.add(elem)


print(fct(nums))
