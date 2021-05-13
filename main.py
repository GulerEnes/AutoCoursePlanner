from ProjectObjects import *
import csv

# Reading number of classes
#numOfClasses = dict()
classrooms = []
with open("Sample_files/classroom.csv", mode='r') as classroomFile:
    csvReader = csv.reader(classroomFile, delimiter=';')
    for row in csvReader:
        classrooms.append(Classroom(row[0],row[1]))
#print(classrooms)
#print(Classroom.numOfClassroom)
Classroom.bigClassAmount = classrooms[0].amount
Classroom.smallClassAmount = classrooms[1].amount
#print(Classroom.bigClassAmount)
#print(Classroom.smallClassAmount)

courses = []
with open("Sample_files/Courses.csv", mode='r') as coursesFile:
    csvReader = csv.reader(coursesFile, delimiter=';')
    for row in csvReader:
        courses.append(Course(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
#print(courses)

services = []
with open("Sample_files/service.csv", mode='r') as serviceFile:
    csvReader = csv.reader(serviceFile, delimiter=';')
    for row in csvReader:
        services.append(ServiceCourse(row[0], row[1], row[2]))
#print(services)

busyInstructors = dict()
with open("Sample_files/busy.csv", mode='r') as busyFile:
    csvReader = csv.reader(busyFile, delimiter=';')
    for row in csvReader:
        if row[0] not in busyInstructors:
            i = BusyInstructor(row[0])
            busyInstructors[row[0]] = i
            BusyInstructor.appendBusyTimeSlot(i, row[1], row[2])
            busyInstructors[row[0]] = i
        else:
            BusyInstructor.appendBusyTimeSlot(busyInstructors[row[0]], row[1], row[2])

#print(busyInstructors)

#We combine the cources and services objects
for course in courses:
    for service in services:
        if course.code == service.code:
            course.serviceTimeSlot_day = service.day
            course.serviceTimeSlot_clock = service.clock
#print(courses)

years = [[]]*4
print(years)
for course in courses:
    if int(course.year) == 1:
        years[0].append(course)
    elif int(course.year) == 2:
        years[1].append(course)
    elif int(course.year) == 3:
        years[2].append(course)
    else:
        years[3].append(course)
print(years[0])



"""cirriculum = []
for service in services:
    c = Cirriculum(service.day,service.clock,"null",service.code)
    cirriculum.append(c)"""

#print(cirriculum)


"""
daysDic = { 0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
clockDic = {0: "Morning", 1: "Afternoon"}

daysDic2 = { "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
clockDic2 = {"Morning": 0, "Afternoon": 1}"""


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
clock = ['Morning', 'Afternoon']

i = 0
j = 0
matrix = []
for i in range(len(days)):
    for j in range(len(clock)):
        matrix += [[days[i], clock[j]]]
        #print(matrix)


"""
a = 0
for service in services:
    for a in range(len(days)*len(clock)):
        print(a)
        if matrix[a][0] == service.day and matrix[a][1] == service.clock:
            #print(a)
            matrix[a] = service
            print(matrix[a])
            break
"""












            





