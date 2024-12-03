import random

# ���� ������� ������� N � ����� K
N = 6  # ����������� ������� (������ ����� ��� ���������� ������ � ���������)
K = 3  # ��������� K

# ��������� ������� A ���������� ������� � ��������� [-10, 10]
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

# ������� ��� �������� ��������� ������������ ������� ���������
def is_symmetric(matrix, start, end):
    for i in range(start, end):
        for j in range(start, end):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# ������������ ������� F ��� ����� ������� A
F = [row[:] for row in A]

# ���������� ������� 1, 2, 3, 4
half = N // 2

# ��������� �������������� ������� 1 ������������ �������
if is_symmetric(A, 0, half):
    # ������ ������� 2 � 4 �������
    for i in range(half):
        for j in range(half, N):
            F[i][j], F[N - i - 1][j] = F[N - i - 1][j], F[i][j]
    
    # ������ ������� 1 � 3 �������
    for i in range(half):
        for j in range(half):
            F[i][j], F[N - i - 1][j] = F[N - i - 1][j], F[i][j]

# ��������� ������ � ���������� ��������� A*A^T - K*(A+F)
def matrix_multiply(X, Y):
    size = len(X)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def matrix_add(X, Y):
    size = len(X)
    return [[X[i][j] + Y[i][j] for j in range(size)] for i in range(size)]

def matrix_subtract(X, Y):
    size = len(X)
    return [[X[i][j] - Y[i][j] for j in range(size)] for i in range(size)]

def matrix_scalar_multiply(X, scalar):
    size = len(X)
    return [[X[i][j] * scalar for j in range(size)] for i in range(size)]

# A * A^T
A_T = [[A[j][i] for j in range(N)] for i in range(N)]  # ���������������� A
A_AT = matrix_multiply(A, A_T)

# A + F
A_plus_F = matrix_add(A, F)

# K * (A + F)
K_A_plus_F = matrix_scalar_multiply(A_plus_F, K)

# �������� ���������
result = matrix_subtract(A_AT, K_A_plus_F)

# ����� �����������
print("������� A:")
for row in A:
    print(row)

print("\n������� F:")
for row in F:
    print(row)

print("\n��������� ��������� A*A^T - K*(A+F):")
for row in result:
    print(row)
