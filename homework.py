name = str(input("Please enter your name:"))
surname = str(input("Please enter your surname:"))

your_rights = 3
while your_rights > 0:
    
    userName = str(input("Your name is:"))
    userSurname = str(input("Your surname is:"))
    if (userName == name) and (userSurname == surname):
        print("^^^^^^^^^^^^Welcome to my management system :)^^^^^^^^^^^^")
        break
    else:
        your_rights -=1
        print("Please enter the valid name and surname.")
        if your_rights == 0:
            print("Please try again later :(")
            exit()
my_courses_numbers = 0
your_courses = []

def checkCourse(course_number):   
    global my_courses_numbers
    global course_name
    a = 1
    while a > 0:
        print(f"Do you want to take {course_number}?(YES/NO)")
        your_answer = str(input("Your answer is:  "))
        if your_answer ==  "YES":
            my_courses_numbers += 1
            course_name = str(input(f"Name of your {course_number}:  "))
            your_courses.append(course_name)
            a -= 1
            print(f"---------------{course_name} is saved.--------------")
            return course_name
        elif your_answer == "NO":
            print(f"You didn't take {course_number}.")
            a -= 1
        else:
            print("You should enter a valid answer!!!")
    
     

course1 = checkCourse("course1")
course2 = checkCourse("course2")
course3 = checkCourse("course3")
course4 = checkCourse("course4")
course5 = checkCourse("course5")
if my_courses_numbers < 3:
    print(".....................You failed in class :(........................")
    exit()
elif 3 <= my_courses_numbers <= 5:
    print("------------------You must choose a course.-----------------")

dict1 = {
            "midterm": 33,
            "final"  : 57,
            "project": 82
}
dict2 = {
            "midterm": 89,
            "final"  : 50,
            "project": 25
}
dict3 = {
            "midterm": 45,
            "final"  : 51,
            "project": 82
}
dict4 = {
            "midterm": 33,
            "final"  : 96,
            "project": 13
}
dict5 = {
            "midterm": 61,
            "final"  : 54,
            "project": 72
}

def calculateExamPoints(my_dict):
    
    your_grade = my_dict["midterm"]*(3/10) + my_dict["final"]*(5/10) + my_dict["project"]*(2/10)
    if your_grade > 90:
       your_note = "AA :)"
    elif 90 > your_grade >  70:
        your_note = "BB"
    elif 70 > your_grade > 50:
        your_note = "CC"
    elif 50 > your_grade > 30:
        your_note = "DD"
    elif 30 > your_grade:
        your_note = "FF :( Unfortunately, you are failure."
    
    return f"You have {your_grade} average, so that you took --->  {your_note}  <---."

print("You should choose one of your courses, and write down.")

determined_course = str(input("Which courses want to take an exam?:  "))
if determined_course == course1:
    print(calculateExamPoints(dict1))
elif determined_course == course2:
    print(calculateExamPoints(dict2))
elif determined_course == course3:
    print(calculateExamPoints(dict3))
elif determined_course == course4:
    print(calculateExamPoints(dict4))
elif determined_course == course5:
    print(calculateExamPoints(dict5))






