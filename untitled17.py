def modifylist(lst):
        lst = [elt.strip() if type(elt) is str else elt for elt in lst]
        while '' in lst:
                lst.remove('')
        return lst
p = ['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5']
k = modifylist(p)
l = min(k)
print(l)