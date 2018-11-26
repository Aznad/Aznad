import statistics

list1 = []
list2 = []
number =int(input("Enter list length: ") )
print ("Enter the numbers: ")

for i in range(number):
    data = int(input())
    list1.append(data)
    x = statistics.mean(list1)
    print ("Mean value: ", x)
    print (" ")

list1 = []
list2 = []
number = int(input("Enter list length: "))
print ("Enter the numbers: ")

for i in range(number):
    data = int(input())
    list1.append(data)
    y = statistics.median(list1)
    print ("Median value is:", y)

list1 = []
list2 = []
number = int(input("Enter list length: "))
print ("Enter the numbers: ")


#MODE program didnot work :(
#for i in range(number):
    #data = int(input())
    #list1.append(data)
    #z = statistics.mode(list1)
   # print("Mode number is: ", z)

#from statistics import mode

#mode ([1,2,3,3,4])