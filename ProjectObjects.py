import csv
import random


class Main:

    # Creating available place holder for classrooms.
    def timeGenerator(self):
        return {"Monday": ["Morning", "Afternoon"],
                "Tuesday": ["Morning", "Afternoon"],
                "Wednesday": ["Morning", "Afternoon"],
                "Thursday": ["Morning", "Afternoon"],
                "Friday": ["Morning", "Afternoon"]}

    # Checking classroom numbers and avalible class relations. If you got 30 slots for lessons and you got less than 30 it'll be work.
    def isNumberOfClassesEnough(self, bigClasses, smallClasses):
        return len(bigClasses) * 10 >= Course.numberOfCompulsoryCourses and len(smallClasses) * 10 + (
                len(bigClasses) * 10 - Course.numberOfCompulsoryCourses) >= Course.numberOfElectiveCourses

    # Placing service lessons for mandatory place.
    def findCorrectPlace(self, classes, courses, service, timesForYears):
        for _class in classes:  # To find correct place
            if _class.className[0] == 'b' and _class.code is None:
                if _class.day == service.day and _class.clock == service.clock:
                    _class.code = service.code

                    timesForYears[courses[service.code].year - 1][_class.day].remove(_class.clock)
                    if 0 == len(timesForYears[courses[service.code].year - 1][_class.day]):
                        timesForYears[courses[service.code].year - 1].pop(_class.day)
                    courses.pop(service.code)
                    break

    # readed input is correct or not
    def isInputOkay(self, row, parameterCount):
        return len(row) == parameterCount

    def main(self):
        maxTableIteration = 0
        while maxTableIteration < 1000:
            maxTableIteration += 1
            # Arranging  available times of lecturers.
            busyInstructors = dict()
            with open("busy.csv", mode='r') as busyFile:
                csvReader = csv.reader(busyFile, delimiter=';')
                for row in csvReader:
                    if self.isInputOkay(row, 3):
                        if row[0] not in busyInstructors:
                            busyInstructors[row[0]] = BusyInstructor(row[0])
                        busyInstructors[row[0]].appendBusyTimeSlot(row[1], row[2])

            # Reading number of classes and creating name of classes.
            numOfClasses = dict()
            with open("classroom.csv", mode='r') as classroomFile:
                csvReader = csv.reader(classroomFile, delimiter=';')
                for row in csvReader:
                    if (self.isInputOkay(row, 2)):
                        numOfClasses[row[0]] = int(row[1])

            bigClasses = ["bigClass_" + str(i + 1) for i in range(numOfClasses["big"])]
            smallClasses = ["smallClass_" + str(i + 1) for i in range(numOfClasses["small"])]

            # Read the classes and put all of them into a list.
            courses = dict()
            with open("Courses.csv", mode='r') as coursesFile:
                csvReader = csv.reader(coursesFile, delimiter=';')
                for row in csvReader:
                    if (self.isInputOkay(row, 7)):
                        courses[row[0]] = Course(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

            # Reading service lessons.
            services = []
            with open("service.csv", mode='r') as serviceFile:
                csvReader = csv.reader(serviceFile, delimiter=';')
                for row in csvReader:
                    if self.isInputOkay(row, 3):
                        services.append(ServiceCourse(row[0], row[1], row[2]))

            classes = [Classroom(className, day, clock, None) for day in
                       ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                       for clock in ["Morning", "Afternoon"] for className in bigClasses + smallClasses]
            timesForYears = [self.timeGenerator(), self.timeGenerator(), self.timeGenerator(), self.timeGenerator()]

            for service in services:
                if courses[service.code].CE == 'C':  # Compulsory Service Course
                    self.findCorrectPlace(classes, courses, service, timesForYears)
                else:  # Elective service course
                    self.findCorrectPlace(classes, courses, service, timesForYears)
                    if service.code in courses:  # if there is no available "small" class for the lesson. Put this into "big" class.
                        self.findCorrectPlace(classes, courses, service, timesForYears)

            # We calculating, In order to hold our lecturers' available time
            for busyInstructor in busyInstructors.values():
                busyInstructor.availableTimesCalculator(busyInstructors)

            if self.isNumberOfClassesEnough(bigClasses, smallClasses):
                Ccount = 0
                while len(courses.keys()) > 0 and Ccount < len(courses.keys()) * 20:
                    Ccount += 1
                    randomCourse = random.choice(list(courses.values()))
                    count = 0
                    while count < len(classes) * 20:
                        randomClassroom = random.choice(classes)
                        # Mandatory lesson must be in "big" classrooms. Also the classrom has to be available for setting lesson.
                        if randomClassroom.code is None and randomCourse.CE == 'C' and randomClassroom.className[
                            0] == 'b':
                            # The lessons of the  same year cannot be in same block.

                            if randomClassroom.day in timesForYears[
                                randomCourse.year - 1].keys() and randomClassroom.clock in \
                                    timesForYears[randomCourse.year - 1][randomClassroom.day]:

                                # Checking for available time of the lecturer.
                                if randomCourse.instructor in busyInstructors.keys():
                                    availableTimes = busyInstructors[randomCourse.instructor].availableTimeSlots
                                    if randomClassroom.day in availableTimes.keys() and randomClassroom.clock in \
                                            availableTimes[
                                                randomClassroom.day]:
                                        # Put the selected course here.

                                        randomClassroom.code = randomCourse.code
                                        # Deleting time line from timesForYears
                                        timesForYears[randomCourse.year - 1][randomClassroom.day].remove(
                                            randomClassroom.clock)
                                        if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                                            timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                                        courses.pop(randomCourse.code)  # Deleting course from courses
                                        break

                                else:  # Lecturer is always available.
                                    randomClassroom.code = randomCourse.code
                                    # Deleting time line from timesForYears
                                    timesForYears[randomCourse.year - 1][randomClassroom.day].remove(
                                        randomClassroom.clock)
                                    if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                                        timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                                    courses.pop(randomCourse.code)  # Deleting course from courses
                                    break
                        count += 1

                Ccount = 0
                while len(courses.keys()) > 0 and Ccount < len(courses.keys()) * 100:
                    Ccount += 1
                    randomCourse = random.choice(list(courses.values()))
                    count = 0
                    while count < len(classes) * 100:

                        randomClassroom = random.choice(classes)
                        # Is the classroom available at given day and given clock.
                        if randomClassroom.code is None:
                            # The lectures which are same years cannot be in same block.

                            # Friday Morning smallClass_1 None CENG465,INTERNET OF THINGS AND ITS APPLICATIONS,4,5,E,D,PROF.DR. REMZI YILDIRIM

                            if randomClassroom.day in timesForYears[
                                randomCourse.year - 1].keys() and randomClassroom.clock in \
                                    timesForYears[randomCourse.year - 1][randomClassroom.day]:

                                # Available times of lecturers.
                                if randomCourse.instructor in busyInstructors.keys():
                                    availableTimes = busyInstructors[randomCourse.instructor].availableTimeSlots

                                    if randomClassroom.day in availableTimes.keys() and randomClassroom.clock in \
                                            availableTimes[
                                                randomClassroom.day]:

                                        # Put the selected course here
                                        randomClassroom.code = randomCourse.code
                                        courses.pop(randomCourse.code)  # Deleting course from courses
                                        # Deleting time line from timesForYears
                                        timesForYears[randomCourse.year - 1][randomClassroom.day].remove(
                                            randomClassroom.clock)
                                        if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                                            timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                                        break
                                else:  # lecturer is always available.

                                    randomClassroom.code = randomCourse.code
                                    courses.pop(randomCourse.code)  # Deleting course from courses
                                    # Deleting time line from timesForYears
                                    timesForYears[randomCourse.year - 1][randomClassroom.day].remove(
                                        randomClassroom.clock)
                                    if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                                        timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                                    break
                        count += 1

            else:  # Don't have enough classrom
                # Increase the number of classrooms and start the program from scratch.

                Course.numberOfCompulsoryCourses = 0
                Course.numberOfElectiveCourses = 0
                if maxTableIteration == 999:
                    print("There is no enough classroom, unfortunately. " +
                          "Number of the classroom will be increased and program will start from scratch")
                    maxTableIteration = 0
                    oldBig = numOfClasses["big"]
                    oldSmall = numOfClasses["small"]
                    with open('classroom.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow(['big', str(oldBig + 1)])
                        writer.writerow(['small', str(oldSmall + 1)])

            if len(courses.keys()) == 0:
                break

        for i in classes:
            if i.code is None:
                i.code = "--------"

        [print(i) for i in classes]
        # print("Iteration", maxTableIteration)




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

