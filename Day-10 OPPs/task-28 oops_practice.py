# Class Creation
class Abhi():
    print("Hello World")



# Object Creation
class Abhi():
    def Output(self):
        print("Hello World")

vivo=Abhi()
vivo.Output()



class Abhi():
    a=10 
    def show(self):
        print("this is class")
# obj name=class name()
sai=Abhi()
print(sai.a)
sai.show()





class Abhi():
    a=10 #attribute
    def display(self):
        print(self.a)
    
A1=Abhi()  
A2=Abhi()
A1.display()
A2.display()






class Abhi():
    def __init__(self,a,b,c):
        self.A1=a
        self.B1=b
        self.C1=c
        
    def Output(self):
        print(self.A1, self.B1, self.C1)
p=Abhi(1,2,3)
p.Output()






class Mobiles():
    def __init__(self,Mobile_name,Mobile_Ram,Mobile_battery,Mobile_Price):
        self.a=Mobile_name
        self.c=Mobile_Ram
        self.d=Mobile_battery
        self.e=Mobile_Price

    def Mobile_Data(self):
        print("Mobile Name:",self.a)
        print("Mobile Ram:",self.c)
        print("Mobile Battery:",self.d)
        print("Mobile Price:",self.e)


name=input("Enter the Mobile Name:")
ram=input("Enter the Mobile Ram:")
bat=input("Enter the Mobile Battery:")
Price=float(input("Enter the Mobile Price:"))

Mobile_obj=Mobiles(name,ram,bat,Price)
Mobile_obj.Mobile_Data()







