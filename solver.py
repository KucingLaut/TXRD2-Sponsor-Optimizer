import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_hungarian(matrix, maximize=False):
    """
    Solves the assignment problem using the Hungarian algorithm.
    
    Parameters:
    - matrix (2D list or numpy array): The cost matrix to minimize/maximize.
    - maximize (bool): If True, solve the maximization problem.
    
    Returns:
    - row_ind (list): The row indices of the optimal assignment.
    - col_ind (list): The column indices of the optimal assignment.
    - total_cost (float): The total cost of the optimal assignment.
    """
    # Convert to numpy array if necessary
    matrix = np.array(matrix)
    
    # Handle maximization by converting to minimization problem
    if maximize:
        matrix = matrix.max() - matrix
    
    # If the matrix is not square, pad it to make it square
    n_rows, n_cols = matrix.shape
    if n_rows != n_cols:
        max_dim = max(n_rows, n_cols)
        padded_matrix = np.zeros((max_dim, max_dim))
        padded_matrix[:n_rows, :n_cols] = matrix
        
        if maximize:
            padded_matrix[n_rows:, :] = 0
            padded_matrix[:, n_cols:] = 0
        else:
            padded_matrix[n_rows:, :] = matrix.max() + 1
            padded_matrix[:, n_cols:] = matrix.max() + 1
        
        matrix = padded_matrix
    
    # Solve the assignment problem
    row_ind, col_ind = linear_sum_assignment(matrix)
    
    return row_ind, col_ind

# Testing purposes
# run solver.py to solve
csv_file = "txrd2_sponsors.csv"
df = pd.read_csv(csv_file, index_col=0, comment='#')
matrix = df.values
row_headers = df.index.to_numpy()
column_headers = df.columns.to_numpy()

row_ind, col_ind = solve_hungarian(matrix, maximize=True)

print(f"Optimal assignment: ")
optimal_list = []
optimal_value = 0
for row, col in zip(row_ind, col_ind):
    if row >= len(row_headers) or col >= len(column_headers):
        continue
    optimal_list.append([row, col])
    optimal_list.sort(key=lambda x: x[1])
    if row < len(row_headers):
        optimal_value = optimal_value + int(matrix[row][col])

for li in optimal_list:
    print(f"{column_headers[li[1]]} -> {row_headers[li[0]]}")
print(f"Optimal value: {optimal_value}")