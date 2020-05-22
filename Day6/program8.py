def print_spiral(m, n, a):
    k = 0
    l = 0
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''

    while k < m and l < n:
  
        for i in range(l, n):
            print(a[k][i], end=" ")

        k += 1
        print(k)
  
        for i in range(k, m):
            print(a[i][n - 1], end=" ")

        n -= 1
        print(n)
 
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")

            m -= 1
            print(m)

        if l < n:
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1
            print(l)

a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

Row = 3
Columns = 4
print_spiral(Row, Columns, a)
