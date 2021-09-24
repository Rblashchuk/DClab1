from main import solve_exp


def test_not_exp1():
    answer = solve_exp('Hello')
    assert answer


def test_not_exp2():
    answer = solve_exp('/"123\n(]*!@')
    assert answer
