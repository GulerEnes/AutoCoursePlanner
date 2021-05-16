class Course:
    numberOfCompulsoryCourses = 0
    numberOfElectiveCourses = 0

    def __init__(self, code, name, year, credit, CE, DS, instructor):
        self.code = code
        self.name = name
        self.year = int(year)
        self.credit = int(credit)
        self.CE = CE  # Compulsory - Elective
        self.DS = DS  # Department - Service
        self.instructor = instructor

        if CE == 'C':
            Course.numberOfCompulsoryCourses += 1
        else:
            Course.numberOfElectiveCourses += 1

    def __repr__(self):
        return self.code + "," + self.name + "," + str(self.year) + "," + \
               str(self.credit) + "," + self.CE + "," + self.DS + "," + self.instructor


class ServiceCourse:
    def __init__(self, code, day, clock):
        self.code = code
        self.day = day
        self.clock = clock


class Classroom:
    def __init__(self, className, day, clock, code):
        self.day = day
        self.clock = clock
        self.className = className
        self.code = code

    def __repr__(self):
        return str(self.day) + " " + str(self.clock) + " " + self.className + " " + str(self.code)


class BusyInstructor:
    def __init__(self, name):
        self.name = name
        self.busyTimeSlots = []
        self.availableTimeSlots = {"Monday": ["Morning", "Afternoon"],
                                   "Tuesday": ["Morning", "Afternoon"],
                                   "Wednesday": ["Morning", "Afternoon"],
                                   "Thursday": ["Morning", "Afternoon"],
                                   "Friday": ["Morning", "Afternoon"]}

    def appendBusyTimeSlot(self, day, clock):
        self.busyTimeSlots.append([day, clock])

    def availableTimesCalculator(self, busyInstructors):
        for day, clock in busyInstructors[self.name].busyTimeSlots:
            self.availableTimeSlots[day].remove(clock)
            if len(self.availableTimeSlots[day]) == 0:
                self.availableTimeSlots.pop(day)
