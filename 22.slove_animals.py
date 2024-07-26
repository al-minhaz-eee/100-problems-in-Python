"""
 22.Write a program that will tell the number of dogs and chicken are
 there when the user will provide the value of total heads and legs.
"""

def slove_animals(H, L):
    if H<0 or L<0 or L%2!=0 or H>L/2:
        return "No solution"
    D = L//2-H
    C = H - D
    if D<0 or C<0:
        return "No solution"
    return f"the number of dogs are {D} and chicken are {C}"

heads = int(input("How many heads are there? "))
legs = int(input("How many legs are there? "))

print(slove_animals(heads, legs))
