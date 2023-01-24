class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self.grades)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_av_student(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades) / len(grades)
            count += 1
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} ' \
              f'\nСредняя оценка за домашнее задание: {self.get_av_student()}' \
              f'\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)} ' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не верное сравнение')
            return
        return self.get_av_student() < other.get_av_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}
        Lecturer.lecturer_list.append(self.lect_grades)

    def get_av_lect(self):
        sum_hw = 0
        count = 0
        for grades in self.lect_grades.values():
            sum_hw += sum(grades) / len(grades)
            count += 1
        return round(sum_hw / count, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} ' \
              f'\nСредняя оценка за лекции: {self.get_av_lect()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не верное сравнение!')
            return
        return self.get_av_lect() < other.get_av_lect()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Roy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Git']
best_student.finished_courses += ['HTML']

best_student1 = Student('Bob', 'Spenser', 'male')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['Java']
best_student1.courses_in_progress += ['Git']
best_student1.finished_courses += ['HTML']
best_student1.finished_courses += ['C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer1 = Reviewer('Bruce', 'Lee')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.courses_attached += ['C++']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.courses_attached += ['HTML']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'C++', 8)
cool_reviewer.rate_hw(best_student1, 'Python', 7)
cool_reviewer.rate_hw(best_student1, 'Java', 10)
cool_reviewer.rate_hw(best_student1, 'Git', 8)

cool_lecturer = Lecturer('Bill', 'Angry')
cool_lecturer.courses_attached += ['C++']
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['Python']
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'C++', 10)
best_student.rate_lect(cool_lecturer, 'Java', 7)

cool_lecturer1 = Lecturer('Ewan', 'Spicy')
cool_lecturer1.courses_attached += ['Python']
cool_lecturer1.courses_attached += ['Java']
cool_lecturer1.courses_attached += ['Git']
best_student1.rate_lect(cool_lecturer1, 'Python', 9)
best_student1.rate_lect(cool_lecturer1, 'Java', 10)
best_student1.rate_lect(cool_lecturer1, 'Git', 6)
best_student1.rate_lect(cool_lecturer1, 'Python', 5)

print(f'{best_student}\n{best_student1}\n')
print(f'{cool_lecturer}\n{cool_lecturer1}\n')
print(f'{cool_reviewer}\n{cool_reviewer1}\n')


def get_av_st(students, course):
    sum_hw = 0
    count = 0
    for student in students:
        if course in student:
            sum_hw += sum(student[course]) / len(student[course])
            count += 1
            return f'Средняя оценка студентов по курсу {course}: {round(sum_hw / count, 2)}'
    return 'Нет оценок по курсу!'


print(get_av_st(Student.student_list, 'Python'))


def get_av_lecturer(lecturers, course):
    sum_hw = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer:
            sum_hw += sum(lecturer[course]) / len(lecturer[course])
            count += 1
            return f'Средняя оценка лекторов по курсу {course}: {round(sum_hw / count, 2)}'
    return 'Нет оценок по курсу!'


print(get_av_lecturer(Lecturer.lecturer_list, 'Python'))
