#!/usr/bin/python3
def f(n):
	res, d = [], 2
	while d*d <=n:
		while n%d == 0:  res.append(d); n//= d
		d +=1
	return res + ([n] if n > 1 else [])
n = int(input()); print(f"{n} =", *f(n), sep=" * ")

 
