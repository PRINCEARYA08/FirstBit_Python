class Student:
    iName = "FBS"
   
    def __init__(self, frn, name, batch):
        self.frn = frn
        self.name = name
        self.batch = batch
      

    def getFRN(self):
        return self.frn

    def setFRN(self, nfrn):
        self.frn = nfrn

    def getName(self):
        return self.name

    def setName(self, nName):
        self.name = nName

    def getBatch(self):
        return self.batch

    def setBatch(self, nBatch):
        self.batch = nBatch

    def getIName(self):
        return self.iName

    def setIName(self, nIName):
        self.iName = nIName
 
    @staticmethod
    def login(self):
        print("Login to the system")
            
    def display(self):
        print(f"FRN={self.frn} Name={self.name} Batch={self.batch} IName={Student.iName}")

    def __del(self):
        print(f"Destructor called for {self.name}")
        print(self.name)
        self.name=None
        self.frn=None
        self.batch=None
        self.iName=None
        print(self.name)
    
    
s1 = Student(12, "Sudhir", "Aug Python")
s2 = Student(13, "Ram", "Sep Python")
s3 = Student(14, "Sham", "July Python")

#1
# s1.display()
# # s1.setName("Sudhir Kumar")

# s2.display()
# s3.display()

# s1.setName("Sudhir Kumar")
# s1.display()

 
 
#2
# print(s1.iName)
print(Student.iName)
Student.iName = "FirstBit Solutions"
print(Student.iName)


#3
# def change(newval):
#     a=10
#     print(a)
#     a=newval
#     print(a)
# change(45)


#4
#Student.login()
s1.login()