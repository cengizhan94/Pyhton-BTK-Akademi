"""
x = input("number1 : ") #inputta algılanan type String olarak algılanır.
y = input("number2 : ")
toplam = int(x) +int(y)
print(type(x))
print(type(y))
print(toplam)
"""

x=5                 #int
y=2.5               #float
name = "Cengiz"     #str
isOnline = True     #boolean


#Type Conversion
#int to float

x=float(x)
print(x)
print(type(x))


#float to int

y = int(y)
print(y)
print(type(y))

result = x+y
print(result)
print(type(result))

#bool to str
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

#bool to int

isOnline = True
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))