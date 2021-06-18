def capital(k):
    #k = {'state': 'Maine', 'capital': 'Augusta'}
    #print(k["state"])
    con = k["state"]
    cap = k["capital"]
    final = f"The capital of {con} is {cap}"
    return final
print(capital({"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}))