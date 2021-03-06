import numpy as np

"""
Este programa genera una hélice o espiral de números primos
Generates an helix or spiral of prime numbers
El número dim son las dimensions (dim x dim) y el "pool" de donde se sacan los primos
va hasta el numero dim**3
si quieres generar más primos cambiar primosGenerados a un número mayor
if you want to generate more primes change primosGenerados to a larger value
"""

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction


def spiral(num, dim):
    
    if dim < 1:
        raise ValueError
        
    if dim==2:
        x, y = 0,0
    elif dim%2==0:
        x, y = (dim // 2)-1, (dim // 2)-1 
    else:
        x, y = dim // 2, dim // 2 # start near the center
    dx, dy = NORTH # initial direction
    
    matrix = [[0] * dim for _ in range(dim)]
    ## matrix = np.matrix(np.zeros((width, height), dtype = np.int))

    primos = []

    for primoPosible in range(2, num):

        esPrimo = True
        for i in range(2, primoPosible):
            if primoPosible % i == 0:
                esPrimo = False

        if esPrimo:
            primos.append(primoPosible)

    con = 0
    
    while True:
        
        count = primos[con]
        con += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        
        if (0 <= new_x < dim and matrix[new_y][new_x]==0): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < dim):
                return matrix 

      
dim = int(input("Dame la dimensión de la matriz: "))
primos = np.array(spiral(dim**3, dim))
print(primos)