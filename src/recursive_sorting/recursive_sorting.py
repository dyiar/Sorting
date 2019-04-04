# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if not len(arrA) or not len(arrB):
        return arrA or arrB

    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    i = j = 0
    # TO-DO
    while (len(merged_arr) < len(arrA) + len(arrB)):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1
        if i == len(arrA) or j == len(arrB):
            merged_arr.extend(arrA[i:] or arrB[j:])
            break
    
    return merged_arr

# def merge(a,l,m,r):

    # n1 = m - l + 1
    # n2 = r - m
    # L = [0] * n1
    # R = [0] * n2

    # for i in range(0, n1):
    #     L[i] = a[l + i]
    # for i in range(0, n2):
    #     R[i] = a[m + i + 1]

    # i, j, k = 0, 0, l
    # while i < n1 and j < n2:
    #     if L[i] > R[j]:
    #         a[k] = R[j]
    #         j+=1
    #     else:
    #         a[k] = L[i]
    #         i +=1
    #     k +=1

    # while i < n1:
    #     a[k] = L[i]
    #     i += 1
    #     k +=1 

    # while j < n2:
    #     a[k] = R[j]
    #     j += 1
    #     k +=1


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    arr = merge(merge_sort(left), merge_sort(right))

    return arr

# print(merge_sort([0,1,2,3,4,5,6,7,8,9]))

# def merge_sort(a):
#     current_size = 1

#     #outer loop for traversing each sub array of current size
#     while current_size <= len(a)-1:
#         left = 0
#         #inner loop for merge call in the sub array
#         #each complete iteration sorts the iterating sub array
#         while left <= len(a) -1:

#             #mid index = left index of sub array + current sub array size-1
#             mid = left + current_size-1

#             #(False result, True result)
#             #[condition] can use current_size
#             #if 2* current_size < len(a)-1
#             #else len(a)-1
#             right = ((2* current_size + left -1, len(a) -1)[2*current_size + left -1 > len(a)-1])

#             #merge call for each sub array 
#             merge(a, left, mid, right)
#             left = left + current_size*2

#         current_size = 2*current_size

# a = [12, 11, 13, 5, 6, 7] 
# print("Given array is ") 
# print(a) 
  
# merge_sort(a) 
  
# print("Sorted array is ") 
# print(a)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
