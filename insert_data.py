import pymongo

# 连接 MongoDB 数据库
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["course_system"]
students_collection = db["students"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]

# 插入示例学生数据，确保学生ID唯一
students_data = [
    {"student_id": "1001", "student_name": "Alice"},
    {"student_id": "1002", "student_name": "Bob"},
    {"student_id": "1003", "student_name": "Charlie"},
    {"student_id": "1004", "student_name": "David"},
    {"student_id": "1005", "student_name": "Eva"}
]

for student in students_data:
    existing_student = students_collection.find_one({"student_id": student["student_id"]})
    if existing_student is None:
        students_collection.insert_one(student)
        print(f"学生 {student['student_id']} 添加成功!")
    else:
        print(f"学生ID {student['student_id']} 已存在!")

# 插入示例课程数据，确保课程ID唯一
courses_data = [
    {"course_id": "CS101", "course_name": "计算机科学入门", "instructor": "张老师"},
    {"course_id": "ENG201", "course_name": "英语进阶", "instructor": "王老师"},
    {"course_id": "MATH301", "course_name": "高等数学", "instructor": "李老师"},
    {"course_id": "PHY202", "course_name": "物理学导论", "instructor": "赵老师"},
    {"course_id": "CHEM101", "course_name": "化学基础", "instructor": "刘老师"}
]

for course in courses_data:
    existing_course = courses_collection.find_one({"course_id": course["course_id"]})
    if existing_course is None:
        courses_collection.insert_one(course)
        print(f"课程 {course['course_id']} 添加成功!")
    else:
        print(f"课程ID {course['course_id']} 已存在!")

print("示例学生和课程数据插入完成!")

db = client["course_system"]
students_collection = db["students"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]

# 查询现有的学生和课程信息
existing_students = set(student["student_id"] for student in students_collection.find())
existing_courses = set(course["course_id"] for course in courses_collection.find())

# 插入示例选课数据，确保学生ID和课程ID组合唯一
enrollments_data = [
    {"student_id": "1001", "course_id": "CS101"},
    {"student_id": "1002", "course_id": "ENG201"},
    {"student_id": "1003", "course_id": "MATH301"},
    {"student_id": "1004", "course_id": "PHY202"},
    {"student_id": "1005", "course_id": "CHEM101"}
]

for enrollment in enrollments_data:
    student_id = enrollment["student_id"]
    course_id = enrollment["course_id"]

    # 检查学生ID和课程ID是否存在
    if student_id not in existing_students:
        print(f"学生ID {student_id} 不存在，无法选课。")
        continue

    if course_id not in existing_courses:
        print(f"课程ID {course_id} 不存在，无法选课。")
        continue

    # 检查学生ID和课程ID组合是否唯一
    existing_enrollment = enrollments_collection.find_one({"student_id": student_id, "course_id": course_id})
    if existing_enrollment is None:
        enrollments_collection.insert_one(enrollment)
        print(f"学生 {student_id} 选课 {course_id} 成功!")
    else:
        print(f"学生 {student_id} 已选过课程 {course_id}!")

print("示例选课数据插入完成!")
