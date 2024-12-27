import math

#Smallest Divisible is SD
def smallestDivisible (number):
    final = 1 #assume the SD is by default 1
    for x in range(1,number+1): #loop through n but add 1 to include the n 
        lcm_for_n = final*x #get all the lcm for all n by multiplying them
        gcd = math.gcd(final,x) #get the gcd accourding to n relative to the assumed answer
        final= int(lcm_for_n/gcd) #divide and parse for error handling and retreiving the answer accourding to the equation
        
        
    return final
        
        
if __name__=='__main__':
    n = int(input("Enter the number to get the smallest divisible to n: ")) #Parse the input from string to int
    if n <=0: #Only positve number
        print("Only Positive numbers")
    else: #Print the returned value of the method 
        print(smallestDivisible(n))