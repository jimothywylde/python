#objects file
class Person:
    def __init__(self, id, fname, lname, sex, gender, ssn, dob, email):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.gender = gender
        self.ssn = ssn
        self.dob = dob
        self.email = email
    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, id, fname, lname, sex, gender, ssn, dob, email, major, residenceHall, year, isEnrolled):
        super().__init__(id, fname, lname, sex, gender, ssn, dob, email)
        self.major = major
        self.residenceHall = residenceHall
        self.year = year
        self.isEnrolled = isEnrolled

    global students
    students = []

    def countStudents():
        global enrolledStudents
        enrolledStudents = 0
        for x in students:
            if x.isEnrolled == True:
                enrolledStudents +=1
        print("The number of enrolled students is:", enrolledStudents)

class Faculty(Person):
    def __init__(self, id, fname, lname, sex, gender, ssn, dob, email, department, hireDate, hireYear):
        super().__init__(id, fname, lname, sex, gender, ssn, dob, email)
        self.department = department
        self.hireDate = hireDate
        self.hireYear = hireYear

    global faculty
    faculty = []

    def yearsOfService():
        global currentYear
        currentYear = 2019
        for x in faculty:
            serviceYears = currentYear - x.hireYear
            print(x.fname, x.lname, "has worked here for", serviceYears, "years.")

#people file
#import objects
student0 = Student(0, "Alex", "Adams", "M", "M", "ssn", "dob", "alexadams@gmail.com", "Algebra", "Hall 1", "Freshman", True)
students.append(student0)
student1 = Student(1, "Becky", "Bennet", "F", "F", "ssn", "dob", "beckybennet@gmail.com", "Braille", "Hall 2", "Sophomore", True)
students.append(student1)
student2 = Student(2, "Caleb", "Castor", "M", "M", "ssn", "dob", "calebcastor@gmail.com", "Counting Numbers", "Hall 1", "Sophomore", True)
students.append(student2)
student3 = Student(3, "Derrick", "Delorean", "M", "M", "ssn", "dob", "xbox_s1ay3r@hotmail.com", "Digital Arts", "Hall 2", "Junior", True)
students.append(student3)
student4 = Student(4, "Edith", "Edwards", "F", "T", "ssn", "dob", "edithedwards@gmail.com", "Ecomonics", "Hall 2", "Freshman", True)
students.append(student4)
student5 = Student(5, "Frank", "Foster", "M", "M", "ssn", "dob", "frankfoster@gmail.com", "Freakanomics", "Hall 1", "Senior", True)
students.append(student5)
student6 = Student(6, "Greg", "Gergich", "M", "T", "ssn", "dob", "greggergich@gmail.com", "Geometry", "Hall 1", "Sophomore", True)
students.append(student6)
student7 = Student(7, "Hogarth", "Hughles", "M", "M", "ssn", "dob", "hogarthhughles@gmail.com", "Husbandry, Animals", "Hall 1", "Senior", True)
students.append(student7)
student8 = Student(8, "Isabelle", "Ignacio", "F", "F", "ssn", "dob", "isabelleignacio@gmail.com", "Iambic Pentameter", "Hall 2", "Junior", True)
students.append(student8)
student9 = Student(9, "John", "Jackson", "M", "M", "ssn", "dob", "johnjackson@gmail.com", "Journalism", "Hall 1", "Freshman", False)
students.append(student9)
#faculty list
faculty0 = Faculty(0, "Alan", "Adamson", "M", "M", "ssn", "dob", "aadamson@gmail.com", "Agricultural Sciences", "hiredate", 2000)
faculty.append(faculty0)
faculty1 = Faculty(1, "Boison", "Bojangles", "?", "?", "ssn", "dob", "bojanglesbojanglesbojangles@gmail.com", "Bojanglin'", "hiredate", 2001)
faculty.append(faculty1)
faculty2 = Faculty(2, "Carmen", "Carter", "F", "F", "ssn", "dob", "ccarter@gmail.com", "Communication", "hiredate", 2002)
faculty.append(faculty2)
faculty3 = Faculty(3, "Deadra", "Dunhill", "F", "F", "ssn", "dob", "ddunhill@gmail.com", "Departmentology", "hiredate", 2003)
faculty.append(faculty3)
faculty4 = Faculty(4, "Eric", "Everyman", "M", "M", "ssn", "dob", "everymanemail@email.com", "Every Dept", "hiredate", 2004)
faculty.append(faculty4)

#number of students
Student.countStudents()
#faculty years of service
Faculty.yearsOfService()