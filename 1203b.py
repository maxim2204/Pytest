import timeit
def palka(spisok2):
    spisok = spisok2[:]
    n = len(spisok)
    for i in spisok:
        if spisok.count(i)%2 != 0:
            return False
    finish = []
    for i in range(n//4):
        x1 = min(spisok)
        x2 = max(spisok)
        finish.append((x1,x2))
        spisok.remove(x1)
        spisok.remove(x1)
        spisok.remove(x2)
        spisok.remove(x2)
    s = finish[0][0] * finish[0][1]
    for i in range(len(finish)):
        if s != finish[i][0] * finish[i][1]:
            return False
    return True


#x = timeit.timeit("palka([10,5,1,10,5,1,1,1])", "from  __main__ import palka", number=1000000)
#print(x)
#assert palka([10,5,1,10,5,1,1,1]) == False
#assert palka([1,1,1,1,1,1,1,1]) == True
#assert palka([10000,10000,10000,10000]) == True
#assert palka([10,5,2,10,1,1,2,5]) == True


def factors(n,k):
    fac = []
    for i in range(1,n+1):
        if n % i == 0:
            fac += [i for j in range(k)]
    return fac

#assert palka(factors(12,2)) == True
x = timeit.timeit("palka(L)", "from  __main__ import palka, factors;  L = factors(100000,200)", number=100)
print(x)