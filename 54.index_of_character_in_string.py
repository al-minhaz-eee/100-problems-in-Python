"""
 54.Find the index position of a particular character in another string.

"""
def count_index(string, ch):
    count=0
    for char in string:
        count += 1
        if char == ch:
            yield count-1

sen = input('Enter a sentence ')
ch = input('Enter a character for index position ')
positions_ch = count_index(sen, ch)
print(f"index(s) of {ch} : ", end="")
for position in positions_ch:
    print(position, end=" ")
