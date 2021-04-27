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


class ServiceCourse:
    numOfServiceCourses = 0

    def __init__(self, code, day, clock):
        self.code = code
        self.day = day
        self.clock = clock


class BusyInstructor:
    numOfBusyInstructor = 0

    def __init__(self, name):
        self.name = name
        self.busyTimeSlots = dict()

    def appendBusyTimeSlot(self, day, clock):
        self.busyTimeSlots[day] = clock
