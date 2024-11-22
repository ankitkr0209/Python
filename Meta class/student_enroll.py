

class student:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
    
    def get_roll(self):
        return self.roll 
    def get_name(self):
        return self.name
    
class department:

    def __init__(self, depart):
        self.department = depart
    
    def get(self):
        return self.department
class course:
    def __init__(self,course):
        self.course = course

    def get(self):
        return self.course
    
class enroll_student:

    def __init__(self,name,roll, cour,depart):
        self.stu = student(roll,name)
        self.dept = department(depart)
        self.course = course(cour)
    
    def show(self):
        print("Name = ", self.stu.get_name())
        print("Roll = ",self.stu.get_roll())
        print("Course = " , self.course.get())
        print("Department = ",self.dept.get())

stu1 = enroll_student( "Ankit", 226013 ,"BCA",  "Technical")
stu1.show()
