class Student():
    
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
        
    def getRoll(self):
        return self.roll
    def setRoll(self,newRoll):
        self.roll=newRoll
    
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName
    
    def getMarks(self):
        return self.marks
    def setMarks(self,newMarks):
        self.marks=newMarks
    
    def display(self):
        print(f"roll = {self.roll}, name = {self.name}, roll = {self.marks}")
        
e1=Student(1,"Raju",99)
e2=Student(2,"Viraj",80)
e1.display()
e2.display()
e1.setName("Swarup")
e1.display()
print(e1.getName())

