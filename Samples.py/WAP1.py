#Write a program that prints the numbers from 1 to 50.

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

# def reversed_number(x):
#   x = str(x)
#   x = reversed(x)
  
#   return x

# n =int(input("enter th number:"))
# print(reversed_number(n))

# age = 22
# day = "Thursday"
# price =12 if age>=18 else 8

# if day == "Wednessday":
#     # price = price - 2
#     price -=2

# print("Ticket price for you id $")

# number = 3
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(number,'x', i , '=', number*i)


# input_str = "Python"
# reversed_str = ""
# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)    

# input_str = "teeterasdasd"
# for char in input_str:
#     print(char)
#     if input_str.count(char)==1:
#         print("Char is: ", char)
#         break


# number = 5
# factorial =1

# while number>0:
#     # factorial = factorial*number
#     # number *= number
#     factorial *=factorial
#     number-= 1

# print("Factorial value of the number is:",factorial)    


# while True:
#     number = int(input("enter the value between 1 and 10"))
#     if 1<= number <=10:
#         print("thanks")
#         break
# else:
#     print("invalid number")



# items = ["apple" , "banana" , "orange" ,"apple" , "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("duplicate:",item) 
        
#     unique_item.add(item)

# print(unique_item)    
# def add_numbers(n):
#     total = 0
#     for i in range(0,n+1):
#         total += i
#     return total 
# print(add_numbers(4))    





# def prime_numbers(starting_range , ending_range):
#   lst = []
#   flag = 0
#   for i in range(starting_range , ending_range):
#     for j in range(2, i):
#       if(i % j == 0):
        
#         flag = 1
#         break
#       else: flag=0
#     if(flag == 0):
#         lst.append(i)

#   return lst
# print(prime_numbers(2,10))  

# def divisibility(num1 , num2):
#     if(num1%num2==0):
#         print(num1 ,"is divisible by", num2)
#     else:
#         print(num1 , "is not divisible by" , num2)
#     return

# def main():
#     num1=int(input("Enyer the number:"))
#     num2=int(input("Enter the second number:"))
#     divisibility(num1, num2)
# main()
