# def square_of_num(x):
#     return  (x**2)

# print(square_of_num(4))

# def add(x,y):
#     return x+y
# print(add(5,7))

# def multiply(p1 , p2):
#     return p1 * p2
# print(multiply(3,7))
# print(multiply('abcd',7))

# import math 

# def circle_stats(r):
    
#     area = math.pi*r**2
#     circumference = 2 * math.pi * r
#     return area , circumference
# a , c = circle_stats(3)

# print("Area: ",a,"circumference",c)

# def greet(name = "User"):
#     return "Hello, " + name + " !"
# print(greet("Chai")) 

# cube = lambda x : x ** 3

# print(cube(5))


# def sum_all(*args):

#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)
    
# print(sum_all(1,2,3))
# # print(sum_all(1,2,3,4,5))
# # print(sum_all(1,2,3,4,5,6,7,8))

# def print_kwargs(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key}: {value}")
    
# print_kwargs(name="Shaktimaan", power="Lazer")
# print_kwargs(name="shatimaan")
# print_kwargs(name="Shaktimaan", power="Lazer",enemy="Dr.Jackaal")




# def even_generator(limit):
    
#     for i in range(2, limit + 1,2):
#      yield i
# for num in even_generator(10):
#    print(num) 

# def factorial(n):
#      if n ==0 :
#           return 1
#      else:
#           return n * factorial(n - 1)
     
# num = int(input("enter the number:"))
# print(factorial(num))

