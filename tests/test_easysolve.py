from main import solve_exp


def test_easysolve1():
    answer = solve_exp('2+3')
    assert answer == 5


def test_easysolve2():
    answer = solve_exp('3*5')
    assert answer == 15


def test_easysolve3():
    answer = solve_exp('7**2')
    assert answer == 49
