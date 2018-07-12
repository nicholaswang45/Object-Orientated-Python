class SchoolMember:
  members = 0
  def __init__(self,name,age):
    self.name = name
    self.age = age
    SchoolMember.members+=1
  def printMember(self):
    print ("Member =",self.name, "age =",self.age,end=" ")
  @classmethod
  def printMembers(cls):
    print ("There are",cls.members,"members",end=" ")

class Student(SchoolMember):
  students = 0
  def __init__(self,name,age,marks):
    SchoolMember.__init__(self,name,age)
    self.marks = marks
    Student.students = Student.students+1
  def printMember(self):
    SchoolMember.printMember(self)
    print ("Marks = ",self.marks)
  @classmethod
  def printMembers(cls):
    SchoolMember.printMembers()
    print ("and",cls.students,"students")

class Teacher(SchoolMember):
  teachers = 0
  def __init__(self,name,age,salary):
    SchoolMember.__init__(self,name,age)
    self.salary = salary
    Teacher.teachers+=1
  def printMember(self):
    SchoolMember.printMember(self)
    print("Salary:",self.salary)
  @classmethod
  def printMembers(cls):
    SchoolMember.printMembers()
    print ("and {0} teachers".format(cls.teachers))

class Undergrad(Student):
  undergrads = 0
  def __init__(self,name,age,marks,tuition):
    Student.__init__(self,name,age,marks)
    self.marks = marks
    self.tuition = tuition
    Undergrad.undergrads+=1
  def printMember(self):
    SchoolMember.printMember(self)
    print("Marks = {0}, Tuition = {1}".format(self.marks,self.tuition))
  @classmethod
  def printMembers(cls):
    SchoolMember.printMembers()
    print("and {0} undergrads".format(Undergrad.undergrads))

class Gradstudent(Student):
  pass
