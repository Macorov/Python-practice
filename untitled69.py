def goodVsEvil(good, evil):
    k = good.split()
    l = evil.split()
    lst1 = []
    lst2 = []
    for num in k:
        num = int(num)
        lst1.append(num)
    for num in l:
        num = int(num)
        lst2.append(num)
    good = 0
    evil = 0
    good = 1*lst1[0] + 2*lst1[1] + 3*lst1[2] + 3*lst1[3] + 4*lst1[4] + 10*lst1[5]
    evil = 1*lst2[0] + 2*lst2[1] + 2*lst2[2] + 2*lst2[3] + 3*lst2[4] + 5*lst2[5] + 10*lst2[6]
    if good < evil:
        return "Battle Result: Evil eradicates all trace of Good', 'Evil should win"
    elif evil < good:
        return 'Battle Result: Good triumphs over Evil', 'Good should win'
    else:
        'Battle Result: No victor on this battle field', 'Should be a tie'
    return f'Battle Result: No victor on this battle field', 'Should be a tie'
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))