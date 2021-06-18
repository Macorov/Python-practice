n1 = input("enter")
n2 = input()
o = input()
number1 = int(n1)
number2 = int(n2)
num1 = int(n1,2) 
num2 = int(n2,2) 
if o == "add":
    ans = num1 + num2
elif o == "subtract":
    ans = num1 - num2
elif o == "multiply":
    ans = num1 * num2
k = bin(ans)[2:]
p = str(k)
final = p.replace("b", "-")
print(final)
