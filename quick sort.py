arr = [28,21,27,12,19,29,44,78,87,66,31,76,58,88,83,97,41,99,44]
n = len(arr)
#moves all numbers that are less than a random “pivot” number to the left of the “pivot” number. Then moves all numbers greater than the “pivot” to the right of it. The moved numbers are not necessarily in order. Returns the index of the “pivot”.
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
#starts at the “end” number and goes through each number moving towards the left until it finds a number lower than the “pivot”.
        while low <= high and array[high] >= pivot:
            high = high - 1

#starts at the “start” number and goes through each number moving towards the right until it finds a number lower than the “pivot”.
        while low <= high and array[low] <= pivot:
            low = low + 1

#after it moves the lower numbers to the left and the greater numbers to the right, it exits the loop. It places the pivot number between the two sides.
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

#m 
def quick_sort(array, start, end):
# 
    if start >= end:
        return
	# 
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

    return "brrfg"

print(quick_sort([28,21,27,12,19,29,44,78,87,66,31,76,58,88,83,97,41,99,44], 0, 17)
