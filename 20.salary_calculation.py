"""
20. Write a programthat will give you the in hand salary after
 deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between
 5-10 lakh–10%),(11-20lakh–20%),(20< _– 30%)(0-1lakh print k)
"""
def calc_hand_in_salary(salary):
    HRA = 0.10
    DA = 0.05
    PF = 0.03
    sub_total_deduction = HRA+DA+PF
    if salary>= 500000 and salary>= 1000000:
        salary -=sub_total_deduction+0.10
        return salary
    elif salary>= 1100000 and salary>= 2000000:
        salary -= sub_total_deduction + 0.20
        return salary
    elif salary>= 2000000:
        salary -= sub_total_deduction + 0.30
        return salary
    elif salary >= 0 and salary<= 100000:
        return "k"
    else:
        return salary*sub_total_deduction

salary = float(input("Enter your salary: "))
in_hand_salary = calc_hand_in_salary(salary)

print(f"the in hand salary after deduction is {in_hand_salary}")