import csv
from ProjectObjects import *
import random


def timeGenerator():
    return {"Monday": ["Morning", "Afternoon"],
            "Tuesday": ["Morning", "Afternoon"],
            "Wednesday": ["Morning", "Afternoon"],
            "Thursday": ["Morning", "Afternoon"],
            "Friday": ["Morning", "Afternoon"]}


def isNumberOfClassesEnough(bigClasses, smallClasses):
    return len(bigClasses) * 10 > Course.numberOfCompulsoryCourses and len(smallClasses) * 10 + (
            len(bigClasses) * 10 - Course.numberOfCompulsoryCourses) > Course.numberOfElectiveCourses


def findCorrectPlace(classes, courses, service, timesForYears):
    for _class in classes:  # To find correct place
        if _class.className[0] == 'b' and _class.code is None:
            if _class.day == service.day and _class.clock == service.clock:
                _class.code = service.code

                timesForYears[courses[service.code].year - 1][_class.day].remove(_class.clock)
                if 0 == len(timesForYears[courses[service.code].year - 1][_class.day]):
                    timesForYears[courses[service.code].year - 1].pop(_class.day)
                courses.pop(service.code)
                break


def putCourses(busyInstructors, courses, timesForYears, flag):
    Ccount = 0
    while len(courses.keys()) > 0 and Ccount < len(courses.keys()) * 20:
        Ccount += 1
        randomCourse = random.choice(list(courses.values()))
        count = 0
        while count < len(classes) * 20:
            randomClassroom = random.choice(classes)
            # Zorunlu ders, büyük sınıf ve bahsi geçen sınıfın o sırada boş olma durumu kontroü
            if (flag == 'E' and randomClassroom.code is None) or (
                    flag == 'C' and randomCourse.CE == 'C' and randomClassroom.className[0] == 'b'):
                # Aynı yıla ait olan derslerin aynı satırda olmaması için zaman kontrolü

                if randomClassroom.day in timesForYears[randomCourse.year - 1].keys() and randomClassroom.clock in \
                        timesForYears[randomCourse.year - 1][randomClassroom.day]:

                    # Hocanın müsaitlik kontrolü
                    if randomCourse.instructor in busyInstructors.keys():
                        availableTimes = busyInstructors[randomCourse.instructor].availableTimeSlots
                        if randomClassroom.day in availableTimes.keys() and randomClassroom.clock in availableTimes[
                            randomClassroom.day]:
                            # Put the fuckin course here

                            randomClassroom.code = randomCourse.code
                            # Deleting time line from timesForYears
                            timesForYears[randomCourse.year - 1][randomClassroom.day].remove(randomClassroom.clock)
                            if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                                timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                            courses.pop(randomCourse.code)  # Deleting course from courses
                            break

                    else:  # Hoca her zaman müsait
                        randomClassroom.code = randomCourse.code
                        # Deleting time line from timesForYears
                        timesForYears[randomCourse.year - 1][randomClassroom.day].remove(randomClassroom.clock)
                        if 0 == len(timesForYears[randomCourse.year - 1][randomClassroom.day]):
                            timesForYears[randomCourse.year - 1].pop(randomClassroom.day)
                        courses.pop(randomCourse.code)  # Deleting course from courses
                        break
            count += 1


maxTableTryNumber = 0


def changingClassNumbers(oldBig, oldSmall):
    with open('classroom.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow('Big;' + str(oldBig + 1))
        writer.writerow('Small;' + str(oldSmall + 1))


while maxTableTryNumber < 1000:
    maxTableTryNumber += 1
    # Hocacıklarımızın müsait olmadıkları zamanlar
    busyInstructors = dict()
    with open("busy.csv", mode='r') as busyFile:
        csvReader = csv.reader(busyFile, delimiter=';')
        for row in csvReader:
            if row[0] not in busyInstructors:
                busyInstructors[row[0]] = BusyInstructor(row[0])
            busyInstructors[row[0]].appendBusyTimeSlot(row[1], row[2])

    # Sınıf sayılarının okunması ve sınıf isimlerinin oluşturulması
    numOfClasses = dict()
    with open("classroom.csv", mode='r') as classroomFile:
        csvReader = csv.reader(classroomFile, delimiter=';')
        for row in csvReader:
            numOfClasses[row[0]] = int(row[1])

    bigClasses = ["bigClass_" + str(i + 1) for i in range(numOfClasses["big"])]
    smallClasses = ["smallClass_" + str(i + 1) for i in range(numOfClasses["small"])]

    # Derslerin okunması ve hepsinin tek bir listeye atılması
    courses = dict()
    with open("Courses.csv", mode='r') as coursesFile:
        csvReader = csv.reader(coursesFile, delimiter=';')
        for row in csvReader:
            courses[row[0]] = Course(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    # Service derslerinin okunması
    services = []
    with open("service.csv", mode='r') as serviceFile:
        csvReader = csv.reader(serviceFile, delimiter=';')
        for row in csvReader:
            services.append(ServiceCourse(row[0], row[1], row[2]))

    classes = [Classroom(className, day, clock, None) for className in bigClasses + smallClasses
               for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] for clock in
               ["Morning", "Afternoon"]]

    timesForYears = [timeGenerator(), timeGenerator(), timeGenerator(), timeGenerator()]

    # Service derslerinin yerleştirilmesi
    for service in services:
        if courses[service.code].CE == 'C':  # Compulsory Service Course
            findCorrectPlace(classes, courses, service, timesForYears)
        else:  # Elective service course
            findCorrectPlace(classes, courses, service, timesForYears)
            if service.code in courses:  # Eğer uygun küçük sınıf yoksa büyük sınıfa koy
                findCorrectPlace(classes, courses, service, timesForYears)

    # Hocacıklarımızın müsait olduğu zamanları tutabilmek için hesaplama yapıyoruz
    for busyInstructor in busyInstructors.values():
        busyInstructor.availableTimesCalculator(busyInstructors)

    if isNumberOfClassesEnough(bigClasses, smallClasses):
        putCourses(busyInstructors, courses, timesForYears, 'C')
        putCourses(busyInstructors, courses, timesForYears, 'E')


    else:  # Sınıf sayısı yetmiyor
        # Sınıfsayısını artır ve bütün dosyayı en baştan çalıştır.
        Course.numberOfCompulsoryCourses = 0
        Course.numberOfElectiveCourses = 0
        if maxTableTryNumber == 999:
            maxTableTryNumber = 0
            changingClassNumbers(numOfClasses["big"], numOfClasses["small"])

    if len(courses.keys()) == 0:
        break


[print(i) for i in classes]
