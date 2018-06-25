#question1
class animal():
    def attribute(self):
        print("carnivore animal")

class tiger(animal):
    pass

obj=tiger()
obj.attribute()

#question2
#print a.f(),b.()->A,B
#print a.g(),b.g()->A,B

#question3
class Cop():
	def __init__(self,n,a,w,e,z):
		self.name=n
		self.age=a
		self.work=w
		self.exp=e
		self.des=z
	def add(self):
		self.age=self.age+self.exp
		print("after adding %d" %(self.age))
	def display(self):
		print("name of cop is %s age is %d works as a %s experience of %d designation is %s"%(self.name,self.age,self.work,self.exp,self.des))
	def update(self,new_age):
		self.age=new_age

class Mission(Cop):
    def add_mission_details(self):
        if(self.exp>5):
            print("available for mission")
        else:
            print("not available")
            
name=input("enter the name of cop")
age=int(input("enter age of cop"))
work=input("enter work of cop")
exp=int(input("enter experince of cop"))
des=input("enter designation")

x=Mission(name,age,work,exp,des)
x.display()
new_age=int(input("enter new age"))
x.update(new_age)
x.display()
x.add_mission_details()

        
#question 4
class Shape():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        if(self.length==self.breadth):
            print("area of square is %d"%(self.length*self.breadth))
        else:
            print("area of rectangle is %d"%(self.length*self.breadth))
            
            
class Rectangle(Shape):
    pass
     
class Square(Shape):
    pass

ln=int(input("enter first side"))
br=int(input("enter second side"))
x=Rectangle(ln,br)
x.area()

        



