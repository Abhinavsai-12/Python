
# class Parent:
#     def output(self):
#          print('this is parent class')
# class Child(Parent):
#     def outputChild(self): # output
#         print('this is child class')
# i=Child()
# i.output()
# i.outputChild()






# class Father:
#     def output(self):
#         print('this is parent class')
# class Mother:
#     def outputM(self):
#         print('this is mother class')
# class Child(Father,Mother):
#     def outputChild(self):
#         print('this is child class')      
# ice=Child()
# ice.output()
# ice.outputM()
# ice.outputChild()



# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
#     def outputChild(self):
#         print('this is child class')      
# ice=Child()
# ice.output()
# ice.outputf()
# ice.outputChild()






# class Father:#100cr
#     def output(self):
#         print('this is father class')
# class Child1(Father):#50cr
#     def outputf(self):
#         print('this is child 1 class')
# class Child2(Father):#50cr
#     def outputChild(self):
#         print('this is child  2 class')      
# ice=Child1()
# cream=Child2()
# ice.output() #child 1 of parent
# ice.outputf()
# cream.output() # child 2 of parent
# cream.outputChild() # child 2







# Polymorphism
# poly-many
# morph = forms
# 1.method overloading 
# 2.method overridding




# class Methodoverlod:
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=Methodoverlod()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()




# class Methodoverri:
#     def display(self):
#         print("this is parent class")

# class Child(Methodoverri):
#     def display(self):
#         print("this is child class")
#         super().display() 
               
# obj=Child()
# obj.display()






#encapsulation

# binding of class (methods and variables(attributes))
# # public 
# # and 
# # private __
# # protected _



# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)

# print(account.get_balance())





# class GFather:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class Father(GFather):
#     def display1(self):
#         print(self._y)
# class Child2(Father):
#     def display2(self):
#         print("child2",self._y)
# obj=Child2(12)
# obj.display2()
# obj.display1()



# a=10
# def func():
#     b=20
#     print('this is fun',b,a)
# func()

# print(a)




# from abc import ABC, abstractmethod   
# class Car(ABC): 
#     @abstractmethod  
#     def mileage(self):   
#         pass  
# class Tesla(Car):   
#     def mileage(self):   
#         print("The mileage is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):   
#           print("The mileage is 24kmph ")   
# class Renault(Car):   
#     def mileage(self):   
#             print("The mileage is 27kmph ")           
# # Driver code

# t= Tesla ()   
# t.mileage()   
# r = Renault()   
# r.mileage()    
# s = Suzuki()   
# s.mileage()   
# d = Duster()   
# d.mileage()  

