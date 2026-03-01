# Task1.
# 1. Create an empty list;
# 2. Input numbers;
# 3. Stop when enters the word "stop";
# 4. Convert all valid entries to integers;
# 5. Print the sum, the smallest value, and the list itself;
lst = []
s = 0
x = 0
while True:
    a = input("Enter number only OR 'stop' to exit: ")
    if a.replace(" ", "").lower() == "stop":
        break
    for x in a:
        if x.isdigit():
            x = int(x)
            s += x
            lst.append(x)
            sorted_lst = sorted(lst)
    print(f"The sum of all valid numeric entry is: {s}")
    print(f"The smallest value of the valid entry is: {sorted(lst)[0]}")
    print(f"The list of numbers by order of entry is: {lst}")

# Task 2.
# You are given a string: "python is awesome!"
# Create a new string using a for loop:
# • Replace every space with «_»;
# • Replace every vowel by #;
# • Add each transformed character into a list
# print it out.
string1 = "python is awesome!"
string0 = []

for n in string1:
    if n in ['a','e','o','i','u']:
        string0.append(n)
        string1 = string1.replace(n,'#')
    if n == " ":
        string0.append(n)
        string1 = string1.replace(n,'_')
print(f"Symbols that were transformed separated by /: {"/".join(string0)}")
print(f"String after being transformed: {string1}")

# Task 3.
# 1. Ask the user for any positive number N;
# 2. Create a list containing a countdown from N to 1 using a while loop.
# Then print:- The list
# A string where all numbers are joined with «->»
lst = []
c = -1
while True:
    n = input("Enter a number: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("Not a number, re-enter")

for i in range(int(n)):
    c += 1
    x = int(n) - c
    lst.append(x)
y = '->'.join(str(t) for t in lst)
print(f"{lst} {y}")