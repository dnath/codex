import heapq

# O(n) time complexity
def get_k_statistic(arr, k):
    if k > len(arr) or k < 1:
        return None

    lower_k_part, rest = [], []
    for ele in arr:
        if lower_k_part == [] or lower_k_part[0][1] >= ele:
            heapq.heappush(lower_k_part, (-ele, ele))
            if len(lower_k_part) > k:
                key, item = heapq.heappop(lower_k_part)
                heapq.heappush(rest, (-key, item))
        else:
            heapq.heappush(rest, (ele, ele))
            if len(rest) > len(arr) - k:
                key, item = heapq.heappop(rest)
                heapq.heappush(lower_k_part, (-key, item))

    return lower_k_part[0][1]


print get_k_statistic([2,2,2,2], 2)
print get_k_statistic([3,4,1,2], 1)
print get_k_statistic([3,4,1,2], 4)
print get_k_statistic([3,4,1,2], 5)
print get_k_statistic([2,2,2,1,2], 3)
print get_k_statistic([4,5,2,1,3], 4)
