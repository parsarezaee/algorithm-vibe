def increasingTriplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num  
        elif num <= second:
            second = num  
        else:
            return True
    return False

print(increasingTriplet([2, 1, 5, 0, 4, 6]))
