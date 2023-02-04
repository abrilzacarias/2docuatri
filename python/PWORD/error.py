def fact(n):
    if n == 0:
        r = 1
    else:
        #n=n+1
        r = n * fact(n - 1)

    return r

divisor = 0
while divisor < 11 :
    divisor+=1
    #print(divisor)
    print (fact(divisor))
    resulta = 100000 / (479001600 - fact(divisor))
    #print(fact(divisor))

print("")
print(resulta)
