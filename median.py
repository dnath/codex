import heapq

# O(n) time complexity
def get_median(arr):
    lower_half, upper_half = [], []
    for ele in arr:
        if lower_half == [] or lower_half[0][1] >= ele:
            heapq.heappush(lower_half, (-ele, ele))
            if len(lower_half) > len(upper_half) + 1:
                key, item = heapq.heappop(lower_half)
                heapq.heappush(upper_half, (-key, item))
        else:
            heapq.heappush(upper_half, (ele, ele))
            if len(upper_half) > len(lower_half) + 1:
                key, item = heapq.heappop(upper_half)
                heapq.heappush(lower_half, (-key, item))

    if len(lower_half) == len(upper_half):
        return lower_half[0][1], upper_half[0][1]
    elif len(lower_half) > len(upper_half):
        return lower_half[0][1]
    else:
        return upper_half[0][1]


print get_median([2,2,2,2])
print get_median([3,4,1,2])
print get_median([2,2,2,1,2])
print get_median([4,5,2,1,3])
