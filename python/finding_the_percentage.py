#   You have a record of N students. Each record contains the student's name,
#   and their percent marks in Maths, Physics and Chemistry. The marks can be
#   floating values. The user enters some integer N followed by the names and
#   marks for N students. You are required to save the record in a dictionary
#   data type. The user then enters a student's name. Output the average
#   percentage marks obtained by that student, correct to two decimal places.

if __name__ == '__main__':
    n = int(input())    # Number of students
    student_marks = {}  # Where we will store names and respective marks.

    # Test Case
    # student_marks = {'Elizabeth': [99, 89, 91], 'Erika': [95, 96, 96], 'John': [89, 91.5, 94]}
    # query_name = 'John'

    for index in range(n):
        name, *line = input().split()   # eddie 96 89 92
        # name = 'eddie'
        # line = ['96', '89', '92']
        # *line = 96 89 92

        # "map() function returns a list of the results after applying
        # the given function to each item of a given iterable (list, tuple etc.)"
        scores = list(map(float, line))

        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        print("{0:.2f}".format(round(sum(student_marks[query_name])/3.0, 2)))

