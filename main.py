from ProjectObjects import *
import csv

# Reading number of classes
numOfClasses = dict()
with open("Sample_files/classroom.csv", mode='r') as classroomFile:
    csvReader = csv.reader(classroomFile, delimiter=';')
    for row in csvReader:
        numOfClasses[row[0]] = row[1]

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


