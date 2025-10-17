"""
场景 3：数据类（dataclass）字段定义

应用：配合 @dataclass 定义结构化数据，自动生成 __init__ 等方法
"""

from dataclasses import dataclass, field

# ✅ Python 3.9+ 方式：使用内置泛型

@dataclass
class Student:
    """学生信息"""
    name: str
    age: int
    grades: list[float]  # 成绩列表
    metadata: dict[str, str]  # 元数据
    courses: list[str] = field(default_factory=list)  # 课程列表
    
    def average_grade(self) -> float:
        """计算平均成绩"""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


@dataclass
class Course:
    """课程信息"""
    code: str
    name: str
    credits: int
    prerequisites: list[str] = field(default_factory=list)
    enrolled_students: set[int] = field(default_factory=set)
    
    def enroll(self, student_id: int) -> None:
        """学生选课"""
        self.enrolled_students.add(student_id)
    
    def get_enrollment_count(self) -> int:
        """获取选课人数"""
        return len(self.enrolled_students)


@dataclass
class Grade:
    """成绩记录"""
    student_id: int
    course_code: str
    score: float
    components: dict[str, float]  # 成绩组成（作业、考试等）
    
    def is_passing(self) -> bool:
        """是否及格"""
        return self.score >= 60.0


@dataclass
class Transcript:
    """成绩单"""
    student_id: int
    student_name: str
    grades: list[Grade]
    gpa: float = 0.0
    
    def calculate_gpa(self) -> float:
        """计算 GPA"""
        if not self.grades:
            return 0.0
        
        total_score = sum(g.score for g in self.grades)
        self.gpa = total_score / len(self.grades)
        return self.gpa


print("=" * 60)
print("场景 3：数据类字段定义")
print("=" * 60)

# 示例 1：学生信息
print("\n[示例 1] 学生信息：\n")

student = Student(
    name="Alice",
    age=20,
    grades=[85.5, 92.0, 78.5, 90.0],
    metadata={"email": "alice@example.com", "phone": "123-4567"},
    courses=["CS101", "MATH201", "PHY101"]
)

print(f"学生: {student.name}")
print(f"年龄: {student.age}")
print(f"成绩: {student.grades}")
print(f"平均分: {student.average_grade():.2f}")
print(f"课程: {student.courses}")
print(f"元数据: {student.metadata}")

# 示例 2：课程信息
print("\n[示例 2] 课程信息：\n")

course = Course(
    code="CS201",
    name="数据结构",
    credits=4,
    prerequisites=["CS101"]
)

# 学生选课
course.enroll(1001)
course.enroll(1002)
course.enroll(1003)

print(f"课程: {course.name} ({course.code})")
print(f"学分: {course.credits}")
print(f"前置课程: {course.prerequisites}")
print(f"选课人数: {course.get_enrollment_count()}")

# 示例 3：成绩记录
print("\n[示例 3] 成绩记录：\n")

grade1 = Grade(
    student_id=1001,
    course_code="CS201",
    score=88.5,
    components={
        "作业": 25.0,
        "期中考试": 30.0,
        "期末考试": 33.5
    }
)

print(f"学生ID: {grade1.student_id}")
print(f"课程: {grade1.course_code}")
print(f"总分: {grade1.score}")
print(f"成绩组成: {grade1.components}")
print(f"是否及格: {grade1.is_passing()}")

# 示例 4：成绩单
print("\n[示例 4] 成绩单：\n")

grades_list = [
    Grade(1001, "CS101", 85.0, {"作业": 20, "考试": 65}),
    Grade(1001, "MATH201", 92.0, {"作业": 22, "考试": 70}),
    Grade(1001, "PHY101", 78.5, {"作业": 18, "考试": 60.5})
]

transcript = Transcript(
    student_id=1001,
    student_name="Alice",
    grades=grades_list
)

gpa = transcript.calculate_gpa()
print(f"学生: {transcript.student_name}")
print(f"课程数: {len(transcript.grades)}")
print(f"GPA: {gpa:.2f}")

print("\n[所有课程成绩]")
for g in transcript.grades:
    status = "✅ 及格" if g.is_passing() else "❌ 不及格"
    print(f"  {g.course_code}: {g.score:.1f} {status}")

print("\n[dataclass 的优势]")
print("  ✅ 自动生成 __init__, __repr__, __eq__ 等方法")
print("  ✅ 类型注解清晰，支持静态检查")
print("  ✅ 使用 field() 设置默认工厂")
print("  ✅ 代码简洁，减少样板代码")

print("\n💡 总结：dataclass + 内置泛型 = 简洁的数据结构定义")

