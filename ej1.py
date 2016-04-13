#!/usr/bin/env python
# encoding: utf-8

import random

# Recordar que la media (o esperanza) muestral de X esta dada por (X1 + X2 + ... + Xn) / n , siendo
# X1 , ... , Xn las muestras de X. 
# A su vez, la varianza muestral de X esta dada por (((X1 - E(X)) ** 2) + ... + ((Xn - E(X)) ** 2)) / (n - 1)

def exp(n):
    res = []			
    for k in range(n):
        tmp = 0
        cards = [i for i in range(1, 101)]
        random.shuffle(cards)
        
        #print "cartas: " + str(cards)
        
        for r in range(1, 101):
            #print "carta:" + str(r)
            if r == cards[r - 1]:
                tmp += 1

                #print "exitos:" + str(tmp)

        res.append(tmp)

        #print "lista de exitos:" + str(res)
    
    #Esperanza = #E[X] = #(exitos) / #(experimentos)
    
    esperanza = float(sum(res)) / float(n)
    
    #E[X^2] = (exitos^2) / #(experimentos)
    #Varianza = #V[X] = E[X^2] - (E[X])^2
    
    esperanza2 = 0.0
    
    for i in res:
        esperanza2 += (i)** 2
        #print "esperanza:" + str(esperanza)
        #print "esperanza2:" + str(esperanza2)
        
    esperanza2 = float(esperanza2)/n

    varianza = esperanza2 - (esperanza)**2
    return (esperanza, varianza)

def main():
    print "exp(1000): " + str(exp(1000))
    #print "exp(1000): " + str(exp(1000))
    #print "exp(10000): " + str(exp(10000))
    #print "exp(100000): " + str(exp(100000))
    #print "exp(1000000): " + str(exp(1000000))


if __name__ == "__main__":
    main()
