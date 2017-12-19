maximo =int(input("calculame primos hasta el numero:"))
lista= []
for number in range(maximo,1,-1):
    divisor = number-1
    while number % divisor is not 0 and divisor > 1:
        divisor = divisor - 1
        #print ("numero {} divisor {}".format(number,divisor))
    else:
        if divisor == 1:
            lista.append(number)
            #print ("{} ".format(number),end='')
#print("")
#print("ahora en modo lista")
#print (lista)
print ("ordenados de menor a mayor")
lista.sort()
print (lista)
