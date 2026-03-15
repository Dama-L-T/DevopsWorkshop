import pytest
import sys
sys.path.insert(0, "../app")

from gaussian_eliminate import row_echelon, reduce_row_echelon, extract_sols

def print_mat(matrix):
    for row in matrix:
        for item in row:
            s = f"{item:.2f}"
            print(f"{s:>5}", end=" ")
        print()

@pytest.mark.parametrize(
    "augmented_mat, solution",
    [
        # case 0
        ([
            [5, 6, 7],
            [3, 4, 5],
        ],(-1,2),
        ),

        # case 1
        ([
            [2, -2, 3, 2],
            [1, 2, -1, 3],
            [3, -1, 2, 1],
        ],(-1,4,4)
        ),

        # case 2
        ([
            [2, 4, 6, 22],
            [3, 8, 5, 27],
            [-1, 1, 2, 2],
        ],(3,1,2)
        ),

        # case 3
        ([
            [0, 4, 2, 1],
            [2, 3, 5, 0],
            [3, 1, 1, 11],
        ],(4, 3/2, -5/2)
        ),

        # case 4
        ([
            [3, 6, -9, 15],
            [2, 4, -6, 10],
            [-2, -3, 4, -6],
        ],"infinite"

        # case 5
        ),
        ([
            [1,2,0],
            [1,2,5],
        ],"no solutions"
        ),

    ]
)

def test_solutions(augmented_mat, solution):
    re = row_echelon(augmented_mat)
    print("row echelon form: ")
    print_mat(re)
    rre = reduce_row_echelon(re)
    print("reduce row echelon form: ")
    print_mat(rre)
    results = extract_sols(rre)
    for res, sol in zip(results, solution):
        if isinstance(res, float):
            res = round(res, 5)
        assert res == sol

