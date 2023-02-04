from django.shortcuts import render
from django.http.response import JsonResponse


def Home(request):
    return render(request, 'Home.html')


def DynamicProgramming(request):
    try:
        data=request.GET['values']
        data = data.replace(',',"")
        my_list = []
        try:
            for x in data:
                my_list.append(int(x))
        except:
            print('')
        p=my_list
        # print(p)
        m, s = matrix_chain_multiplication(p)
        Minimum_X=m[1][len(p)-1]
        OptiomalOrder=print_optimal_parens(s,1,len(p)-1)
        return JsonResponse({'Minimum_X':Minimum_X, 'OptiomalOrder':OptiomalOrder,'error':''})
    except Exception as e:
        return JsonResponse({'Minimum_X':'', 'OptiomalOrder':'','error':''})


def matrix_chain_multiplication(p):
    # n is the number of matrices
    n = len(p) - 1
    # m is the 2D array that stores the minimum number of multiplications needed
    m = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # s is the 2D array that stores the optimal split point
    s = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                # q is the number of multiplications needed for the current split point
                q = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    # Base case: if i and j are the same, print the matrix
    sequence = ""
    if i == j:
        sequence += "A" + str(i)
    else:
        sequence += "("
        sequence += print_optimal_parens(s, i, s[i][j])
        sequence += print_optimal_parens(s, s[i][j] + 1, j)
        sequence += ")"
    return sequence
