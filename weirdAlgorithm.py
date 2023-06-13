"""
Consider an algorithm that takes as input a positive integer n
. If n
 is even, the algorithm divides it by two, and if n
 is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n
 is one. For example, the sequence for n=3
 is as follows:
3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a given value of n.
"""

def Algo(N):
	while N>0:
		if N == 1:
			break
		if N%2 == 0:
			N = N//2
			print(N, end=' ')
		else:
			N *= 3
			N += 1
			print(N, end=' ')

x = int(input('Enter a number: '))
print(x, end=' ')
Algo(x)

"""
Problem Link: https://www.codechef.com/problems/WALG?tab=statement
"""
