from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

pwdRange = inputFile.readline().split('-')
cnt = 0
pwd = int(pwdRange[0])


def test(num: int) -> int:
    i = 1
    adjacent_duplicate = 0

    while i <= len(str(num)) - 1:
        curr = int_pos(num, i)
        prev = int_pos(num, i-1)

        if curr >= prev:
            if curr == prev:
                adjacent_duplicate += 1
            i += 1
        else:
            return 0

    return 1 if adjacent_duplicate > 0 else 0


def int_pos(num, pos):
    return int(str(num)[pos])


while pwd <= int(pwdRange[1]):
    if test(pwd):
        cnt += 1

    pwd += 1

# --- solution ---

iohandler.end(str(cnt))
