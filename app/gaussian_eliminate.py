import copy

def scale_row(row: list[float], factor: float):
    new_list = []
    for item in row:
        new_list.append(item*factor)
    return new_list

def add_row(row1: list[float], row2: list[float]):
    new_list = []
    for i1, i2 in zip(row1, row2):
        new_list.append(i1+i2)
    return new_list

def row_echelon(augmented_matrix: list[list[float]]):
    augmented_matrix = copy.deepcopy(augmented_matrix)
    result = []
    n_vars = len(augmented_matrix[0]) - 1
    n_equations = len(augmented_matrix)
    i = 0 
    while i<n_equations: # go through line by line
        current_eq = augmented_matrix[i]
        for j, reduced_eq in enumerate(result): # reduce line by all previous lines
            coeff = current_eq[j]
            current_eq = add_row(current_eq, scale_row(reduced_eq, -coeff))
        coeff = current_eq[i]
        # print(current_eq)
        if coeff == 0:
            if i+1 == n_equations:
                result.append(current_eq)
                break
            
            augmented_matrix[i+1], augmented_matrix[i] = augmented_matrix[i], augmented_matrix[i+1]
        else:
            i+=1
            result.append(scale_row(current_eq, 1/coeff))
    return result
        
def reduce_row_echelon(row_echelon_matrix: list[list[float]]):
    result = []
    n_equations = len(row_echelon_matrix)
    for i, row in enumerate(row_echelon_matrix[::-1]):
        real_ind = n_equations-i-1
        for j, rre_row in enumerate(result):
            coef = row[n_equations-1-j]
            row = add_row(row, scale_row(rre_row, -coef))
        result.append(row)
    return result[::-1]

# edit this function to account for failed cases
def extract_sols(rre_mat: list[list[float]]):
    sols = []
    for row in rre_mat:
        sols.append(row[-1])
    return sols