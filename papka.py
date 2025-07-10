def misol(sonlar):
    natija = []
    for son in sonlar:
        if son % 2 != 0:
            natija.append(son ** 2)
    return natija
print(misol([1, 2, 3, 4, 5]))
