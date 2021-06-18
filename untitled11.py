def DNA_strand(dna):
    
    
    p = list(dna)

    k = list()
    for word in p:
        if word == "A":
            k.append("T")
        elif word == "T":
        
            k.append("A")
        elif word == "C":
            k.append("G")
        elif word == "G":
            k.append("C")
    str = ""
    for ele in k:
        str += ele
    return str
print(DNA_strand("ATA"))