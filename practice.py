import time

name = input("Enter your Name: ").title()
hours = int(time.strftime("%H"))

if (hours>=4 and hours<12):
    print("Good morning",name)
elif(hours>=12 and hours>16):
    print("good afternoon",name)
elif(hours>=16 and hours<20):
    print("good evening",name)
else:
    print("good night",name)


# 2 match case program
    

my_day = input("enter a day to check what to-do today :- ")
x = 0

match my_day:
    case my_day if my_day == "sunday":
        print("it is %s today, party accordingly! you have office tomorrow " %(my_day))
    case my_day if my_day =="monday":
        print("it is %s and its a work day" %(my_day))
    case my_day if my_day =="tuesday":
        print("it is %s and its also a work day" %(my_day))
    case my_day if my_day =="wednesday":
        print("it is %s and its a wrok day" %(my_day))
    case my_day if my_day =="thursday":
        print("it is %s and its a  work day" %(my_day))
    case my_day if my_day =="friday":
        print("it is %s and its a FRIDAY NIGHT HURREY" %(my_day))
    case my_day if my_day =="saturday":
        print("it is %s and YEAH YOU CAN PARTY TONIGHT" %(my_day))
    case _:
        print("invalid input")

#  input function on python
# WAP to print sum of two numbers

x = int(input("enter first number : "))
y = int(input("enter second number : "))
print("sum of these numbers is", x + y)

# WAP to read employee data from keyboard and print the data

emp_name = str(input("enter name of emplyee :"))
emp_number = int(input("enter number of emplyee :"))
emp_salary = float(input("enter salary amount of employee :"))
emp_desig = str(input("enter the designation of employee : "))
print("the details of emplyee are : ", "\t", emp_name, emp_number, emp_salary, emp_desig)


# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.  
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of 
#  followed by  lines of commands where each command will be of the 
#  types listed above. Iterate through each command in order and perform 
# the corresponding operation on your list.

year = int(input())
if ( year >= 1900 and year * 4 ):
    print("is leap: "(year))    
    if  year >= 1900 and year * 4:
        print("Leap")

class Solution:
    def insertion_sort(arr):
     for i in range(1, len(arr)):
            j = i
            while arr[j - 1] > arr[j] and j > 0:
                arr[j - 1], arr[j] = arr[j - 1]
                j -= 1
                
arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    else:
        # Recursively calculate the height of the left and right subtrees
        left_height = height(root.left)
        right_height = height(root.right)

        # Return the maximum of the left and right subtree heights, plus 1 for the current node
        return max(left_height, right_height) + 1

print(function)

def is_leap(year):
    leap = False
    if (year %4==0) and (year %100!=0 or year %400==0):
        leap = True
    # Write your logic here
    return leap

year = input(int())
print(is_leap(year))

# Nested list


def average(array):
    # your code goes here 
    h =set(array)
    return sum(h)//len(h)

    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)