import _sqlite3
conn = _sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instructor TEXT,
               )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY(student_id) REFERENCES students(id),
               FOREIGN KEY(course_id) REFERENCES courses(course_id),
               PRIMARY KEY(student_id, course_id)
               )""")

while(True):
    print("\n1.Додати нового студента")
    print("2.Додати новий курс")
    print("3.Показати список студентів")
    print("4.Показати список курсів")
    print("5.Зареєстувати студентів на курс")
    print("6.Показати студентів на конкретному курсі")
    print("7.Вийти")
    choise = input("")
    if choise == "1":
        name=input("Введіть ім'я студента")
        age=int(input("Введіть вік"))
        major=input("Введіть спеціальність студента")
        cursor.execute("INSERT INTO students(name,age,major) VALUES (?,?,?)",(name,age,major))
        conn.commit()
    elif choise=="2":
        course=input("Введіть назву курсу")
        instuctor=input("Введіть викладача курсу")
        cursor.execute("INSERT INTO course(course,instuctor) VALUES (?,?)",(course,instuctor))
    elif choise=="3":
        cursor.execute("SELECT * FROM students")
        students=cursor.fetchall()
        if not students:
            print("У базі немає студентів")
        else:
            print("\nСписок студентів")
            for i in students:
                print(f"ID:{i[0]}, Ім'я:{i[1]}, Вік:{i[2]}, Спеціальність:{i[3]}")
    elif choise=="4":
        cursor.execute("SELECT * FROM course")
        curses=cursor.fetchall()
        if not curses:
            print("")
        else:
            print("\n")
            for i in curses:
                print(f"ID:{i[0]},Назва курсу:{i[1]},Викладачі:{i[2]}")
    elif choise=="5":
        student_id=int(input("Введіть ID студента "))
        course_id=int(input("Введіть ID курсу"))
        cursor.execute("INSERT INTO course (student_id,course_id) VALUES (?,?)",(student_id,course_id))
        conn.commit
    elif choise=="6":
        course_id=int(input("Введіть ID курсу"))
        cursor.execute("""SELECT student.id, student.name, student.age, student.major
                       FROM students , student_course
                       WHERE students.id=student_courses.student_id
                       AND student_courses.course_id=?""",(course_id))
        students_on_course=cursor.fetchall()
        if not students_on_course:
            print("")
        else:
            print("")
            for i in students_on_course:
                print(f"ID:{i[0]}, Ім'я:{i[1]}, Вік:{i[2]}, Спеціальність:{i[3]}")
    elif choise=="7":
        break
    else:
        print("")
        
conn.close