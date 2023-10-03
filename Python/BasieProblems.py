# -----Even and odd-----
# num=int(input("Enter a number"))
# if(num%2)==0:
#     print(num,"Even num")
# else:
#     print(num,"odd num")

# -------Positive or negative or zero-------
# num=float(input("Enter a number"))
# if(num>0):
#     print("Positive num")
# elif (num==0):
#     print("zero")
# else:
#     print("negative number")

# ------Factorial -------2
# num=int(input("Enter a num"))
# factorial=1
# if(num<0):
#     print("Factorial does not exit")
# elif(num==0):
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#         print("The factorial of",num,"is",factorial)

# ------Reverse a num-------
# n=int(input("Enter a num"))
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#     print("Reverse",rev)

# ----Palindrome a num----
# n=int(input("enter a num"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
#     if(temp==rev):
#         print("palindrome")
#     else:
#         print("not a palindrome ")


# ----functions in python normal function-------
# def even_odd(x):
#     if(x%2)==0:
#         print(x,"is even")
#     else:
#         print(x,"is odd")
# even_odd(2)

# ---- Lambda function-----
# g=lambda x:x*x*x
# print(g(7))

# li=[5,7,22,97,54,62,77,23,73,61]
# final_list=list(map(lambda x:x*2,li))
# print(final_list)
# filter_list=list(filter(lambda x:(x%2!=0),li))
# print(filter_list)


# -----Creating First Class-------
# class Phone:
#     def make_call(self):
#         print("making calls")
#     def play_game(self):
#         print("Playing games")
# p1=Phone()
# p1.make_call()  
# p1.play_game()


# -----Adding parameters to the class-----
# class Phone:
#     def set_color(self,color):
#         self.color=color
#     def set_cost(self,cost):
#         self.cost=cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost
#     def make_call(self):
#         print("making calls")
#     def play_game(self):
#         print("Playing games")
# p1=Phone()
# p1.set_color("blue")
# p1.set_cost("500000")


# -------creating a constructor------
# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender
#     def employee_details(self):
#         print("name of employee",self.name)
#         print("Age of employee",self.age)
#         print("Salary of employee",self.salary)
#         print("Gender of employee",self.gender)

# e1=Employee("nikhil",20,250000,"male") 
# e1.employee_details()


# -------Inheritance--------

# class Vehicle:
    # def __init__(self,mileage,cost):
    #     self.mileage=mileage
    #     self.cost=cost
    # def show_details(self):
    #     print("I am vehicle")
    #     print("bike mileage",self.mileage)
    #     print("bike cost",self.cost)
# v1=Vehicle(50,50000)
# v1.show_details()

# creating a child class

# class Car(Vehicle):
#     def show_car(self):
#         print("I am a car")
# c1=Car(50,100000000)
# c1.show_details()
# c1.show_car()

# over-riding init method

# class Car(Vehicle):
#     def __init__(self, mileage, cost,tyres,hp):
#         super().__init__(mileage, cost)
#         self.tyres=tyres
#         self.hp=hp
#     def show_car_details(self):
#         print("I am car")
#         print("no of tyres in car", self.tyres)
#         print("horse power of car",self.hp)
# c2=Car(20,1200000,4,6000)
# c2.show_details()
# c2.show_car_details()
    

# ---multi-level inhertance------
class Parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        print("name",self.name)
class child(Parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        print("Age",self.age)
class GrandChild(child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        print("Gender",self.gender)
g1=GrandChild()
g1.assign_name("nikhil")
g1.assign_age(20)
g1.assign_gender("male")

g1.show_name()
g1.show_age()
g1.show_gender()
