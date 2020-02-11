#Yanira Manzano
#2/11/2020
#List of Operators

from statistics import mean
from statistics import median
from statistics import mode

#lists
my_lst = []
even_lst =[]
odd_lst = []

#User Input (int only)
print("PEnter 5 numeric values:")
user1 = int(input("> "))
user2 = int(input("> "))
user3 = int(input("> "))
user4 = int(input("> "))
user5 = int(input("> "))

#The list will have 5 users inputed as a number
my_lst.append(user1)
my_lst.append(user2)
my_lst.append(user3)
my_lst.append(user4)
my_lst.append(user5)

# Method Functions that will help with the list of users after begin inputed
sort = sorted(my_lst)
add_total = sum(my_lst)
prod_total = user1 * user2 * user3 * user4 * user5
average = mean(my_lst)
middle = median(my_lst)
maxi = max(my_lst)
mini = min(my_lst)
no_duplicates = []

#The For loop
for n in my_lst:
    if n not in no_duplicates:
        no_duplicates.append(n)
for i in my_lst:
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
        
#Statements
print(f"Your list is {my_lst}")
print(f"Your list is sorted: {sort}")
input("Continue?")
print(f"The sum of your list is {add_total}")
print(f"The product of your list is {prod_total}")
input("Input anything to continue..")
print(f"The mean is {average}")
print(f"The median is {middle}")
input(f"Continue?")      

#The rest of the print statement is what you inputed into the list.
#It will tell you what things will appear specific: such as max, min, etc
print(f"The largest number is {maxi}")
print(f"The smallest number is {mini}")
input(f"Input anything to continue..")
print(f"Your list with duplication are {no_duplicates}")
print(f"Your list with even numbers {even_lst}")
print(f"Your list with odd numbers {odd_lst}")
print("Please input a random number.")
user6 = int(input("> "))
if user6 == user1:
    print(f"Your input, {user6}, equals {user1} on the list")
if user6 == user2:
    print(f"Your input, {user6}, equals {user2} on the list")
if user6 == user3:
    print(f"Your input, {user3}, equals {user3} on the list")
if user6 == user4:
    print(f"Your input, {user4}, equals {user4} on the list")
if user6 == user5:
    print(f"Your input, {user5}, equals {user6} on the list")
print("""Clear! You did something.""")
