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


class BusyInstructor:
    numOfBusyInstructor = 0

    def __init__(self, name):
        self.name = name
        self.busyTimeSlots = []
        BusyInstructor.numOfBusyInstructor += 1





    def appendBusyTimeSlot(self, day, clock):
        self.busyTimeSlots.append([day, clock])
