n=int(input("enter a integer: "))
if n>0:
    print("positive number: ")
else:
    print("negative number")

#2
n=int(input("enter number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")

#3
age=int(input("enetr age: "))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

#4
a=int(input("enter a number: "))
b=int(input("enter b number: "))
if a>b:
    print("ais big")
else:
    print("b is big")

#5
ch=input("enter character: ")
if ch in ['a','e','i','o','u']:
    print("vowel")
else:
    print("not vowel")

#6
ch=input("enter ALPHABET: ")
if 'A'<=ch<='Z':
    print("ALPHABET")
else:
    print("NOT ALPHABET")

#7
user=input("enter useer name: ")
pwd=input("enter password: ")
if user=="logic" and pwd==1234:
    print("login success")
else:
    print("error:invalid success")

#8
a=int(input("enter number between 30 to 50: "))
if 30<= a <=50:
    print("valid number entered")
else:
    print("invalid number entered")


