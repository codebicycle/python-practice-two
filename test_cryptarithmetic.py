from cryptarithmetic import solve


def test_solve_valid_formula():
    formula = 'ODD + ODD == EVEN'
    result = solve(formula)
    assert result


def test_solve_invalid_formula():
    formula = 'AB / 2 == AB'
    result = solve(formula)
    assert result is None
