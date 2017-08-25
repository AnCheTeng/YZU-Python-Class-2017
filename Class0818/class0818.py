# # My first while loop
# i = 1
# fac = 1
# while i < 6:
#     fac = fac * i
#     i += 1
#     print("This turn: " + str(fac))
# print("-------------------")
# print("Final answer: " + str(fac))

# def factorial(n):
#     i = 1
#     fac = 1
#     faclist = []
#     totallist = []
#     while i <= n:
#         fac *= i
#         faclist.append(fac)
#         i += 1
#
#     return fac, faclist, "Hello, world!"
#
# result1, resultlist, myvar = factorial(5)
#
# print "Result1: "+str(result1)
# print "Result-List: "+str(resultlist)
# print myvar
# x = 3
# if x > 4:
#     print("X is greater than 4")
# elif x > 2:
#     print("X is less than 4")
#     print("X is also greater than 2")
# else:
#     if x > 0:
#         print("X is less than 2")
#
# print("--------------")
# print("X is: "+str(x))

# for i in range(10):
#     # if i == 5 or i==6:
#     #     break
#     #     # continue
#     print i
#     pass

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(str(i) + ": " + a[i])




# def isPrime(n):
#     if (type(n) != int):
#         print("Error! Input is not int!")
#         return
#     answer = True
#     for i in range(2, n):
#         if n%i == 0:
#             answer = False
#             break
#     return answer
#
# myans = isPrime(37)
# print("37 is a prime number? "+str(myans))
#
# a = 10
# print(a)
# def changeA(n):
#     n = 20
#
# changeA(a)
# print(a)
#
# # -------------------------
#
# mylist = [1,2,3,4,5]
# print(str(mylist))
# def change0(inputList):
#     inputList[0] = 100
# change0(mylist)
# print(str(mylist))

# mylist = [1,2,3,4,5]
# # if you want to copy a list...
# mylist2 = list(mylist)
# # the following will not copy a list!!!
# mylist3 = mylist
#
# print(str(mylist))
# mylist2[0] = 30
# print(str(mylist))
# mylist3[0] = 30
# print(str(mylist))

# import math
# print(math.sqrt(3))

# from math import sqrt
# print(sqrt(3))

# import math
# print(math.log(10, 10))

from random import randint
noise = range(20)
error = []
for i in range(20):
    error.append(randint(1, 10))

f = open('simulation.csv', 'w')
f.write("index, value\n")

for i in range(20):
    f.write(str(noise[i])+","+str(error[i])+"\n")
f.close()







import matplotlib.pyplot as plt
plt.plot(noise, error)
plt.show()

# f = open('simulation.txt', 'r')
# content = f.read()
# print(content)
# f.close()
