# Given the names and grades for each student
# in a Physics class of N students, store them
# in a nested list and print the name(s) of
# any student(s) having the second lowest grade.

# Note: If there are multiple students with the
#   same grade, order their names alphabetically
#   and print each name on a new line.


# Reference(s):
# https://stackabuse.com/lambda-functions-in-python/

if __name__ == '__main__':

    # index = 0
    # # Get the students names and grade
    # for index in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([])
    #     students[index] = [name, score]
    #     index += 1

    # Test Case #1
    # students = [['Tom', -32], ['Andy', -10], ['Edward', -5], ['christina', 78.0], ['erika', 78.0], ['nancy', 89.0],
    #             ['derek', 89.0], ['anna', 90.0], ['burke', 94.0], ['meredith', 99.0]]
    # Test Case #2
    students = [['Abel', -50], ['Henry', -50], ['Jacob', -50], ['Ashley', 51]]

    # Sort the students based on grade using a lamda function.
    #   "In Python, we use the lambda keyword to declare an anonymous function,
    #   which is why we refer to them as "lambda functions". An anonymous function
    #   refers to a function declared with no name. Although syntactically they
    #   look different, lambda functions behave in the same way as regular functions
    #   that are declared using the def keyword."

    students.sort(key=lambda x: x[1])

    # Skip all the students who have a score that is less than 0.
    marker = 0
    for index in range(0, len(students)):
        if students[index][-1] > 0:
            marker = index
            break
    # Skip all the students who have the same lowest score.
    hit = 0
    lowest_grade = students[marker][-1]
    for index in range(marker, len(students)):
        if (students[index][-1] != lowest_grade) or (index == len(students) - 1):
            hit = index
            break

    # Now we know where the student with the second lowest score is.
    # Find any student with the same second lowest score and add them to the list, if any exist.
    second_lowest_grades = []
    second_lowest_grades.append(students[hit][0])
    second_lowest_grade = students[hit][-1]

    for index in range(hit + 1, len(students)):
        if students[index][-1] == second_lowest_grade:
            second_lowest_grades.append(students[index][0])

    # Sort the names of the students with the second lowest scores.
    second_lowest_grades.sort()
    [print(item) for item in second_lowest_grades]