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

# We compute the multiplicity of V(k) in S^m(V(3)), namely the number :
# M_{m,3,k} = [m,3,(3m-k)/2] - [m,3,(3m-k)/2-1].
# Recall that by Hermite's law of reciprocity, this amounts to computing the number :
# M_{3,m,k} = [3,m,(3m-k)/2] - [3,m,(3m-k)/2-1].

def mult(m,k) :
    x = f3(m,(3 * m - k)/2)
    y = f3(m,(3 * m - k)/2 - 1)
    if m == 0 and k == 0 :
        x,y = 1,0
    return(x - y)

# We compute the decomposition of S^m(V(3)) for every integer m. Output = (subspace : multiplicity).

def decomp(m) :
    result = " "
    for k in range(3 * m + 1) :
        if mult(m,k) == 0 :
            continue
        result = result + " +" + f" {mult(m,k)}*V({k})"
    result = result[4:]
    if k == 0 :
        result = "V(0)"
    return(result)

# We compute the decomposition of the tensor product of V(r) with V(s). Output = (subspace : multiplicity).

def tensor(r,s) :
    r1 = max(r,s)
    s1 = min(r,s)
    r = r1
    s = s1
    d = {}
    for k in range(r-s, r+s+1, 2) :
        d[f"V({k})"] = 1
    return(d)

# We compute the tensor product of S^a(V(3)) with S^b(V(3)). Output = (subspace : multiplicity).

def tensor_sym(a,b) :
    d = {}
    for k_a in range(3*a+1) :
        if mult(a,k_a) == 0 :
            continue
        for k_b in range(3*b+1) :
            if mult(b,k_b) == 0 :
                continue
            for k in range(max(k_a, k_b) - min(k_a, k_b), k_a + k_b + 1, 2) :
                if k in d :
                    d[k] = d[k] + mult(a,k_a)*mult(b,k_b)
                else :
                    d[k] = mult(a,k_a)*mult(b,k_b)
    return(d)

# The following code computes the decomposition of S^n(V(3)+V(3)) for every integer n. Output = (subspace, multiplicity).

def Decomp(n) :
    if n == 0 :
        return("V(0)")
    d = {}
    for a in range(n+1) :
        b = n - a
        d_ab = tensor_sym(a,b)
        for key in d_ab :
            if key in d :
                d[key] = d[key] + d_ab[key]
            else :
                d[key] = d_ab[key]
    result = " "
    for k in range(3 * n + 1) :
        if not(k in d) :
            continue
        result = result + " +" + f" {d[k]}*V({k})"
    result = result[4:]
    return(result)
