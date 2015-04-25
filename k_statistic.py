import heapq

# O(n) time complexity
def get_k_statistic(arr, k):
    if k > len(arr) or k < 1:
        return None

    lower_half, upper_half = [], []
    for ele in arr:
        if lower_half == [] or lower_half[0][1] >= ele:
            heapq.heappush(lower_half, (-ele, ele))
            if len(lower_half) > k:
                key, item = heapq.heappop(lower_half)
                heapq.heappush(upper_half, (-key, item))
        else:
            heapq.heappush(upper_half, (ele, ele))
            if len(upper_half) > len(arr) - k:
                key, item = heapq.heappop(upper_half)
                heapq.heappush(lower_half, (-key, item))

    return lower_half[0][1]


print get_k_statistic([2,2,2,2], 2)
print get_k_statistic([3,4,1,2], 1)
print get_k_statistic([3,4,1,2], 4)
print get_k_statistic([3,4,1,2], 5)
print get_k_statistic([2,2,2,1,2], 3)
print get_k_statistic([4,5,2,1,3], 4)
