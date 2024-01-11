# We denote by [b,l,w] the number of sequences x_1 >= x_2 >= ... >= x_l of nonnegative integers such that :
# b >= x_1 and sum(x_i)=w.

# We compute the number [b,l,w] for b=0.

def f0(l,w) :
    if w != 0 or l == 0:
        result = 0
    else :
        result = 1
    return(result)

# We compute the number [b,l,w] for b=1.

def f1(l,w) :
    if int(w) != w or w < 0 :
        result = 0
    elif l == 0 :
        result = 0
    elif l != 0 and w == 0 :
        result = 1
    elif l == 1 and  w != 0 :
        if w > 1 :
            result = 0
        else :
            result = 1
    else :
        result = f1(l-1,w-1)
    return(result)

# We compute the number [b,l,w] for b=2.

def f2(l,w) :
    if int(w) != w or w < 0 :
        result = 0
    elif l == 0 :
        result = 0
    elif l != 0 and w == 0 :
        result = 1
    elif l == 1 and  w != 0 :
        if w > 2 :
            result = 0
        else :
            result = 1
    else :
        result = f2(l-1,w-2) + f1(l-1,w-1)
    return(result)

# We compute the number [b,l,w] for b=3.

def f3(l,w) :
    if int(w) != w or w < 0 :
        result = 0
    elif l == 0 :
        result = 0
    elif l != 0 and w == 0 :
        result = 1
    elif l == 1 and  w != 0 :
        if w > 3 :
            result = 0
        else :
            result = 1
    else :
        result = f3(l-1,w-3) + f2(l-1,w-2) + f1(l-1,w-1)
    return(result)

# We compute the number [b,l,w] for b=4.

def f4(l,w) :
    if int(w) != w or w < 0 :
        result = 0
    elif l == 0 :
        result = 0
    elif l != 0 and w == 0 :
        result = 1
    elif l == 1 and  w != 0 :
        if w > 4 :
            result = 0
        else :
            result = 1
    else :
        result = f4(l-1,w-4) + f3(l-1,w-3) + f2(l-1,w-2) + f1(l-1,w-1)
    return(result)

# We compute the number [b,l,w] for b=5.

def f5(l,w) :
    if int(w) != w or w < 0 :
        result = 0
    elif l == 0 :
        result = 0
    elif l != 0 and w == 0 :
        result = 1
    elif l == 1 and  w != 0 :
        if w > 5 :
            result = 0
        else :
            result = 1
    else :
        result = f5(l-1,w-5) + f4(l-1,w-4) + f3(l-1,w-3) + f2(l-1,w-2) + f1(l-1,w-1)
    return(result)

# We compute the multiplicity of V(k) in S^m(V(5)), namely the number :
# M_{m,5,k} = [m,5,(5m-k)/2] - [m,5,(5m-k)/2-1].
# Recall that by Hermite's law of reciprocity, this amounts to computing the number :
# M_{5,m,k} = [5,m,(5m-k)/2] - [5,m,(5m-k)/2-1].

def mult(m,k) :
    x = f5(m,(5 * m - k)/2)
    y = f5(m,(5 * m - k)/2 - 1)
    if m == 0 and k == 0 :
        x,y = 1,0
    return(x - y)

# We compute the decomposition of S^m(V(5)) for every integer m. Output = (subspace : multiplicity).

def decomp(m) :
    result = " "
    for k in range(5 * m + 1) :
        if mult(m,k) == 0 :
            continue
        result = result + " +" + f" {mult(m,k)}*V({k})"
    result = result[4:]
    if k == 0 :
        result = "V(0)"
    return(result)
