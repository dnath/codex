class Value:
    LOW = 0
    MID = 1
    HIGH = 2

def dnf_sort(arr):
    current = left = 0
    right = len(arr) - 1

    while current <= right:
        if arr[current] == Value.LOW:
            arr[left], arr[current] = arr[current], arr[left]
            left += 1
            current += 1
        elif arr[current] == Value.HIGH:
            arr[right], arr[current] = arr[current], arr[right]
            right -= 1
        else:
            current += 1

    return arr

print dnf_sort([Value.MID, Value.HIGH, Value.MID, Value.LOW, Value.HIGH, Value.LOW, Value.MID])