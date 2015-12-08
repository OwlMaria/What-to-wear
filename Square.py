from math import *

a=int (input ())
b=int (input ())
c=int (input ())

l=(b**2)-(4*a*c)

if l<0:
    print ('no roots')
else:
    print ((-b+sqrt(l))/(2*a))
    print ((-b-sqrt(l))/(2*a))
    
