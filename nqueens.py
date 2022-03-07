
# sam flores
# my very cool nqueens code

def is_valid(sol, i):
    for j in range(0, len(sol)):    # loop through elements of current sol
        f = abs((i - sol[j]) / (len(sol) - j))  # analyze slope of queens on board
        if f == 0 or f == 1:    # is it the horizontal or on diagonal
            return False
    return True


def nqueens(n):
    sol = nq_solve([], n)
    return sol


def nq_solve(sol, n):
    if len(sol) == n:
        return sol
    for i in range(0, n):   # check if queen at i solves the problem
        if is_valid(sol, i):    # not in the same row or diagonal
            temp_sol = sol
            sol = nq_solve(sol + [i], n)    # try and solve the rest
            if sol:
                return sol
            else:
                sol = temp_sol
    print(len(sol))
    return False  # tried every i in solver did not work