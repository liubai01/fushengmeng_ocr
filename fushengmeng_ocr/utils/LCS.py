"""
This script provides built-in solution of fitting the name.

For exmaple:

    is_same_name("虎虎", "梦生清闲の虎虎")

"""

def LCS(A, B):
    """
    Solver for LCS(Longest common subseqeunce problem), DP solution
    :param A: string A
    :param B: string B
    :return: the length of LCS
    """
    n = len(A)
    m = len(B)
    if m == 0 or n == 0:
        return -1
    c = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i][j - 1], c[i - 1][j])
    return c[-1][-1]

def is_same_name(A, B):
    """
    Judge whether it is the same name accroding to pre-defined threshold
    :param A: name A (target name)
    :param B: name B (template name)
    :return: Bool(sanity or not), Fitness(the degree of fitting)
    """
    lcs = LCS(A, B)

    fitness = lcs / (len(A) * 0.9 + len(B) * 0.1)
    sanity = lcs / len(A) > 0.5

    # Remark@liubai01: the philosophy behind the formulas is that:
    # (1): template name is redundant, but includes some informative keywors (e.g: 留白 w.r.t. 梦生清闲の留白）
    # (2): if the length of LCS largely matches the target name, then we think it make sense
    # (3): if the length of LCS even perfectly match the template name, then we think it is more advisible

    if sanity:
        return True, fitness
    else:
        return False, fitness

def find_fit_name(name, pool):
    """
    Find the most perferable name in the pool
    :param name: a string, the underlying full name is in pool. （e.g： '随风'）
    :param pool: a list, contains a few list of candidate name. (e.g: ['甲乙', '梦生清闲の随风'，...])
    :return: None if no name make sense. Otherwise, return that name in pool.
    """
    if name is None:
        return None

    if len(name) == 0:
        return None

    max_name = None
    max_fitness = 0

    for to_name in pool:
        flag, fitness = is_same_name(name, to_name)

        if flag:
            if fitness > max_fitness:
                max_fitness = fitness
                max_name = to_name

    return max_name

if __name__ == "__main__":
    print(is_same_name('虎虎', '梦生清闲的虎虎'))
