#objects files wilks
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
