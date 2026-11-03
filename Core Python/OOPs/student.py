class Student:
    def __init__(self, frn, name, batch, iName):
        self.frn = frn
        self.name = name
        self.batch = batch
        self.iName = iName

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

    def display(self):
        print(f"FRN={self.frn} Name={self.name} Batch={self.batch} IName={self.iName}")


s1 = Student(12, "Sudhir", "Aug Python", "FBS")
s2 = Student(13, "Ram", "Sep Python", "FBS")
s3 = Student(14, "Sham", "July Python", "FBS")

s1.display()
s2.display()
s3.display()