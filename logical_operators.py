a=int(input("enter a number: "))
print(a%2==0 and a%3==0)
print("--------------------------")

#2
a=int(input("enter a number: "))
print(a%4==0 and a%6!=0)
print("--------------------------")

#3
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
print(a<=b and a>=c)
print("--------------------------")

#4
a=int(input("enter a number: "))
print(20<=a<=40)
print("--------------------------")

#5
a=int(input("enter a number: "))
b=int(input("enter b number: "))
print(a%10==0 and b%10!=0)
print("--------------------------")

#6
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
d=int(input("enter d number: "))
print(a>=35 and b>=35 and c>=35 and d>=35)
print("------------------------------------------")

#7
a=input("enter: ")
print(a in "a,e,i,o,u,A,E,I,O,U")
print("--------------------------")

#8
chr=input("enter a chr: ")
print('A' <= chr <= 'Z')
print("--------------------------")

#9
n=int(input("enter a num: "))
print(0 <= n <= 9)
print("--------------------------")

#10
pin=int(input("enter a num: "))
print(1000 <= pin <= 9999)
print("--------------------------")

#11
chr=input("enter chr letter: ")
print('a'<= chr <='z' or 'A' <= chr <= 'Z')

#12
ch = input()
print(not ch.isalnum())

#13
a = 10
b = 10
c = 10
print(a == b == c)

#14
a = 10
b = 10
c = 20
print(a == b or b == c or a == c)

#15
a = 10
b = 10
c = 20
print(a != b or b != c or a != c)
