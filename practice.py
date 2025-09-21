# Name = input("Enter Your Name: ")
# print(len(Name))


# string = str("Ra$vin")
# print(string.find("$"))


# num = int(input("Enter Your Number: "))

# if num % 7 == 0:
#     print("Yes")
# else:
#     print("No")


# a = int(input("Enter Your First Number: "))
# b = int(input("Enter Your second Number: "))
# c = int(input("Enter Your Third Number: "))

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)




# movies = []
# N = int(input ("Number of Movies: "))

# for i in range(N):
#     a = input("Enter 1st movie Name: ")
#     movies.append(a)

# print(movies)


# Grade = ("C", "D", "A", "A", "B", "B", "A")
# # st = Grade.count("A")
# # print(st)



# Grade = ("C", "D", "A", "A", "B", "B", "A")
# sortedGrade = []

# for g in Grade:
#     sortedGrade.append(g)

# sortedGrade.sort()
# print(sortedGrade)


# cities = {"Delhi", "Mumbai", "Delhi", "Morena", "Jaipur"}
# print(cities)  # {'Mumbai', 'Delhi', 'Morena', 'Jaipur'}



# for i in range(3,10,3):
#     print(i)



# fruits = ['Apple','banana','grappes','papaya']

# def list(fruits):
#     for fruit in fruits:
#         print(fruit)

# list(fruits)



# def factorial(n):
#     fact = 1
#     i = 1
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)

# Num = int(input("which Number's factorial: "))
# factorial(Num)



# Recursion
# def sum(n):
#     if n == 0:
#         return
#     print(n)
#     sum(n-1)
# sum(5)


# def cal(n):
#     if n == 0:
#         return
#      = n + (n-1)
# print(sum)
# cal(5)


# def cal(n):
#     if n == 0:
#         return 0
#     return n + cal(n - 1)

# # To print the sum of numbers from 1 to 5
# print(cal(5))


# list = [4,6,12,56,78,32,23]

# def allprint(n):
#     if n == len(list):
#         return
#     print(list[n])
#     allprint(n+1)

# allprint(0)



# f = open("Greet.txt","r")

# data = f.update("My name is ravin")
# print(data)



# f = open("Greet.txt", "w")  # write mode
# f.write("My name is ravin")
# print("Succes")
# f.close()



# f = open("love.txt", "w")
# data = f.write("Love is Life")
# f.close()


# with open("Greet.txt","r") as f:
#     data = f.read()

#     print(data)



# import os
# os.remove("Greet.txt")


# practice
# with open("practice.txt", "w") as f:
#     data = f.write("Hi everyon \nwe are learning file I/O \nUsing java. \nI like programing in java")
#     print(data)


# with open("practice.txt", "r") as f:
#     data = f.read() 

# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# if(data.find("learning") != -1):
#     print("Found")
# else:
#     print("not found")



# a = int(input("Enter your first Number: "))
# b = int(input("Enter your second Number: "))

# ....................
# temp = a
# a = b
# b = temp
# ......................

# a,b = b,a

# ........................

# print(f'a = {a}, b = {b}')



# add = a+b
# sub = 0
# mult = 1
# div = 0
# intdiv = 0
# mod = 0
# if a > b:
#     sub = a-b
#     div = a/b
#     intdiv = a//b
#     mod = a%b
# else:
#     sub = b-a
#     div = b/a
#     intdiv = b//a
#     mod = b%a

# mult = a*b

# print(add,sub,mult,div,intdiv,mod)


# quot = a//b
# rem = a%b

# print(quot,rem)


# lastdigit = a%10
# print(lastdigit)


# F = 9*a/5 + 32
# print(F)


# largest = a//b*b
# print(largest)

# if a>b:
#     print(a)
# else:
#     print(b)

# if a%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# if a < 0:
#     print("Negative")
# elif a > 0:
#     print("positive")
# else:
#     print("Zero")


# if a % 2 == 0:
#     print(a)
# else:
#     print(a*2)




# a = int(input("Enter your first Number: "))
# b = int(input("Enter your second Number: "))
# c = int(input("Enter your third Number: "))
# d = int(input("Enter Your forth Number: "))

# if a > b and a > c and a > d:
#     print(a)
# elif b > a and b > c and b > d:
#     print(b)
# elif c > a and c > b and c > d:
#     print(c)
# else: 
#     print(d)



# class Student():
#     name = "Karan"

# s1 = Student()
# print(s1.name)
 

# s2 = Student()
# print(s2.name)



# class Student():
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student('karan',89)
# print(s1.name, s1.marks)


# a = int(input("Enter Year: "))

# if a % 100 == 0:
#     if a % 400 == 0:
#         print("Leap Year")
#     else:
#         print("Odd Year")
# elif a % 4 == 0:
#     print("Leap Year")
# else:
#     print("Odd Year")



# a = int(input("Enter your first Number: "))
# b = int(input("Enter your second Number: "))
# c = int(input("Enter your third Number: "))


# if (a<b and a>c) or (a>b and a<c):
#     print("Second Max is: ",a)
# elif (b>a and b<c) or (b>c and b<a):
#     print("Second max is: ",b)
# else:
#     print("Second max is: ",c)



# a = int(input("Enter Bisic Salary: "))
# hra = 0
# da = 0
# if a <= 10000:
#     hra = a*20/100
#     da = a*80/100
#     print(a+hra+da)
# elif a <= 20000:
#     hra = a*25/100
#     da = a*90/100
#     print(a+hra+da)
# else:
#     hra = a*30/100
#     da = a*95/100
#     print(a+hra+da)


# units = int(input("Enter Total Electricity Unit: "))
# bill = 0

# if units <= 50:
#     bill = units*0.50
# elif units <= 150:
#     bill = 50*0.50 + (units-50)*0.75
# elif units <= 250:
#     bill = 50*0.50 + 100*0.75 + (units-150)*1.20
# else:
#     bill = 50*0.50 + 100*0.75 + 100*1.20 + (units-250)*1.50

# surcharge = bill*0.20
# total_bill = bill + surcharge
# print(total_bill)



# if(a>b and a<c and a<d) or (a>c and a<b and a<d) or (a>d and a<c and a<b):
#     print("Third max is: ",a)
# elif(b>a and b<c and b<d) or (b>c and b<a and b<d) or (b>d and b<a and b<c):
#     print("third max is: ",b)
# elif(c>a and c<b and c<d) or (c>b and c<a and c<d) or (c>d and c<b and c<a):
#     print("Third max is: ",c)
# else: 
#     print(d)



# a = int(input("Enter your first Number: "))
# name = input("Enter your second Number: ")

# for i in range(a):
#     print(name)
#     i += 1



# a = int(input("Enter your first Number: "))

# count = 0
# for i in range(1,a):
#     if a % i == 0:
#         count += i

# if count == a:
#     print('perfect number')
# else:
#     print("Not Perfect")


# num = int(input("Enter your first Number: "))
# a = num
# new_num = 0

# while num != 0:
#     d = num % 10
#     new_num = new_num*10 + d
#     num = num // 10

# if a == new_num:
#     print("This is a Palindrome Number")
# else:
#     print("Not Palindrome")



# num = int(input("Enter your first Number: "))
# squre = 1
# for i in range(1,num//4+1):
#     squre = i*i*i
#     if squre == num:
#         print("Perfect Cube")
#         break
# else:
#     print("Not perfect Cube")



# num = int(input("Enter The Number: "))
# sum = 0
# for i in range(1,num+1):
#     if i%2 == 1:
#         sum += i

# print(sum)


# m = int(input("Enter start Number: "))
# n = int (input("Enter end Number: "))
# sum = 0
# for i in range(m,n+1):
#     sum += i
# print(sum)



# sum = 0
# for i in range(1,n+1):
#     sum += 1/i
# print(sum)


# num = int(input("Enter Number: "))
# digits = len(str(num))
# print(digits)


# sum=0
# while num != 0:
#     d = num%10
#     sum += d
#     num = num // 10
# print(sum)


# num = int(input("Enter The Number: "))
# reverse = 0
# while num != 0:
#     d = num % 10
#     reverse = reverse*10+d
#     num = num // 10
# print(reversed(num))


# num = int(input("Enter Number"))  


# n = int(input("Enter The Number: "))
# count = 0
# for i in range(1,n):
#     if n % i == 0:
#         count += i

# if count == n:
#     print("Perfect Number")
# else:
#     print("not")



# n = int(input("Enter length of an erray: "))
# allprint = []
# for i in range(n):
#     num = int(input(f'Enter {i+1} Number: '))
#     allprint.append(num)

# for i in range(len(allprint)):
#     print(allprint[i])



# num = int(input("Enter Till Number: "))
# ntrnum = []
# for i in range(1,num+1):
#     n = i
#     ntrnum.append(n)

# print(ntrnum)


# n = int(input("Enter length: "))
# reverse = []

# for i in range(n):
#     num = int(input(f"Enter {i+1} Number: "))
#     reverse.append(num)

# for i in range(len(reverse)-1,-1,-1 ):
#     print(reverse[i])



# s = int(input("Enter Size of Array: "))
# list = []
# oddsum = 0
# evensum = 0
# for i in range(s):
#     n = int(input(f"Enter {i+1} Number: "))
#     list.append(n)

# for i in range(len(list)):
#     if list[i] % 2 == 0:
#         evensum += list[i]
#     else:
#         oddsum += list[i]
    
# print(f"Sum of Odd Numbers = {oddsum}")
# print(f"Sum of even Numbers = {evensum}")



# s = int(input("Enter Size of Array: "))
# list = []
# duplicates = []
# for i in range(s):
#     n = int(input(f"Enter {i+1} Number: "))
#     list.append(n)

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i] == list[j] and list[i] not in duplicates:
#             duplicates.append(list[i])
# print(duplicates)



# n = int(input("Enter Size of list: "))
# num = []

# for i in (n):




# OOP(Object Oriented Programming language)

#  create class
# class Student:
#     name = "Ravin"

#  create Objects
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)



#topic => With init function (Constructor method)
# class Car():
#     def __init__(self, color, brand):
#         self.rang = color 
#         self.brand = brand       


# bolero_new = Car('Red', "Mahindra")
# print(bolero_new.rang)
# print(bolero_new.brand)


#topic => Types of Constructor => 1. Default 2.Parameterized

#topic => Class & Instans(Obj.) Attributes
# class Student():
#     collage_name = 'ABC-Collage'
#     name = "Raju"
#     def __init__(self, name, marks):
#         self.name = name  
#         self.marks = marks


# Ravin = Student("Ravin", 95)
# print(Ravin.name, Ravin.marks, Ravin.collage_name)



#practice Question
# class Student():
#     def __init__(self, name, hindi, english, math):
#         self.name = name
#         self.hindi = hindi
#         self.english = english
#         self.math = math

#     def average(self):
#         print((self.hindi + self.english + self.math)/3)


# s1 = Student("Ravin", 89, 76, 99)
# print(s1.name, s1.hindi, s1.english, s1.math)
# s1.average()



#Topic => methods => Static and Non-static methods

# class Student():
#     @staticmethod
#     def collage():
#         print('ABC-Collage')

#     def __init__(self, name, marks):
#         self.name = name  
#         self.marks = marks

# s1 = Student("Ravin", 78)
# print(s1.name, s1.marks)
# s1.collage()



# Practice Quesion 
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account = acc


# user_1 = Account(100, 12345678)
# print(user_1.balance, user_1.account)



#reverse string, output in list
# A = "HELLO"
# B = []

# for i in range(len(A)-1,-1,-1):
#     B.append(A[i])
# print(B)



# check palindrom in string
# a = input("Enter Your Text: ")
# count = 0

# for i in range(len(a)//2):
#     if a[i] == a[-(i+1)]:
#         count += 1

# if count == len(a)//2:
#     print("YES")
# else:
#     print("NO")



# Print Duplicate character
# s = input("Write Your Word: ")
# already_checked = []

# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1
#     if count > 1 and s[i] not in already_checked:
#         print("Duplicate character:", s[i])
#         already_checked.append(s[i])



#return string number of Times
# s = input("Enter Your string: ")
# n = int(input("Enter Number of times: "))
# string = ""

# for i in range(n):
#     string += s

# print(string)
 




# a = 5
# b = 9
# print("A") if a>b else print("B")


# a = 332
# b = 330
# print("A") if a>b else print("=") if a == b else print("B")




# Cake Making 

# a, b = map(int, input().split())

# if a>b:
#     print((a-1)*b)
# elif a==b:
#     print((a-1)*b)
# else:
#     print((b-1)*a)


# Brick Comparision

# t = int(input())
# for i in range(t):
#     n = int(input())
#     A = list(map(int, input().split()))
    
#     current_index = 0  
#     for i in range(1, n):
#         if A[i] > A[current_index]:
#             current_index = i 
    
#     print(current_index + 1)



# -----------------------------------------learning------------------------------------------------------

# Arbitrary Arguments
# def student(*num):
#         add = sum(num) 
#         print(add)

# student(9,6,85)



# Arbitrary Keyword Arguments
def Student_info (**data):
    for key,value in data.items():
        print(f"{key}: {value}")


Student_info(Name = "Ravin", Age = "22", City = "Gwalior")