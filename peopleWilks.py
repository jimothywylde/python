#people file
import objectsW
student0 = objectsWilks.Student(0, "Alex", "Adams", "M", "M", "ssn", "dob", "alexadams@gmail.com", "Algebra", "Hall 1", "Freshman", True)
objectsWilks.students.append(student0)
student1 = objectsWilks.Student(1, "Becky", "Bennet", "F", "F", "ssn", "dob", "beckybennet@gmail.com", "Braille", "Hall 2", "Sophomore", True)
objectsWilks.students.append(student1)
student2 = objectsWilks.Student(2, "Caleb", "Castor", "M", "M", "ssn", "dob", "calebcastor@gmail.com", "Counting Numbers", "Hall 1", "Sophomore", True)
objectsWilks.students.append(student2)
student3 = objectsWilks.Student(3, "Derrick", "Delorean", "M", "M", "ssn", "dob", "xbox_s1ay3r@hotmail.com", "Digital Arts", "Hall 2", "Junior", True)
objectsWilks.students.append(student3)
student4 = objectsWilks.Student(4, "Edith", "Edwards", "F", "T", "ssn", "dob", "edithedwards@gmail.com", "Ecomonics", "Hall 2", "Freshman", True)
objectsWilks.students.append(student4)
student5 = objectsWilks.Student(5, "Frank", "Foster", "M", "M", "ssn", "dob", "frankfoster@gmail.com", "Freakanomics", "Hall 1", "Senior", True)
objectsWilks.students.append(student5)
student6 = objectsWilks.Student(6, "Greg", "Gergich", "M", "T", "ssn", "dob", "greggergich@gmail.com", "Geometry", "Hall 1", "Sophomore", True)
objectsWilks.students.append(student6)
student7 = objectsWilks.Student(7, "Hogarth", "Hughles", "M", "M", "ssn", "dob", "hogarthhughles@gmail.com", "Husbandry, Animals", "Hall 1", "Senior", True)
objectsWilks.students.append(student7)
student8 = objectsWilks.Student(8, "Isabelle", "Ignacio", "F", "F", "ssn", "dob", "isabelleignacio@gmail.com", "Iambic Pentameter", "Hall 2", "Junior", True)
objectsWilks.students.append(student8)
student9 = objectsWilks.Student(9, "John", "Jackson", "M", "M", "ssn", "dob", "johnjackson@gmail.com", "Journalism", "Hall 1", "Freshman", False)
objectsWilks.students.append(student9)
#faculty list
faculty0 = objectsWilks.Faculty(0, "Alan", "Adamson", "M", "M", "ssn", "dob", "aadamson@gmail.com", "Agricultural Sciences", "hiredate", 2000)
objectsWilks.faculty.append(faculty0)
faculty1 = objectsWilks.Faculty(1, "Boison", "Bojangles", "?", "?", "ssn", "dob", "bojanglesbojanglesbojangles@gmail.com", "Bojanglin'", "hiredate", 2001)
objectsWilks.faculty.append(faculty1)
faculty2 = objectsWilks.Faculty(2, "Carmen", "Carter", "F", "F", "ssn", "dob", "ccarter@gmail.com", "Communication", "hiredate", 2002)
objectsWilks.faculty.append(faculty2)
faculty3 = objectsWilks.Faculty(3, "Deadra", "Dunhill", "F", "F", "ssn", "dob", "ddunhill@gmail.com", "Departmentology", "hiredate", 2003)
objectsWilks.faculty.append(faculty3)
faculty4 = objectsWilks.Faculty(4, "Eric", "Everyman", "M", "M", "ssn", "dob", "everymanemail@email.com", "Every Dept", "hiredate", 2004)
objectsWilks.faculty.append(faculty4)


#number of students
objectsWilks.Student.countStudents()
#faculty years of service
objectsWilks.Faculty.yearsOfService()