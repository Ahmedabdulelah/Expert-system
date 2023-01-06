#Question :#00
"""Write program doing print you are Fullname and department""" 
print('Name:Ahemd abdulelah Abuzied abdulrahim \n Department:computer science \n Third Year (semester 6)')
#############################################################

#Question :#01
"""If we have a string variable named Weather = "Rainfall", 
which of the following will print the substring or all characters before the "f"?"""
Weather = 'Rainfall'
print(Weather[:4])

#############################################################

#Question :#02
"""Fill in the correct Python commands to put “This is fun!” onto the screen 5 times"""
for i in range(0, 5):
    print('This is fun!')

#############################################################
#Question :#03
"""Complete the script by filling in the missing parts. The function receives a name,
then returns a greeting based on whether or not that name is "Mohammed"""
def greeting(name):
    if name == "Mohammed":
        return "Welcome back Mohammed!"
    else:
        return "Hello there, " + name


print(greeting("Mohammed"))
print(greeting("Ahmed"))

#############################################################
#Question#04
"""What’s the output of this code if number equals 10?"""
number = 10
if number > 11: 
    print(0)
elif number != 10:
    print(1)
elif number >= 20 or number < 12:
    print(2)
else:
    print(3)
    #The output is 2

#############################################################

#Question#05
"""If a filesystem has a block size of 4096 bytes,
this means that a file comprised of only one byte will still use 4096 bytes of storage. 
A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, 
can you fill in the gaps in the calculate storage function below,
which calculates the total number of bytes needed to store a file of a given size?"""
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks =  block_size // filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size*2
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192 

#############################################################

#Question#06
"""Fill in the blanks to make the print_prime_factors function 
print all the prime factors of a number.
A prime factor is a number that is prime and divides another without a remainder."""
def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
    # Check if factor is a divisor of number
        if number % factor == 0 :
        # If it is, print it and divide the original number
            print(factor)
            number = number / factor
    else:
        # If it's not, increment the factor by one
        factor += 1
        return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

#############################################################

#Question#07
"""The following code can lead to an infinite loop.
Fix the code so that it can finish successfully for all numbers.
#Note: Try running your function with the number 0 as the input, and see what you get! """
def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
        return False
    

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False  

#############################################################

#Question#08
"""Fill in the empty function so that it returns the sum of all the divisors of a number, 
without including it. 
A divisor is a number that divides into another without a remainder"""
def sum_divisors(n):
    sum = 0
    i = 0
    while i<=n:
        if n % i == 0:
            sum = sum + i
            i+=1
    # Return the sum of all divisors of n, not including n
            return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114 

#############################################################

#Question#09 
"""Suppose that you have a list 10 items long. How
might you move the last three items from the end of the list to the beginning,
keeping them in the same order?"""

List = [1,2,3,4,5,6,7,8,9,10]
List.insert(0,8) 
List.insert(1,9) 
List.insert(2,10) 
List.pop()
List.pop()
List.pop()
print(List)

#############################################################

#Question#10
"""Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]"""
#Because the tuple is immutable