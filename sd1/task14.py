#!/usr/bin/env python3.14t

#{P: len(arr) > 0}
def find_max(arr):
    # base of induction: if len(a) == 1, then max(arr) == arr[0] obviously
    max_value = arr[0] 
    if len(arr) > 1:
        for i in range(1, len(arr)):
            # induction step, lets res = max(arr[:i-1]), try to proof that it is correct after algorithm
            # 1) {P: res = max(arr[:i-1]) && arr[i] <= res}
            # 2) {P: res = max(arr[:i-1]) && arr[i] > res
            if arr[i] > max_value:
                max_value = arr[i]
            # 1) {Q: res = max(arr[:i])} # without changing
            # 2) {Q: res = max(arr[:i])} # within changing the res variable

    return max_value
# {Q: res = max(arr[:len(arr)])} by induction step

if __name__ == "__main__":
    print(find_max([1,5,6,0]))
    # {P: len(arr) > 0} res = find_max(arr) {Q: res = max(arr)}
    # by induction -- see above
