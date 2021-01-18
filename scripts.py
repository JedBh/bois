# print("exercise one\n")
# print("Net4U is the best place\n\t...in the world!")

# print("\nexercise two\n")
# from datetime import datetime

# now = datetime.now()

# currentTime = now.strftime("%H:%M:%S")
# print(currentTime)


# print("\nexercise three\n")
# firstName = input("Please enter your first name: ")
# lastName = input("Please enter your last name: ")
# print(lastName + " " + firstName)

# print("\nexercise four\n")
# fileName = input("Enter file name: ")
# extension = fileName.split(".")
# print(extension[-1])

# print("\nexercise five\n")
# num = input("Please enter a single digit: ")
# newNum = int(num) + int(num * 2) + int(num * 3)
# print(newNum)

# print("\nexercise six\n")
# num = input("Enter a number: ")
# condition = int(num) % 2
# if condition == 0:
#     print("number is even")
# else:
#     print("number is odd")

# print("\nexercise seven\n")
# height = input("How tall are you in feet: ")
# height = height.split("'")
# feet = int(height[0])
# inches = int(height[1])
# cm = feet * 30.48 + inches * 2.54
# print(str(cm))

# print("\nexercise eight\n")
# var = 20
# print(var)
# var = 0
# print(var)

# print("\nexercise nine\n")
# SampleDictionary = {0: 10, 1: 20}
# SampleDictionary.update({2 : 30})
# print(SampleDictionary)

# print("\nexercise ten\n")
# dicit = {}
# string = input("Enter one string: ")
# string = list(string)
# print(string)
# for char in string:
#     dicit.update({char : 1})
# print(dicit)

# print("\nexercise eleven\n")
# str1 = "hello"
# str2 = "yoo"
# reStr = str1 + " " + str2
# print(reStr)

# print("\nexercise twelve\n")
# dicit = {}
# string = "thequickbrownfoxjumpsoverthelazydog"
# for char in string:
#     if char in dicit:
#         dicit[char] += 1
#     else:
#         dicit.update({char : 1})
    
# print(dicit)

# print("\nexercise thirteen\n")
# list = [1, 2, 3]
# total = 0
# for num in list:
#     total += num

# print(total)

# print("\nexercise fourteen\n")
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list1.pop(5)
# list1.pop(4)
# list1.pop(0)
# print(list1)

# Create a file
# fileName = "test.txt"
# f = open(fileName, "w+")
# print(f.read())
# f.close()

# # Read a file
# fileName = "test.txt"
# f = open(fileName, "r")
# print(f.read())
# f.close()

# # Write to a file
# f = open(fileName, "w")
# f.write("192.168.14.1\n192.168.14.103")
# f.close()

# f = open(fileName, "a")
# f.write("Something else")
# f.close()

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp"
#       "above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,"
#       "\n\tHow I wonder what you are")

# from datetime import date
# fDate = date(2021, 1, 17)
# lDate = date(2020, 8, 5)
# diffDate = fDate - lDate
# print(diffDate)

# def nana(num1, num2, num3):
#     if (num1 == num2 == num3):
#         total = num1 + num2 + num3
#         return total * 3
#     else:
#         return num1 + num2 + num3

# print(nana(1,1,2))

# def baba(num1, num2):
#     summ = num1 + num2
#     if (summ >= 15 and summ <= 20):
#         return 20
#     else:
#         return num1 + num2

# print(baba(10,0))

# print("name :   Jed")
# print("age  :   21")
# print("email:   jbenhod@gmail.com")

# def mathTing(x, y):
#     return (x + y) * (x + y)

# print(mathTing(4, 3))

