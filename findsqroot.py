
g = 1
x = int(raw_input("""Please enter the number you want to find the square root for:   
"""))

while g*g != x:
	g = g +1
# 	print g
	if g > x:
		print "This program cant find the square root for, %s" % x
		exit()	
else:
	print "The square root of %s is: %s" % (x, g)


# g = 1
# x = int(raw_input("enter the number you want to find the square root for"))
# 
# while g != x:
# 	i = g +1
# 	g = i*g
# 	print g
# else:
# 	print "square root of %s is: %s" % (x, g)