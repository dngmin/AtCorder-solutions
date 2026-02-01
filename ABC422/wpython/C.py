T = int(input())
testcases = [list(map(int,input().split())) for _ in range(T)]

for testcase in testcases:
    contest = 0
    na, nb, nc = testcase
    min_abc = min(testcase)

    if min_abc == nb and min_abc not in (na, nc):
        contest = nb
        na -= nb
        nc -= nb

        if na != nc:
            diff = abs(na - nc)
            min_acd = min([na, nc, diff])
            if min_acd == diff:
                if na > nc:
                    na -= 2*diff
                    nc -= diff
                    contest += diff
                else:
                    na -= diff
                    nc -= 2*diff
                    contest += diff
            else:
                contest += min_acd

        if na == nc:
            contest += (na//3)*2 +1 if na%3 == 2 else (na//3)*2

    else:
        contest = min([na,nc])

    print(contest)