class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = [[int(i) for i in r.split()] for r in matrix_string.split("\n")]
        self.columns = [list(l) for l in zip(*self.rows)]
#         self.matrix_string = matrix_string
#
#     def row(self, index):
#         try:
#             row = self.matrix_string.split('\n')[index - 1]
#             return [int(x) for x in row.split()]
#         except IndexError:
#             raise MatrixIndexOutOfBounds("Row outside of range of matrix.")
#
#     def column(self, index):
#         col = []
#         try:
#             for i in self.matrix_string.split('\n'):
#                 col.append(i.split()[index - 1])
#                 return [int(x) for x in col]
#         except IndexError:
#             raise MatrixIndexOutOfBounds("Column outside of range of matrix.")
#
#
# class MatrixIndexOutOfBounds(Exception):
#     pass

