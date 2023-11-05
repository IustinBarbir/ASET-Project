# Matrix Class
class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def decode(self):
        pass

# Concrete Matrix Implementations
class SparseMatrix(Matrix):
    def decode(self):
        return "Decoding using Stern's ISD algorithm for Sparse Matrix"

class DenseMatrix(Matrix):
    def decode(self):
        return "Decoding using Stern's ISD algorithm for Dense Matrix"

# Matrix Factory
class MatrixFactory:
    @staticmethod
    def create_matrix(matrix_type, matrix_data):
        if matrix_type == "sparse":
            return SparseMatrix(matrix_data)
        elif matrix_type == "dense":
            return DenseMatrix(matrix_data)
        else:
            raise ValueError("Invalid matrix type")

# Client code
def main():
    matrix_type = "sparse"  # You can change this to "dense" as needed
    matrix_data = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]  # Your matrix data here
    matrix = MatrixFactory.create_matrix(matrix_type, matrix_data)
    result = matrix.decode()
    print(result)

if __name__ == "__main__":
    main()
