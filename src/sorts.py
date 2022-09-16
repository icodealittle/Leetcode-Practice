import random


def mmerge_sort(arr: []) -> []:
    """
    Not in place implementation
    Only works when even
    """
    if len(arr) == 1:
        return arr
    if len(arr) == 0:
        return False

    lst = []
    left = 0
    right = len(arr)

    # [4, 3, 8 ,7]
    def sort(arr, left, right, lst):
        # Check to see if i"m over
        if left > right:
            return
        mid = left + right // 2  # Tree like mid? increment by 1 to change
        if arr[mid] < arr[len(arr)]:
            save = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = save

        sort(arr[left:mid], left + 1, right, lst)

        sort(arr[mid:right], left, right - 1, lst)
        # Call merge sort on each piece of the divided array

        return lst

    return sort(arr, left, right, lst)


def merge_sort(arr: []) -> []:
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:len(arr)]
    start = 0
    end = len(arr) // 2

    while left < right:
        mid = start + end // 2


def quick_sort(arr:[])->[]:
    """
    designed for recursive implementation
    > can be stable...
    piv rules =
        1. Always pick the first element as a pivot.
        2. Always pick the last element as a pivot (implemented below)
        3. Pick a random element as a pivot.
        4. Pick median as the pivot.

        The key process in quickSort is a partition().
         The target of partitions is:
          1. given an array and an element x of an array as the pivot
          2. put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x
          3. and put all greater elements (greater than x) after x. All this should be done in linear time.
    """
    # Piv can be the first element of the last element
    if len(arr) == 0:
        return False
    left = 0
    right = len(arr)
    piv = arr[0]
    def sort(arr,left, piv):
        pass



def insertion_sort():
    pass


def linear_sort():
    pass


def mergeSort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst[:len(lst)]

    mid = len(lst) // 2
    right = lst[0:mid]
    left = lst[mid:len(lst)]

    newright = mergeSort(right)
    newleft = mergeSort(left)
    newLst = merge(newright, newleft)
    return newLst


def merge(right, left):
    index_right = 0
    index_left = 0
    lst = []

    while index_right < len(right) and index_left < len(left):
        if right[index_right] <= left[index_left]:
            lst.append(right[index_right])
            index_right = index_right + 1
        else:
            lst.append(left[index_left])
            index_left = index_left + 1
    lst.extend(right[index_right:])
    lst.extend(left[index_left:])
    return lst

''' When we do trees...
def heap_sort():
    pass
'''


def tim_sort():
    """
    About:
     sorting algorithm based on Insertion Sort and Merge Sort.
     Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().

    How To:
    We divide the Array into blocks known as Run.
    We sort those runs using insertion sort one by one
    and then merge those runs using the combine function
    used in merge sort. If the size of the Array is less
    than run, then Array gets sorted just by using Insertion Sort.
    The size of the run may vary from 32 to 64 depending upon the size
    of the array. Note that the merge function performs well when size
    subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.

    """
    pass


def count_sort():
    pass


def gen_arr(ran):
    arr = []
    for i in range(ran):
        arr.append(random.randint(1, 100))
    return arr


def quickSort(arr):
    right = []
    mid = []
    left = []

    if len(arr) > 1:
        pivot = arr[0]
        for _ in arr:
            if _ < pivot:
                left.append(_)
            if _ > pivot:
                right.append(_)
            if _ == pivot:
                mid.append(_)
        return quickSort(left) + mid + quickSort(right)
    else:
        return arr

if __name__ == '__main__':
    #print(merge_sort([4, 3, 8, 7]))
    #print(mergeSort(gen_arr(10)))
    print(quick_sort(gen_arr(10)))
