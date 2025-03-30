ca = [21,10,11,15,13]
ca1 = [1, 13, 21, 5, 7]


def fselsort(ca):
    for sa  in range(0, 4, 1):
        mina = ca[sa]
        minix = sa

        for sb in range(sa+ 1, 5, 1):
            if mina > ca[sb]:
                mina = ca[sb]
                minix = sb

        temp = ca[sa]
        ca[sa] = ca[minix]
        ca[minix] = temp
        # print(ca)
    return ca
print(fselsort(ca))
print(fselsort(ca1))

