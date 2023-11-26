import pymongo

# 连接 MongoDB 数据库
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["course_system"]
students_collection = db["students"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]

# 定义选课系统的基本功能
def add_course(course_id, course_name, instructor):
    course = {
        "course_id": course_id,
        "course_name": course_name,
        "instructor": instructor
    }
    courses_collection.insert_one(course)
    print(f"课程 {course_name} 添加成功!")

def remove_course(course_id):
    result = courses_collection.delete_one({"course_id": course_id})
    if result.deleted_count > 0:
        print(f"课程 {course_id} 删除成功!")
    else:
        print(f"未找到课程 {course_id}!")

def enroll_student(student_id, course_id):
    enrollment = {
        "student_id": student_id,
        "course_id": course_id
    }
    existing_enrollment = enrollments_collection.find_one(enrollment)
    if existing_enrollment is None:
        enrollments_collection.insert_one(enrollment)
        print(f"学生 {student_id} 选课 {course_id} 成功!")
    else:
        print(f"学生 {student_id} 已选过课程 {course_id}!")

def withdraw_student(student_id, course_id):
    result = enrollments_collection.delete_one({"student_id": student_id, "course_id": course_id})
    if result.deleted_count > 0:
        print(f"学生 {student_id} 退课成功!")
    else:
        print(f"未找到学生 {student_id} 或学生未选过课程 {course_id}!")

def display_courses():
    courses = courses_collection.find()
    for course in courses:
        print(f"课程ID: {course['course_id']}, 课程名称: {course['course_name']}, 授课教师: {course['instructor']}")

def display_student_courses(student_id):
    enrollments = enrollments_collection.find({"student_id": student_id})
    print(f"\n学生 {student_id} 已选课程:")
    for enrollment in enrollments:
        course = courses_collection.find_one({"course_id": enrollment["course_id"]})
        print(f"课程ID: {course['course_id']}, 课程名称: {course['course_name']}, 授课教师: {course['instructor']}")

def display_course_students(course_id):
    enrollments = enrollments_collection.find({"course_id": course_id})
    print(f"\n课程 {course_id} 的选修学生:")
    for enrollment in enrollments:
        student = students_collection.find_one({"student_id": enrollment["student_id"]})
        print(f"学生ID: {student['student_id']}, 学生姓名: {student['student_name']}")

# 命令行交互界面
while True:
    print("\n选课系统命令:")
    print("1. 添加课程")
    print("2. 删除课程")
    print("3. 选课")
    print("4. 退课")
    print("5. 查询课程")
    print("6. 查询学生的选课")
    print("7. 查询课程下选修的学生")
    print("0. 退出")

    choice = input("请输入命令编号: ")

    if choice == "1":
        course_id = input("请输入课程ID: ")
        course_name = input("请输入课程名称: ")
        instructor = input("请输入授课教师: ")
        add_course(course_id, course_name, instructor)
    elif choice == "2":
        course_id = input("请输入要删除的课程ID: ")
        remove_course(course_id)
    elif choice == "3":
        student_id = input("请输入学生ID: ")
        course_id = input("请输入课程ID: ")
        enroll_student(student_id, course_id)
    elif choice == "4":
        student_id = input("请输入学生ID: ")
        course_id = input("请输入课程ID: ")
        withdraw_student(student_id, course_id)
    elif choice == "5":
        display_courses()
    elif choice == "6":
        student_id = input("请输入学生ID: ")
        display_student_courses(student_id)
    elif choice == "7":
        course_id = input("请输入课程ID: ")
        display_course_students(course_id)
    elif choice == "0":
        print("感谢使用选课系统，再见！")
        break
    else:
        print("无效的命令，请重新输入。")
