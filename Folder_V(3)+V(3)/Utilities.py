# In this file we write some useful function for few personalized tasks of interest

# We import the SageMath library into Python
from sage.all import diff, var, expand, solve

# We import the modules containing our covariants and rings.
from Covariants import *

def derivative_x(f, n) :
    for i in range(n) :
        f = diff(f, x)
    return (f)

def derivative_y(f, n) :
    for i in range(n) :
        f = diff(f, y)
    return (f)

def degree_x(covariant) :
    n = 0
    while derivative_x(covariant, n) != 0 :
        n += 1
    return (n - 1)

def member(covariant, I) : 
    n = degree_x(covariant)
    veracity = True
    for i in range(n + 1) :
        veracity = veracity and (derivative_x(derivative_y(covariant, n - i), i) in I)
    return (veracity)

def to_ideal(L) :
    I = A.ideal(0)
    for covariant in L :
        n = degree_x(covariant)
        for i in range(n + 1) :
            I = I + A.ideal(derivative_x(derivative_y(covariant, i), n - i))
    return (I)

L_math = [j2,j41,j42,j43,j44,j45,j6,alpha3_1,alpha3_2,alpha5_1,alpha5_2,alpha5_3,alpha5_4,alpha7_1,alpha7_2,alpha7_3,alpha7_4,beta2_1,beta2_2,beta2_3,beta4_1,beta4_2,beta4_3,gamma1_1,gamma1_2,gamma3_1,gamma3_2,gamma3_3,gamma3_4,delta2]
L_greek = ['j2','j41','j42','j43','j44','j45','j6','alpha3_1','alpha3_2','alpha5_1','alpha5_2','alpha5_3','alpha5_4','alpha7_1','alpha7_2','alpha7_3','alpha7_4','beta2_1','beta2_2','beta2_3','beta4_1','beta4_2','beta4_3','gamma1_1','gamma1_2','gamma3_1','gamma3_2','gamma3_3','gamma3_4','delta2']

def p(E, k):
    if k == 0:
        return([set([])])
    elif k == 1:
        return([set([x]) for x in E])
    else:
        retro = p(E, k - 1)
        final = []
        for x in E:
            for subset in retro:
                if not(x in subset):
                    subset = subset.union(set([x]))
                    if not(subset in final):
                        final.append(subset)
    return (final)

def P(E):
    final = []
    final.append(set({}))
    for k in range(1, len(E) + 1):
        final.extend(p(E, k))
    return (final)

def check(liste):
    veracity = True
    for index, element in enumerate(liste):
        veracity = veracity and (element == f'l_{index + 1} == 0')
        if veracity == False:
            return(veracity)
            break
    return (veracity)

def choices(c_math, d, c_greek, k) :
    final_math = []
    final_greek = []

    for subset in p(c_math, k) :  
        subset = list(subset)  
        n = degree_x(subset[0])
        l = [var(f'l_{i}') for i in range(1, len(subset) + 1)]
        poly = expand(sum([l[i] * subset[i] for i in range(len(subset))]))  
        L = []
        for i in range(n + 1) :
            for i1 in range(d + 1) :
                for i2 in range(d + 1) :
                    for i3 in range(d + 1) :
                        for i4 in range(d + 1) :
                            for j1 in range(d + 1) :
                                for k2 in range(d + 1) :
                                    for j3 in range(d + 1) :
                                        for j4 in range(d + 1) :
                                            if i1+i2+i3+i4+j1+k2+j3+j4 == d :
                                                monomial = a_1**i1*a_2**i2*a_3**i3*a_4**i4*b_1**j1*b_2**k2*b_3**j3*b_4**j4*x**i*y**(n - i)
                                                if poly.coefficient(monomial) != 0 :
                                                    L.append(poly.coefficient(monomial) == 0)
                                                
        solution = solve(L, l)
        solution = str(solution)[3:-3].split(',')
        solution = [element.lstrip() for element in solution]

        if check(solution) :
            final_math.append(subset)
            subset_greek = []
            for covariant in subset :
                subset_greek.append(c_greek[c_math.index(covariant)])            
            final_greek.append(subset_greek)
    return (final_math, final_greek)

def display_belong(I) :
    L1 = [element for element in L_math]
    L2 = [element for element in L_greek]
    waste = []
    for index1, covariant1 in enumerate(L1) :
        if covariant1 in waste :
            continue
        element1 = L2[index1]
        if member(covariant1, I) == True :
            print(f"{element1}")
            waste.append(covariant1)
            continue
            
        for index2, covariant2 in enumerate(L1) :
            if (covariant2 in waste) or (member(covariant2, I) == True) :
                continue
            if covariant1 * covariant2 in waste :
                continue
            element2 = L2[index2]
            if member(covariant1 * covariant2, I) == True :
                print(f"{element1} * {element2}")
                waste.append(covariant1 * covariant2)
                continue

            for index3, covariant3 in enumerate(L1) :
                if (covariant3 in waste) or (member(covariant3, I) == True):
                    continue
                if (covariant3 * covariant1 in waste) or (member(covariant3 * covariant1, I) == True) :
                    continue
                if (covariant3 * covariant2 in waste) or (member(covariant3 * covariant2, I) == True) : 
                    continue
                if covariant1 * covariant2 * covariant3 in waste :
                    continue
                element3 = L2[index3]
                if member(covariant1 * covariant2 * covariant3, I) == True :
                    print(f"{element1} * {element2} * {element3}")
                    waste.append(covariant1 * covariant2 * covariant3)