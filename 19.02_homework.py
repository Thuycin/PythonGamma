# # 1. What will this code output?
s = "abcdef"
print(s[1:4])
#bcd
print(s[:3])
#abc
print(s[::2])
#ace
print(s[::-1])
#fedcba

# 2. The user enters numbers separated by spaces as one string.
# The program should create a list of numbers, remove duplicate elements,
# sort the list in ascending order, and print the result.
lst = input("Enter numbers, spaces: ")
new_lst = []
for x in lst:
    if x.isdigit() and x not in new_lst:
        new_lst.append(x)
        new_lst.sort()
print(new_lst)

# 3. The program should remove spaces, ignore letter case,
# check whether the string is a palindrome
# , and print YES or NO.
test_str = input("Enter a string: ")
def palindrome():
    new_str = test_str.replace(" ","").lower()
    if new_str == new_str[::-1]:
        print("YES, this is a palindrome")
    else:
        print("NO, this is not a palindrome")
palindrome()