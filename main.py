class University_Member:
    def __init__(self,name,enrollment_yr,phone=None):
        super().__init__()
        self.name = name
        self.phone = phone
        self.enrollment_year = enrollment_yr
        self.university_name = "Online University of Covid-19"
        self.current_year = 2021

    def __init_subclass__(cls,title):
        cls.title = title
        super().__init_subclass__()

    def introduce(self):
        print("Hello! I am",self.name,". I enrolled in this university in",self.enrollment_year, \
        ". I am so happy to be here. You can always contact me by my phone number:",self.phone)

    def check_relation(self):
        print("This member is tied to university with the title:", self.title)

class Professor(University_Member,title="Professor"):
    def __init__(self, name, enrollment_yr, publications=None, lectures=None ,phone=None):
        self.publications = publications
        self.lectures = lectures
        self.due = -1
        self.items = []
        self.debt = 0
        super().__init__(name, enrollment_yr, phone=phone)

    def show_lectures(self):
        return self.lectures

    def show_publications(self):
        return self.publications

    def add_new_lecture(self,lect):
        self.lectures.append(lect)
        print("Lecture added.")

    def add_new_publication(self,publ):
        self.publications.append(publ)
        print("Publication added.")

class Student(University_Member,title="Student"):
    def __init__(self, name, enrollment_yr, active_courses=None, failed_courses=None, phone=None):
        self.active = active_courses
        self.failed = failed_courses
        self.due = "14 days later"
        self.items = []
        self.debt = 0
        super().__init__(name, enrollment_yr, phone=phone)

    def show_active_courses(self):
        return self.active

    def show_failed_courses(self):
        return self.failed
    
    def add_active_course(self,course):
        self.active.append(course)
        print("Course appended.")

    def add_failing_course(self,course):
        self.failed.append(course)
        print("Course appended.")

class Library_Debt(Professor,Student,title="Student"):
    def add_library_record(self,item,cost,borrow_date):
        self.items.append(item)
        self.debt -= cost
        if str(self.__class__.__base__)=="<class '__main__.Student'>" :
            self.due = borrow_date + " + 14 days"
        else:
            self.due = -1

    def inquire_debt(self):
        print(str(self.debt)+"$")
        return self.debt

    def inquire_debt_due(self):
        print(self.due)
        #print(str(self.__class__.__base__),type(self.__class__.__base__),str(self.__class__.__base__)=="<class '__main__.Student'>")
        return self.due

            
publications = [
    "Turing, Alan (1950) \"Computing Machinery and Intelligence\"",
    "Turing Alan (1936) \"On Computable Numbers, with an Application to the Entscheidungsproblem"
]
professor_lectures = [
    "CS101","CS202","Discrete Math","AI (artificial intelligence)"
]

active_courses = ["CS101","CS202"]
failed_courses = ["Discrete Math", "AI (artificial intelligence)"]

p = Professor("Alan Turing",1940, publications, professor_lectures,199554400)
p.introduce()
p.show_publications

s = Student("Von Neumann",1942,active_courses,failed_courses,phone=None)
s.introduce()
s.show_active_courses()

d = Library_Debt("Dave",2020)
d.introduce()
d.inquire_debt_due()
d.inquire_debt()
d.add_library_record("OOP in Python",2.95,"28.03.2021")
d.inquire_debt()
d.inquire_debt_due()