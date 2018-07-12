from student import *

def main():
	
	myList = []
	n = eval(input("How many people: "))
	for i in range(n):
		myList.append(SchoolMember("Nick",4))
	for i in range(n):
		myList.append(Student("Patrick",3, 99))
	for i in range(n):
		myList.append(Teacher("Jonas",8,95000))
	for i in range(n):
		myList.append(Undergrad("Melvin",8,93,35000))

	for person in myList:
		person.printMember()
	Student.printMembers()
	Undergrad.printMembers()

	input()

main()