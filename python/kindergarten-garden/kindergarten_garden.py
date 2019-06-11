class Garden(object):
    FLOWERS = { 'V':'Violets', 'R':'Radishes', 'C':'Clover', 'G':'Grass' }
    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        diagram = self.diagram.split('\n')
        student_index = self.students.index(student)
        flower_list = []
        for row in diagram:
            flower_list.append(self.FLOWERS[row[student_index * 2]])
            flower_list.append(self.FLOWERS[row[student_index * 2 + 1]])
        return flower_list
        