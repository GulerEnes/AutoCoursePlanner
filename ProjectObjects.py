class Classroom:
    numOfClassroom = 0
    bigClassAmount = 0
    smallClassAmount = 0

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        Classroom.numOfClassroom += int(self.amount)

    def __repr__(self):
            return f"""type: {self.type}
amount: {self.amount}
-------------------------------------------------
"""

class Course:
    numOfCourses = 0

    def __init__(self, code, name, year, credit, CE, DS, instructor):
        self.code = code
        self.name = name
        self.year = year
        self.credit = credit
        self.CE = CE
        self.DS = DS
        self.instructor = instructor
        self.serviceTimeSlot_day = None
        self.serviceTimeSlot_clock = None
        Course.numOfCourses += 1

    def __repr__(self):  # I wrote this for temporarily
        return f"""code: {self.code}
name: {self.name}
year: {self.year}
credit: {self.credit}
CE: {self.CE}
DS: {self.DS}
instructor: {self.instructor}
serviceTimeSlot_day: {self.serviceTimeSlot_day}
serviceTimeSlot_clock: {self.serviceTimeSlot_clock}
-------------------------------------------------
"""


class ServiceCourse:
    numOfServiceCourses = 0

    def __init__(self, code, day, clock):
        self.code = code
        self.day = day
        self.clock = clock
        ServiceCourse.numOfServiceCourses += 1

    def __repr__(self):
            return f"""code: {self.code}
day: {self.day}
clock: {self.clock}
-------------------------------------------------
"""


class BusyInstructor:
    numOfBusyInstructor = 0

    def __init__(self, name):
        self.name = name
        self.busyTimeSlots = []
        BusyInstructor.numOfBusyInstructor += 1

    def appendBusyTimeSlot(self, day, clock):
        self.busyTimeSlots.append([day, clock])
    def __repr__(self):
            return f"""name: {self.name}
BusyTimeSlots: {self.busyTimeSlots}
-------------------------------------------------
"""

class Cirriculum:

    def __init__(self,day,clock,classroom,code):
        self.day = day
        self.clock = clock
        self.classroom = classroom
        self.code = code

    def __repr__(self):
            return f"""Day: {self.day}
Clock: {self.clock}
Classrom: {self.classroom}
Code: {self.code}            
-------------------------------------------------
"""