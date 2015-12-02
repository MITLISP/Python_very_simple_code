def sqrt():
	x = int(raw_input("what is x?"))
	ans = 0
	while ans*ans < x:
		ans = ans + 1
		print "current ans is: %d " % ans
	print "The square root of %d is %d." % (x,ans)	



def solve(numLegs, numHeads):
	for numChicks in range(0, numHeads + 1):
		numPigs = numHeads - numChicks
		totLegs = 4*numPigs + 2*numChicks
		if totLegs == numLegs:
			return (numPigs, numChicks)
		return (None, None)

def barnYard():
	heads = int(raw_input('Enter number of heads: '))
	legs = int(raw_input('Enter number of legs: '))
	pigs, chickens = solve(legs, heads)
	if pigs == None:
		print 'There is no solution'
	else:
		print 'Number of pigs: ', pigs
		print 'Number of chickens: ', chickens
		
barnYard()
