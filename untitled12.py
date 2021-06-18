cc = "123456789"
c = list(cc)
b = len(cc)
print(c)
c[-4:] = "####"

str = ""
for ele in c:
    str += ele
print(str)