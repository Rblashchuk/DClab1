def solve_exp(line):
    return eval(line)


def file_to_exps(filepath):
    file = open(filepath, 'r')
    ans = []
    for line in file:
        ans.append(line.rstrip())
    file.close()
    return ans


def solve_exps(exps):
    ans = []
    for exp in exps:
        ans.append(solve_exp(exp))
    return ans


def ans_to_file(ans, exps, filepath):
    file = open(filepath, 'w')
    for i, exp in enumerate(exps):
        file.write('{}) {} = {};\n'.format(i + 1, exp, ans[i]))
    file.close()
    return 0


def get_exps_filepath():
    print('please input a path to input file')
    ans = str(input())
    return ans


def get_ans_filepath():
    print('please input a path to output file')
    ans = str(input())
    return ans


if __name__ == '__main__':
    fr = get_exps_filepath()
    fw = get_ans_filepath()
    exps = file_to_exps(fr)
    ans = solve_exps(exps)
    ans_to_file(ans, exps, fw)
