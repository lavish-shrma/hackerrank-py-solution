r = int(input("enter the number of rows :"))
c = int(input("enter the number of columns :"))
x=[]
val=[]

for i in range(0,r):
    for j in range(0,c):
        val.insert(j, int(input("enter the %d * %d element :" %(i,j))))
    x.insert(i,val)
    val=[]
y=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, int(input("enter the %d * %d elements :" %(i,j))))
    y.insert(i,val)
    val=[]
sum=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)


# another py program to check if the year is leap year or not

def is_leap(year):
    leap = False
    if (year %4==0) and (year %100!=0 or year %400==0):
        leap = True
    # Write your logic here
    return leap

year = input(int())
print(is_leap(year))