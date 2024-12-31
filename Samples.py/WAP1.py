# ## Write a program that prints the numbers from 1 to 50.

# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz"

# print("The numbers from 1 to 50 are ")
# for i in range(51):

#     print(i , end=' \n')

# n = int(input("Enter the number: "))
# if(n%3==0 and n%5==0): 
#    print("FizzBuzz")
# elif(n%3==0):
#    print("Buzz")
# elif(n%5==0):
#    print("Fizz")

# def  prime_number_checker(n):
#     if(2%n==0):
#         print("It is a prime number.")
#     else:
#         print("It is not a prime number.")
#     return 
# n = int(input("Enter the number:"))

# print(prime_number_checker(n))


# def factorial(x):
#     if( x==0 or x==1):
#         return 1
#     else:
#         return (x*factorial(x-1))

# num=7
# result = factorial(num)
# num = int(input("enter the number"))
# print(factorial(num)) 


# def palindrome(s):
#     rev = s[::-1]
#     if(s == rev):
#      print("yes")
#     else:
#      print("no") 
#     return s
# string = str(input("enter the string"))
# print(palindrome(string))    

# def prime_numbers(x):
#     for x in range(0,x+1):
#         if(x>1):
#             for i in range(2,int(x**0.5)+1): 
#               if(x%i==0):
#                 break
#               else:
#                print(x)

# num = int(input("enter the number:"))

# print(prime_numbers(num))

def reversed_number(x):
  
  return x

n =int(input("enter th number:"))
print(reversed_number(n))
