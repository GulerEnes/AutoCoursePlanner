"""

group Members:
1. EFŞAN ALBAYRAK - 19050151005
2. ÖZGE VARLIOĞLU - 18050111004
3. MELİS ALPKAYA - 18050111042
4. HALİT BURAK YEŞİLDAL - 18050111043
5. ENES GÜLER - 18050111005
6 .YAKUP BATUHAN ÖRDEK – 18050111041

"""
from Features import *
import ProjectObjects
from ProjectObjects import *

# Importing tkinter and ttk modules
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, ttk

if ProjectObjects.x:
    packetInstaller()
    ProjectObjects.x = False

    root = Tk()


    def showOutput(list):
        TOPFRAME_X = 500
        TOPFRAME_Y = 800

        width = root.winfo_screenwidth() // 2 - TOPFRAME_X // 2
        height = root.winfo_screenheight() // 2 - TOPFRAME_Y // 2

        top = Toplevel()
        top.geometry(str(TOPFRAME_X) + 'x' + str(TOPFRAME_Y) + "+" + str(width) + "+" + str(height))
        top.minsize(TOPFRAME_X, TOPFRAME_Y)
        top.maxsize(TOPFRAME_X, TOPFRAME_Y)
        top.title("show window")

        lshow = Label(top, text="\n".join([str(i) for i in list])).pack()
        top.mainloop()


    MAINFRAME_X = 600
    MAINFRAME_Y = 380
    COLOR = "#CECECE"

    width = root.winfo_screenwidth() // 2 - MAINFRAME_X // 2
    height = root.winfo_screenheight() // 2 - MAINFRAME_Y // 2

    root.geometry(str(MAINFRAME_X) + 'x' + str(MAINFRAME_Y) + "+" + str(width) + "+" + str(height))
    root.minsize(MAINFRAME_X, MAINFRAME_Y)
    root.maxsize(MAINFRAME_X, MAINFRAME_Y)
    root.configure(bg=COLOR)
    root.title("Auto Course Planner")

    # These are for parameters
    SLC_BUSY_PATH = StringVar()
    SLC_COURSES_PATH = StringVar()
    SLC_CLASSROOM_PATH = StringVar()
    SLC_SERVICE_PATH = StringVar()
    SLC_FOLDER_PATH = StringVar()

    option = StringVar()
    # These are for labels
    selectedFolderPath = StringVar()
    selectedBusyCsvPath = StringVar()
    selectedClassroomCsvPath = StringVar()
    selectedCoursesCsvPath = StringVar()
    selectedServiceCsvPath = StringVar()

    option.set("notSelected")
    selectedFolderPath.set("Not Selected!")
    selectedBusyCsvPath.set("Not Selected!")
    selectedClassroomCsvPath.set("Not Selected!")
    selectedCoursesCsvPath.set("Not Selected!")
    selectedServiceCsvPath.set("Not Selected!")

    BUSY_DICT = dict()
    NUM_OF_CLASSES_DICT = dict()
    COURSES_DICT = dict()
    SERVICES_LIST = list()


    def run():

        if option.get() == 'notSelected':
            return
        outputPath = "."
        options = [C_var_0.get(), C_var_1.get(), C_var_2.get(), C_var_3.get(), C_var_4.get()]

        if '1' in options[:-1]:
            outputPath = filedialog.askdirectory()

        import ProjectObjects
        program = ProjectObjects.Main()

        if option.get() == '0':
            result = program.main(SLC_FOLDER_PATH.get() + "/busy.csv",
                                  SLC_FOLDER_PATH.get() + "/classroom.csv",
                                  SLC_FOLDER_PATH.get() + "/Courses.csv",
                                  SLC_FOLDER_PATH.get() + "/service.csv",
                                  outputPath, options)

        if option.get() == '1':
            if __name__ == '__main__':
                if __name__ == '__main__':
                    result = program.main("", "", "", "", outputPath, options,
                                          [BUSY_DICT, NUM_OF_CLASSES_DICT, COURSES_DICT, SERVICES_LIST], True)

        if option.get() == '2':
            result = program.main(SLC_BUSY_PATH.get(), SLC_CLASSROOM_PATH.get(), SLC_COURSES_PATH.get(),
                                  SLC_SERVICE_PATH.get(),
                                  outputPath, options)

        if options[-1] == '1':
            showOutput(result)


    def filePathBtnf():
        TOPFRAME_X = 600
        TOPFRAME_Y = 220

        width = root.winfo_screenwidth() // 2 - TOPFRAME_X // 2
        height = root.winfo_screenheight() // 2 - TOPFRAME_Y // 2

        top = Toplevel()
        top.geometry(str(TOPFRAME_X) + 'x' + str(TOPFRAME_Y) + "+" + str(width) + "+" + str(height))
        top.minsize(TOPFRAME_X, TOPFRAME_Y)
        top.maxsize(TOPFRAME_X, TOPFRAME_Y)
        top.title("second window1")

        explanationLine1 = "If your all files are in same directory, you can just select that folder."
        explanationLine2 = "Be sure your files named as busy.csv, classroom.csv, Courses.csv, service.scv"

        explanationLabel1 = Label(top, text=explanationLine1).pack(pady=10)
        explanationLabel2 = Label(top, text=explanationLine2).pack()

        def pathSelectorBtn():
            try:
                s = filedialog.askdirectory()
                SLC_FOLDER_PATH.set(s)
                selectedFolderPath.set("selected path: " + s)
                option.set("0")
            except Exception as e:
                print(e)

        folderSelectBtn = Button(top, text="Select Folder", command=pathSelectorBtn).pack(pady=15)

        selectedFolderLabel = Label(top, textvariable=selectedFolderPath).pack(pady=5)
        continueBtn = Button(top, text="Continue", command=top.destroy).pack(pady=10)
        top.mainloop()


    def manuelInputBtnf():
        def busyAddBtnF():
            inst = insEntry.get()
            day = dayCB.get()
            clock = clockCB.get()

            if inst != '' and day != '' and clock != '':
                if inst not in BUSY_DICT:
                    BUSY_DICT[inst] = BusyInstructor(inst)
                BUSY_DICT[inst].appendBusyTimeSlot(day, clock)

                insEntry.delete(0, 'end')
            else:
                print("there are empty places")

        def courseAddBtnF():
            try:
                code = courseCodeEntry.get()
                name = courseNameEntry.get()
                year = int(yearCB.get())
                credit = int(courseCreditEntry.get())
                CE = c_e_CB.get()[0]  # Compulsory - Elective
                DS = d_s_CB.get()[0]  # Department - Service
                instructor = courseInsNameEntry.get()

                if code != '' and name != '' and CE != '' and DS != '' and instructor != '':
                    COURSES_DICT[code] = Course(code, name, year, credit, CE, DS, instructor)

                    courseCodeEntry.delete(0, 'end')
                    courseNameEntry.delete(0, 'end')
                    courseCreditEntry.delete(0, 'end')
                    courseInsNameEntry.delete(0, 'end')
                else:
                    print("there are empty places ")
            except:
                print("there are empty places ")

        def serviceAddBtnF():
            code = serviceCodeEntry.get()
            day = serviceDayCB.get()
            clock = serviceClockCB.get()

            if code != '' and day != '' and clock != '':
                SERVICES_LIST.append(ServiceCourse(code, day, clock))
                code.delete(0, 'end')
            else:
                print("there are empty places")

        def continueBtnF():
            try:
                bigNumber = int(bigClassEntry.get())
                smallNumber = int(smallClassEntry.get())

                if bigNumber >= 0 and smallNumber >= 0:
                    NUM_OF_CLASSES_DICT['big'] = bigNumber
                    NUM_OF_CLASSES_DICT['small'] = smallNumber

                    option.set('1')
                    top.destroy()
                else:
                    print("Enter valid number")
            except:
                print("there are empty places")

        TOPFRAME_X = 900
        TOPFRAME_Y = 500

        width = root.winfo_screenwidth() // 2 - TOPFRAME_X // 2
        height = root.winfo_screenheight() // 2 - TOPFRAME_Y // 2
        top = Toplevel()
        top.geometry(str(TOPFRAME_X) + 'x' + str(TOPFRAME_Y) + "+" + str(width) + "+" + str(height))
        top.minsize(TOPFRAME_X, TOPFRAME_Y)
        top.maxsize(TOPFRAME_X, TOPFRAME_Y)
        top.title("second window2")

        selectedDay = StringVar()
        selectedClock = StringVar()
        selectedYear = StringVar()
        selectedServiceDay = StringVar()
        selectedServiceClock = StringVar()
        selected_C_E = StringVar()
        selected_D_S = StringVar()
        # Busy
        busyFrame = LabelFrame(top, text="Add Busy Instructor Information")

        busyLabel1 = Label(busyFrame, text="Instructor").grid(row=0, column=0)
        busyLabel2 = Label(busyFrame, text="Day").grid(row=0, column=1)
        busyLabel3 = Label(busyFrame, text="Clock").grid(row=0, column=2)

        insEntry = Entry(busyFrame, width=20)
        insEntry.grid(row=1, column=0, padx=10, pady=5)

        dayCB = Combobox(busyFrame, textvariable=selectedDay, width=10)
        dayCB['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
        dayCB['state'] = 'readonly'
        dayCB.grid(row=1, column=1, padx=10, pady=5)

        clockCB = Combobox(busyFrame, textvariable=selectedClock, width=10)
        clockCB['values'] = ("Morning", "Afternoon")
        clockCB['state'] = 'readonly'
        clockCB.grid(row=1, column=2, padx=10, pady=5)

        busyAddBtn = Button(busyFrame, text="Add", command=busyAddBtnF).grid(row=1, column=3, padx=10, pady=5)

        # Classroom
        classroomFrame = LabelFrame(top, text="Enter Number of Classroom Types")
        classroomLabel1 = Label(classroomFrame, text="Big Classes: ").grid(row=0, column=0, padx=10, pady=5)
        bigClassEntry = Entry(classroomFrame, width=5)
        bigClassEntry.grid(row=0, column=1, padx=10, pady=5)

        classroomLabel2 = Label(classroomFrame, text="Small Classes: ").grid(row=0, column=2, padx=10, pady=5)
        smallClassEntry = Entry(classroomFrame, width=5)
        smallClassEntry.grid(row=0, column=3, padx=10, pady=5)

        # Courses
        coursesFrame = LabelFrame(top, text="Add a Course Information")
        coursesLabel1 = Label(coursesFrame, text="Code").grid(row=0, column=0)
        coursesLabel2 = Label(coursesFrame, text="Name").grid(row=0, column=1)
        coursesLabel3 = Label(coursesFrame, text="Year").grid(row=0, column=2)
        coursesLabel4 = Label(coursesFrame, text="Credit").grid(row=0, column=3)
        coursesLabel5 = Label(coursesFrame, text="C/E").grid(row=0, column=4)
        coursesLabel6 = Label(coursesFrame, text="D/S").grid(row=0, column=5)
        coursesLabel7 = Label(coursesFrame, text="Instructor Name").grid(row=0, column=6)

        courseCodeEntry = Entry(coursesFrame, width=10)
        courseCodeEntry.grid(row=1, column=0, padx=5, pady=5)
        courseNameEntry = Entry(coursesFrame, width=20)
        courseNameEntry.grid(row=1, column=1, padx=5, pady=5)

        yearCB = Combobox(coursesFrame, textvariable=selectedYear, width=5)
        yearCB['values'] = ('1', '2', '3', '4')
        yearCB['state'] = 'readonly'
        yearCB.grid(row=1, column=2, padx=5, pady=5)

        courseCreditEntry = Entry(coursesFrame, width=5)
        courseCreditEntry.grid(row=1, column=3, padx=5, pady=5)

        c_e_CB = Combobox(coursesFrame, textvariable=selected_C_E, width=5)
        c_e_CB['values'] = ('Compulsory', 'Elective')
        c_e_CB['state'] = 'readonly'
        c_e_CB.grid(row=1, column=4, padx=5, pady=5)

        d_s_CB = Combobox(coursesFrame, textvariable=selected_D_S, width=5)
        d_s_CB['values'] = ('Department', 'Service')
        d_s_CB['state'] = 'readonly'
        d_s_CB.grid(row=1, column=5, padx=5, pady=5)

        courseInsNameEntry = Entry(coursesFrame, width=20)
        courseInsNameEntry.grid(row=1, column=6, padx=5, pady=5)

        courseAddBtn = Button(coursesFrame, text="Add", command=courseAddBtnF).grid(row=1, column=7, padx=5, pady=5)

        # Service
        serviceFrame = LabelFrame(top, text="Add a Service Course Information")
        serviceLabel1 = Label(serviceFrame, text="Code").grid(row=0, column=0)
        serviceLabel2 = Label(serviceFrame, text="Day").grid(row=0, column=1)
        serviceLabel3 = Label(serviceFrame, text="Clock").grid(row=0, column=2)

        serviceCodeEntry = Entry(serviceFrame, width=10)
        serviceCodeEntry.grid(row=1, column=0, padx=5, pady=5)

        serviceDayCB = Combobox(serviceFrame, textvariable=selectedServiceDay, width=10)
        serviceDayCB['values'] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
        serviceDayCB['state'] = 'readonly'
        serviceDayCB.grid(row=1, column=1, padx=10, pady=5)

        serviceClockCB = Combobox(serviceFrame, textvariable=selectedServiceClock, width=10)
        serviceClockCB['values'] = ("Morning", "Afternoon")
        serviceClockCB['state'] = 'readonly'
        serviceClockCB.grid(row=1, column=2, padx=10, pady=5)

        serviceAddBtn = Button(serviceFrame, text="Add", command=serviceAddBtnF).grid(row=1, column=3, padx=5, pady=5)

        # Frame packing
        busyFrame.pack(fill='x', padx=20, pady=30)
        classroomFrame.pack(fill='x', padx=20)
        coursesFrame.pack(fill='x', padx=20, pady=30)
        serviceFrame.pack(fill='x', padx=20)

        continueBtn = Button(top, text="Continue", command=continueBtnF).pack(pady=10, padx=20, side=RIGHT)

        top.mainloop()


    def selectFilesBtnf():
        def selectBusy():
            try:
                SLC_BUSY_PATH.set(filedialog.askopenfilename())
                if len(SLC_BUSY_PATH.get()) != 0:
                    selectedBusyCsvPath.set("File Selected \u2713")
            except:
                pass

        def selectClassroom():
            try:
                SLC_CLASSROOM_PATH.set(filedialog.askopenfilename())
                if len(SLC_CLASSROOM_PATH.get()) != 0:
                    selectedClassroomCsvPath.set("File Selected \u2713")
            except:
                pass

        def selectCourses():
            try:
                SLC_COURSES_PATH.set(filedialog.askopenfilename())
                if len(SLC_COURSES_PATH.get()) != 0:
                    selectedCoursesCsvPath.set("File Selected \u2713")
            except:
                pass

        def selectService():
            try:
                SLC_SERVICE_PATH.set(filedialog.askopenfilename())
                if len(SLC_SERVICE_PATH.get()) != 0:
                    selectedServiceCsvPath.set("File Selected \u2713")
            except:
                pass

        TOPFRAME_X = 500
        TOPFRAME_Y = 350
        width = root.winfo_screenwidth() // 2 - TOPFRAME_X // 2
        height = root.winfo_screenheight() // 2 - TOPFRAME_Y // 2

        top = Toplevel()
        top.geometry(str(TOPFRAME_X) + 'x' + str(TOPFRAME_Y) + "+" + str(width) + "+" + str(height))
        top.minsize(TOPFRAME_X, TOPFRAME_Y)
        top.maxsize(TOPFRAME_X, TOPFRAME_Y)
        top.title("second window3")

        explanation = "Select all necessarily files one by one"
        explanationLabel = Label(top, text=explanation).pack(pady=10)

        btnFrameSelect = Frame(top)
        # Busy
        selectBusyCsvBtn = Button(btnFrameSelect, text="select busy.csv", command=selectBusy, width=20) \
            .grid(row=0, column=0, padx=10, pady=10)
        selectedBusyCsvPathLabel = Label(btnFrameSelect, textvariable=selectedBusyCsvPath) \
            .grid(row=0, column=1, padx=15, pady=10)

        # Classroom
        selectClassroomCsvBtn = Button(btnFrameSelect, text="select classroom.csv", command=selectClassroom, width=20) \
            .grid(row=1, column=0, padx=10, pady=10)
        selectedClassroomCsvPathLabel = Label(btnFrameSelect, textvariable=selectedClassroomCsvPath) \
            .grid(row=1, column=1, padx=15, pady=10)

        # Courses
        selectCoursesCsvBtn = Button(btnFrameSelect, text="select Courses.csv", command=selectCourses, width=20) \
            .grid(row=2, column=0, padx=10, pady=10)
        selectedCoursesCsvPathLabel = Label(btnFrameSelect, textvariable=selectedCoursesCsvPath) \
            .grid(row=2, column=1, padx=15, pady=10)

        # Service
        selectServiceCsvBtn = Button(btnFrameSelect, text="select service.csv", command=selectService, width=20) \
            .grid(row=3, column=0, padx=10, pady=10)
        selectedServiceCsvPathLabel = Label(btnFrameSelect, textvariable=selectedServiceCsvPath) \
            .grid(row=3, column=1, padx=15, pady=10)

        btnFrameSelect.pack()

        continueBtn = Button(top, text="Continue", command=top.destroy).pack(pady=30)
        option.set("2")
        top.mainloop()


    # Label
    l1 = Label(root, text="Chose a way to create course plan", font=('Helvatica', 12, 'bold'), background=COLOR,
               foreground="black")

    # Button frame start
    btnFrame = Frame(root)

    style = ttk.Style()
    style.configure("TButton", background=COLOR, font=('Helvatica', 9), width=15)

    filePathBtn = Button(btnFrame, text="With Folder Path", command=filePathBtnf, style="TButton")
    manuelInputBtn = Button(btnFrame, text="Manuel Input", command=manuelInputBtnf, style="TButton")
    selectFilesBtn = Button(btnFrame, text="Select Files", command=selectFilesBtnf, style="TButton")

    filePathBtn.grid(row=1, column=0)
    manuelInputBtn.grid(row=1, column=2)
    selectFilesBtn.grid(row=1, column=4)
    # Button frame end

    # CheckBoxFrame start
    CheckBoxFrame = Frame(root)

    C_var_0 = StringVar()
    C_var_1 = StringVar()
    C_var_2 = StringVar()
    C_var_3 = StringVar()
    C_var_4 = StringVar()

    style2 = ttk.Style()
    style2.configure("TCheckbutton", background=COLOR)

    c0 = Checkbutton(CheckBoxFrame, text="Pdf", variable=C_var_0, onvalue=1, offvalue=0, style="TCheckbutton")
    c0.grid(row=0,column=0, ipadx=21)

    l2 = Label(root, text="")

    if platform.system() == 'Linux':
        c0.config(state=DISABLED)
        l2.config(text="Pdf feature not works on Linux")

    c1 = Checkbutton(CheckBoxFrame, text="Docx", variable=C_var_1, onvalue=1, offvalue=0, style="TCheckbutton").grid(
        row=1,
        column=0,
        ipadx=16)
    c2 = Checkbutton(CheckBoxFrame, text="Excel", variable=C_var_2, onvalue=1, offvalue=0, style="TCheckbutton").grid(
        row=2,
        column=0,
        ipadx=16)
    c3 = Checkbutton(CheckBoxFrame, text="Csv", variable=C_var_3, onvalue=1, offvalue=0, style="TCheckbutton").grid(
        row=3,
        column=0,
        ipadx=21)
    c4 = Checkbutton(CheckBoxFrame, text="Show", variable=C_var_4, onvalue=1, offvalue=0, style="TCheckbutton").grid(
        row=4,
        column=0,
        ipadx=15)
    # CheckBoxFrame end

    # Run button

    runBtn = Button(root, text="Run", command=run, width=15)

    # placement
    l1.pack(pady=20)
    btnFrame.pack(pady=10)
    CheckBoxFrame.pack(pady=30)
    l2.pack(pady=5)
    runBtn.pack(pady=10)

    mainloop()
