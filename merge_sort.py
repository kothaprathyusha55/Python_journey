def merge(arr, start, mid, end):
    leftsize = mid - start + 1
    rightsize = end - mid
    arr1 = [0] * leftsize
    arr2 = [0] * rightsize
    for i in range(leftsize):
        arr1[i] = arr[start + i]
    for j in range(rightsize):
        arr2[j] = arr[mid + 1 + j]
    i = j = 0
    k = start
    while i < leftsize and j < rightsize:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < leftsize:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < rightsize:
        arr[k] = arr2[j]
        j += 1
        k += 1
def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        merge(arr, start, mid, end)
arr = list(map(int, input("Enter numbers: ").split()))
mergesort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
