p = 491988559103692092263984889813697016406 
generator = 5

A = 232042342203461569340683568996607232345 
B = 76405255723702450233149901853450417505 

m = 12259991521844666821961395299843462461536060465691388049371797540470 

#Solving discrete log
a = 27964968784502267776
b = 6997851773996753703

shared_secret = pow(A,b,m)
print(shared_secret)
