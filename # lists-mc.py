# lists-mc
# Henry Roeser
# 10/29/24

print(f'Semester 1 Grade Report')

print(" ")

student_name = 'CANO, Jaxsen' 
print(f'Student: {student_name}')
school_name = 'West Senior High School'
print(f'School: {school_name}')
course_name = 'Chemistry'
print(f'Course: {course_name}')
test_scores = []
test_scores.append(87)
test_scores.append(77)
test_scores.append(92)
test_scores.append(90)
num_elements = len(test_scores)
average_score = sum(test_scores) / num_elements
print(f'Average Score: {average_score:.2f}')

print(" ")

student_name = 'FOLGMANN, Mark' 
print(f'Student: {student_name}')
school_name = 'Central Senior High School'
print(f'School: {school_name}')
course_name = 'History'
print(f'Course: {course_name}')
test_scores = []
test_scores.append(73)
test_scores.append(79)
test_scores.append(83)
test_scores.append(89)
num_elements = len(test_scores)
average_score = sum(test_scores) / num_elements
print(f'Average Score: {average_score:.2f}')