n=int(input("enter n value: "))
if n>0:
    print("positive num")
elif n<0:
    print("negative num")
else:
    print("zero")

#2
a=input("enter a number: ")

if 'a'<=a<='z' or 'A'<=a<='Z':
    print("Alphabet")
elif '0'<=a<='9':
    print("digits")
else:
    print("symbol")

#3
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
if a>=b or a>=c:
    print("a is big")
elif b>=a or b>=c:
    print("b is big")
else:
    print("c is big")
