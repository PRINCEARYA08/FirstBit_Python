class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def getId(self):
        return self.id
    def setId(self,newId):
        self.id=newId
    
    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname
    
    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal
    
    def __str__(self):
        return f"Id={self.id} NAme={self.name} Sal={self.sal}"
    
    
    
    def calSal(self):
        print("Final Sal of Employee=",self.sal)

class Hr(Employee):
    def __init__(self, id, name, sal,com):
        super().__init__(id, name, sal)
        self.com=com
    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com=ncom
    
    def __str__(self):
        return super().__str__()+f" Com={self.com}"
    
    def calSal(self):
        print(F"Sal of HR= {self.com+self.sal}")
    
class Dev(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.bonus=bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self,nbonus):
        self.bonus=nbonus
    def __str__(self):
        return super().__str__()+f" Bonus={self.bonus}"
    def calSal(self):
        print(f"Sal of Devloper = {self.sal+self.bonus}")
        
# e=Employee(1,"Rahul",234556)
# d=Dev(18,"Virat",747474,1000)
# h=Hr(13,"Haraman",557474,100)
# e.calSal()
# d.calSal()
# h.calSal()

a=10
print(a)
e=Employee(1,"Rahul",234556)
h=Hr(13,"Haraman",557474,100)
d =Dev(18,"Virat",747474,1000)
print(h)
print(d)
