from main import solve_exp, file_to_exps


def test_empty_exp():
    answer = solve_exp('')
    assert answer


def test_empty_filepath():
    answer = file_to_exps('')
    assert answer
