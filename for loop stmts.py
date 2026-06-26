i=0
for i in range(10):
    print(i,end=" ")

#2
i=0
for i in range (1,11):
    print(i,end=" ")

#3
i=0
for i in range (2,21,2):
    print(i,end=" ")

#4
i=0
for i in range (1,20,2):
    print(i,end=" ")

#5
i=0
for i in range (10,0,-1):
    print(i,end=" ")

#6
i=0
for i in range (1,11):
    print(i,end=" ")

#7
i=0
for i in range(10,0,-1):
    print(i,end=" ")

#8
for i in range (65,91):
    print(chr(i),end=" ")

#9
i=0
for i in range(2,11,2):
    print(i,end=" ")

#10
i=0
for i in range(15,-1,-3):
    print(i,end=" ")

#11
i=0
for i in range(10,51,10):
    print(i,end=" ")

#12
i=0
for i in range(100,19,-20):
    print(i,end=" ")

#13
i=0
for i in range(100,-21,-20):
    print(i,end=" ")

#14
for i in range(90,64,-1):
    print(chr(i),end=" ")

#15
for i in range(65,91,1):
    print(chr(i),end=" ")

#16
for i in range(97,124,1):
    print(chr(i),end=" ")

#17
for i in range(48,59,1):
    print(chr(i),end=" ")

#18
# Uppercase A-Z
for i in range(65, 91):
    print(chr(i), end=" ")

# Lowercase a-z
for i in range(97, 123):
    print(chr(i), end=" ")

# Digits 0-9
for i in range(48, 58):
    print(chr(i), end=" ")

#19
i=1
for i in range(1,6,1):
    i=i**2
    print(i,end=" ")

#20
i=1
for i in range(1,6,1):
    i=i**3
    print(i,end=" ")

#21
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("Sum =", sum)

#22
n = int(input("Enter n: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("factorial =", fact)

#23
for i in range(20, 61):
    if i % 7 == 0:
        print(i, end=" ")

#24
for i in range(10, 50):
    if i % 3 == 0 and i%5!=0 :
        print(i, end=" ")

#25
for i in range(100, 300):
    if i % 4 == 0 and i%100!=0 :
        print(i, end=" ")

#26
for i in range(30, 70):
    if i%5!=0 :
        print(i, end=" ")

#27
for i in range(2,31,2):
    if i%5!=0 :
        print(i, end=" ")

#28
n=4
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#29
n=20
s=0
for i in range(2,n+1,2):
    s=s+i
print("Sum of even numbers:=",s)

#30
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:      
        count += 1
print("Number of factors =", count)

#31
num=int(input("enter a number: "))
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")

#32
num=int(input("enter a number: "))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum+=i
        print(i,end=" ")
print("sum of factors: ",sum)

#33
num=int(input("enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

#34
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#35
n = int(input("Enter how many terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
