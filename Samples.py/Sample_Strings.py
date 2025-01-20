# def reversed_string(str):
#     return str[::-1]
# str = str(input("Enter the string:"))
# if(str==reversed_string(str)):
#     print("yes")
# else:
#     print("no")  
# 
# 
# tea_varities = ["Black" , "Green" , "Oolong" , "White"]   
# 
# for tea in tea_varities:
# ...  print(tea)
# ...
# Black
# Green
# Oolong
# White
# for tea in tea_varities:
# ...  print(tea , end="-")
# ...
# Black-Green-Oolong-White

# if "Oolong" in tea_varities:
# ... print(" I have Oolong tea")  
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities.append("Lemon")
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White', 'Lemon']
# >>> if "Lemon" in tea_varities:  
# ...  print(" I have Lemon tea")  
# ...
#  I have Lemon tea
# >>> tea_varities.pop()
# 'Lemon'
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities.remove("green")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>> tea_varities.remove("Green") 
# >>> tea_varities       
# ['Black', 'Oolong', 'White']
# tea_varities.insert(
# ... 1,"Green")
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities_copy = tea_varities.copy()
# >>> tea_varities_copy
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities_copy.append("Lemon")
# >>> tea_varities_copy
# ['Black', 'Green', 'Oolong', 'White', 'Lemon']
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> squared_nums = [x**2 for x in range(10)]
# 
# # >>> squared_nums
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 


# def sub_string(main_str,sub_str):
#     if sub_str in main_str:
#         print(sub_str)
#     else:
#         print("sub string not found")

#     return sub_str

# def main():
#     main_str = str(input("enter the string:"))
#     sub_str = str(input("enter the string:"))
#     sub_string(main_str,sub_str)
# main()


        
        