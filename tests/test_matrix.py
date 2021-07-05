from lesson2.homework import Matrix
import pytest


@pytest.mark.parametrize("matrix_1, matrix_2, matrix_result", [
    ([[1, 1]], [[1, 1]], '2 2 \n'),
    ([[1, 1]], [[2, 2]], '3 3 \n'),
    ([[1, 1]], [[3, 3]], '4 4 \n'),
])
def test_add_matrix(matrix_1, matrix_2, matrix_result):
    res = Matrix(matrix_1) + Matrix(matrix_2)
    assert res.__str__() == matrix_result


@pytest.mark.parametrize("matrix_1, matrix_2, matrix_result", [
    ([[1, 1]], [[1, 1]], '0 0 \n'),
    ([[2, 2]], [[1, 1]], '1 1 \n'),
    ([[3, 3]], [[1, 1]], '2 2 \n'),
])
def test_sub_matrix(matrix_1, matrix_2, matrix_result):
    res = Matrix(matrix_1) - Matrix(matrix_2)
    assert res.__str__() == matrix_result


@pytest.mark.parametrize("matrix_1, number, matrix_result", [
    ([[1, 1]], 2, '2 2 \n'),
    ([[2, 2]], 2, '4 4 \n'),
    ([[3, 4]], 2, '6 8 \n'),
])
def test_multiple_matrix(matrix_1, number, matrix_result):
    res = Matrix(matrix_1) * number
    assert res.__str__() == matrix_result


@pytest.mark.parametrize("matrix_1, number, matrix_result", [
    ([[2, 6]], 2, '1.0 3.0 \n'),
    ([[2, 2]], 2, '1.0 1.0 \n'),
    ([[8, 10]], 2, '4.0 5.0 \n'),
])
def test_div_matrix(matrix_1, number, matrix_result):
    res = Matrix(matrix_1) / number
    assert res.__str__() == matrix_result


@pytest.mark.parametrize("exc_type, matrix_1, number", [
    (ZeroDivisionError, [[2, 6]], 0),
    (TypeError, '[[2, 2]]', 0),
    (ZeroDivisionError, [[8, 10]], 0),
])
def test_div_matrix_with_error(exc_type, matrix_1, number):
    with pytest.raises(exc_type):
        Matrix(matrix_1) / number
