"""
 68.Write a program to merge 2 list without using the + operator
"""
def merge_list(list1, list2):
    merg_list = list1.copy()
    for item in list2:
        merg_list.append(item)
    return merg_list

input_list1 = list(map(int, input("Enter strings : ").split()))
input_list2 = list(map(int, input("Enter strings : ").split()))
m_list = merge_list(input_list1, input_list2)
print(f"merge list : {m_list}")

