#!/usr/bin/env python
# encoding: utf-8

# NOTA: OBSERVAR EL USO DE math.floor()

import random
import math

N = 10000

def full_calculation():
	result = 0
	for i in range(1,N+1):
		result += math.exp(i/float(N))
	return result

def exp(n):
	result = 0
	for i in range(n):
		U = random.random()
		k = math.floor(U * 10000) + 1
		result += math.exp(k/N)
	return result


def main():
	print "El valor exacto es: " + str(full_calculation())
	print "El experimento con 100 números aleatorios da como resultado: " + str(exp(100))


if __name__ == '__main__':
	main()