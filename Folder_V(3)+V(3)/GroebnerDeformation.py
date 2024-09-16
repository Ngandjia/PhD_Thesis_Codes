# We import the SageMath library into Python
from sage.all import PolynomialRing, QQ, var, denominator

# We define variables
R1 = PolynomialRing(QQ, ['a_1', 'a_2', 'a_3', 'a_4', 'b_1', 'b_2', 'b_3', 'b_4', 'x', 'y', 't'], order='degrevlex')
a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4, x, y, t = R1.gens()


# In the following, we implement the Gröbner deformation as defined in 
# section 15.8 of the book of Eisenbud (Commutative Algebra, a view towards Algebraic Geometry).
# We choose the degree reverse lexicographic order as the monomial order.


# We define weight constants
lambda_values = [1] * 8 + [0] * 2
lambda1, lambda2, lambda3, lambda4, lambda5, lambda6, lambda7, lambda8, lambda9, lambda10 = lambda_values

# Function f_tilda
def f_tilda(F):
    # We create the tilda version of F
    f_tilda_expr = F(t**(-lambda1)*a_1, t**(-lambda2)*a_2, 
                     t**(-lambda3)*a_3, t**(-lambda4)*a_4,
                     t**(-lambda5)*b_1, t**(-lambda6)*b_2, 
                     t**(-lambda7)*b_3, t**(-lambda8)*b_4,
                     t**(-lambda9)*x, t**(-lambda10)*y)
    
    # We calculate the maximum weight
    max_weight = denominator(f_tilda_expr).degree(t)
    
    if max_weight == 0:
        n = 0
        f = f_tilda_expr.numerator()
        while denominator(f / t) == 1:
            f = f / t
            n += 1
        max_weight = -n

    # We adjust f_tilda with max_weight
    f_tilda_expr = t**max_weight * f_tilda_expr
    f_tilda_expr = f_tilda_expr.numerator()
    
    # We return the evaluated f_tilda expression
    return (f_tilda_expr)

# Function f_limit
def f_limit(F):
    # We create the tilda version of F
    f_tilda_expr = F(t**(-lambda1)*a_1, t**(-lambda2)*a_2, 
                     t**(-lambda3)*a_3, t**(-lambda4)*a_4,
                     t**(-lambda5)*b_1, t**(-lambda6)*b_2, 
                     t**(-lambda7)*b_3, t**(-lambda8)*b_4,
                     t**(-lambda9)*x, t**(-lambda10)*y)

    # We calculate the maximum weight
    max_weight = denominator(f_tilda_expr).degree(t)
    
    if max_weight == 0:
        n = 0
        f = f_tilda_expr.numerator()
        while denominator(f / t) == 1:
            f = f / t
            n += 1
        max_weight = -n

    # We adjust f_tilda with max_weight
    f_tilda_expr = t**max_weight * f_tilda_expr
    f_tilda_expr = f_tilda_expr.numerator()
    
    # We return the limit at t = 0
    return (f_tilda_expr.substitute(t=0))