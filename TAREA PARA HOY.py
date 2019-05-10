def multiplicacion(a,b,fila,columna,resultadop,m,r):
    if fila == len(a):
        return m
    elif columna == len(a[0]):
        return multiplicacion(a,b,fila+1,0,0,m,0)
    elif resultadop == len(a[0]):
        m[fila][columna] = r
        return multiplicacion(a, b, fila, columna+1, 0, m, 0)
    else:
        r += a[fila][resultadop]*b[resultadop][columna]
        resultadop+=1
        return multiplicacion(a, b, fila, columna, resultadop, m, r)

a = [[1,2],[1,3]]
b = [[1,2],[3,1]]
m = [[0, 0], [0, 0]]
c = multiplicacion(a,b,0,0,0,m,0)
print (c)


