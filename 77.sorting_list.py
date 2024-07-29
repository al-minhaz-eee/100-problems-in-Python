"""
Write a program that can sort a given unsorted list. Dont use any built in
 function for sorting.
"""
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag ==0:
            break
    print(arr)
def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min =j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)

list1=[2, 32, 12, 23, 13, 4, 64, 222, 100]
bubble_sort(list1)

list2=[9, 88, 832, 12, 11, 123, 1, 10, 3, 4, 5]
selection_sort(list2)
