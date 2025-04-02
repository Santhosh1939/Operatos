# # 1)create a programm that takes user input for the name and agr.use fromatted strings(f-strings) to print message welcoming the user and stating their age.StopIteration
# user_name=input("username:")
# age=input("age:")
# result=(user_name,age)
# # print=(result)
# #using f string
# print(f"my name is {user_name} and iam {age} years old")

# Exercise: Write a Python script that defines a dictionary with information
# about a product (e.g., name, price, quantity). Use formatted strings to display
# the information in a readable format.

# item_name= input("item_name:")
# price=input("price:")
# quantity = input("quantity:")
# print(f"The buying item name is {item_name} that item price is rice {price} rs quantity of that item is {quantity}")

# # 3. Create a list called numbers that contains integers from 1 to 10.
# # Check if the number 5 is in the list.
# # Check if the number 15 is not in the list.

# list_1 =[1,2,3,4,5,6,7,8,9,10]
# print(5 in list_1)
# print(15 not in list_1)


# Exercise 1:
# Write a Python program to calculate the area of a rectangle using the given
# formula: area = length * width . Take the values of length and width as inputs from
# the user

# length_1=int(input("length:"))
# width_1=int(input("width:"))
# area=length_1 * width_1
# print(f"length of the rectagle is {length_1} and width of the rectangle is {width_1} we get area of rectagle {area} by using the formula")

# output:
# length:25
# width:15
# length of the rectagle is 25 and width of the rectangle is 15 we get area of rectagle 375 by using the formula

# Exercise 2:
# Write a Python program to demonstrate incrementing and decrementing a variable
# num = int(input("enter num:"))
# # num  += 2
# # print(f"after incrementing with 2 {num}")
# num  -= 2
# print(f"after decrementing with 2 {num}")

# # output :enter num:25
# # after incrementing with 2 27

# # output:
# enter num:25
# after decrementing with 2 23


# Exercise 3:
# Write a Python program to convert temperature from Celsius to Fahrenheit. The
# formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as
# input from the user.

# temp_1c=int(input("enter temperature in celsius:"))
# temp_F=((temp_1c*9/5)+32)
# print(f"The temperature in Fahrenheit {temp_F}")

# output: enter temperature in celsius:15
# The temperature in Fahrenheit 59.0

# Exercise 4:
# Write a Python program to calculate the simple interest given the principal
# amount, rate, and time (in years).

# principal=int(input("enter principal_amount:"))
# time=int(input("time in years:"))
# rate=float(input("enter the ratr of intrest:"))
# simple_intrest=(principal*time*rate/100)
# print(simple_intrest)

# output:
# enter principal_amount:5000
# time in years:2
# enter the ratr of intrest:7
# 700.0

# Exercise 5:
# Write a Python program to concatenate two strings and display the result. The
# strings should be taken as input from the user.

# name_1=input("enter name_1:")
# name_2=input("enter name_2:")
# total_name=(name_1 +""+ name_2)
# print(total_name)

# OUTPUT:
# enter name_1:GOWDA
# enter name_2SANTHOSHKUMAR
# GOWDASANTHOSHKUMAR

# # Exercise 6:
# # Write a Python program to convert a distance from kilometers to miles.

# # distance=int(input("Distance in kilometers:"))
# miles=(distance*0.62137)
# print(f"distance in kilomters is {distance} converted into miles by using formula,converted distance in miles{miles}")

# output:
# Distance in kilometers:5
# distance in kilomters is 5 converted into miles by using formula,converted distance in miles3.1068499999999997