#!/usr/bin/env python3.14t


#{P: a, b < len(arr)}
def swap(arr, a, b):
    if a >= len(arr) or b >= len(arr):
        raise Exception()
    t = arr[b]
    arr[b]=arr[a]
    arr[a]=t
#{Q: arr[a] <=> arr[b]}



def quicksort(arr, lo, hi):
    if lo >= hi or lo < 0:
        return None
    #{P: length(arr) > 0 && lo < hi}
    p = partition(arr, lo, hi)
    #{Q: arr[..p-1] <= arr[p] && arr[p] >= arr[p+1..]} sorted by 1 element

    
    #{P: arr[..p-1] <= arr[p] && arr[p] >= arr[p+1..]} sorted by 1 element
    quicksort(arr, lo, p-1)
    quicksort(arr, p+1, hi)
    #{Q: arr[lo] <= arr[lo+1] <= .... <= arr[hi-1] <= arr[hi]}

def partition(arr, lo, hi):
    pivot = arr[hi] # last elem as pivot

    i = lo

    # j is fast pointer
    # i is slow pointer, which look at element of the arr, which arr[i] > pivot
    # lets try to proove by induction
    # P:{arr[lo..hi]}
    # I: one element of arr[lo..hi] -- obviously
    # I: lets i-1 is setted and arr[..i-1] <= pivot && arr[i] > pivot for some j-1. Lets make step by j
    
    for j in range(lo, hi):
        if arr[j] <= pivot:
            
            swap(arr, i, j)
            i += 1

    # QI: j >= i && if arr[j] <= pivot then we swap arr[j] with arr[i] => new arr[i] <= pivot and i = i+1 and then arr[i] > pivot because of if-condition for arr[j]
    swap(arr, i, hi)
    # Q: for each j from arr[..i-1]: j <= arr[i] && for each j from arr[i+1...]: arr[i] > j
    return i


if __name__ == "__main__":
    arr = [9, 10, 5, 4, 1, 3, 8]
    #{P: len(arr) > 0}
    quicksort(arr, 0, len(arr)-1)
    #{Q: arr[0] <= arr[1] <= ... <= arr[n-1] <= arr[n]}

    print(arr)

