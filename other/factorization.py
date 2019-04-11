#!/bin/python3

#11 April 2019

fac = []

def main():
    N = int(input("Enter max factorization: "))
    fac = [[] for x in range(N+1)]

    fac[0] = 0
    fac[1] = 0 #0 and 1 don't have prime factorizations
    
    i = 2
    while i <= N:
        if fac[i] == []:
            cPrime = i
            ex = 1
            while pow(cPrime, ex) <= N:
                ex += 1
            ex -= 1
            while ex > 0:
                val = pow(cPrime, ex)
                mult = 1
                while val * mult <= N:
                    if mult % cPrime == 0:
                        mult += 1
                    else:
                        fac[val * mult].append([cPrime,ex])
                        mult += 1
                ex -= 1
        i += 1

#    print(fac)
#    for i in range(2, N+1):
#        print(i, ":", fac[i])
    print(fac[N])

if __name__ == "__main__":
    main()
