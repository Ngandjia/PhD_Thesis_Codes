# We import the SageMath library into Python
from sage.all import PolynomialRing, QQ

# We import some Invariant-theoretical modules
from sage.rings.invariants.invariant_theory import AlgebraicForm, transvectant

# We define the polynomial rings
R = PolynomialRing(QQ, ['a_1', 'a_2', 'a_3', 'a_4', 'b_1', 'b_2', 'b_3', 'b_4', 'x', 'y'], order='degrevlex')
A = PolynomialRing(QQ, ['a_1', 'a_2', 'a_3', 'a_4', 'b_1', 'b_2', 'b_3', 'b_4'], order='degrevlex')

# We extract variables for ease of use
a_1, a_2, a_3, a_4, b_1, b_2, b_3, b_4, x, y = R.gens()

# We define generic algebraic forms
f1 = AlgebraicForm(2, 3, a_1*x**3 + 3*a_2*x**2*y + 3*a_3*x*y**2 + a_4*y**3, x, y)
f2 = AlgebraicForm(2, 3, b_1*x**3 + 3*b_2*x**2*y + 3*b_3*x*y**2 + b_4*y**3, x, y)
c1 = transvectant(f1, f1, 2)
c2 = transvectant(f1, f2, 2)
c3 = transvectant(f2, f2, 2)

# Covariants of order 0 (i.e. invariants)
j2 = transvectant(f1, f2, 3).form()
j41 = transvectant(c1, c1, 2).form() / 2
j42 = transvectant(c3, c3, 2).form() / 2
j43 = transvectant(c1, c3, 2).form() / 2
j44 = transvectant(c1, c2, 2).form()
j45 = transvectant(c3, c2, 2).form()
j6 = transvectant(transvectant(f1, c2, 2), transvectant(f2, c2, 2), 1).form()

# Covariants of order 1 ( in degree 3)
alpha3_1 = transvectant(c1, f2, 2).form() / 2
alpha3_2 = transvectant(c3, f1, 2).form() / 2

# Covariants of order 1 (in degree 5)
alpha5_1 = transvectant(AlgebraicForm(2, 1, alpha3_1, x, y), c1, 1).form()
alpha5_2 = transvectant(AlgebraicForm(2, 1, alpha3_1, x, y), c3, 1).form()
alpha5_3 = transvectant(AlgebraicForm(2, 1, alpha3_2, x, y), c1, 1).form()
alpha5_4 = transvectant(AlgebraicForm(2, 1, alpha3_2, x, y), c3, 1).form()

# Covariants of order 1 (in degree 7)
alpha7_1 = transvectant(AlgebraicForm(2, 1, alpha5_1, x, y), c3, 1).form()
alpha7_2 = 2 * transvectant(AlgebraicForm(2, 1, alpha5_1, x, y), c2, 1).form()
alpha7_3 = transvectant(AlgebraicForm(2, 1, alpha5_2, x, y), c1, 1).form()
alpha7_4 = 2 * transvectant(AlgebraicForm(2, 1, alpha5_2, x, y), c2, 1).form()

# Covariants of order 2 (in degree 2)
beta2_1 = c1.form() / 2
beta2_2 = c2.form()
beta2_3 = c3.form() / 2

# Covariants of order 2 (in degree 4)
beta4_1 = transvectant(c1, c2, 1).form()
beta4_2 = transvectant(c1, c3, 1).form() / 2
beta4_3 = transvectant(c3, c2, 1).form()

# Covariants of order 3 (in degree 1)
gamma1_1 = f1.form()
gamma1_2 = f2.form()

# Covariants of order 3 (in degree 3)
gamma3_1 = transvectant(c1, f1, 1).form()
gamma3_2 = transvectant(c1, f2, 1).form()
gamma3_3 = transvectant(c3, f1, 1).form()
gamma3_4 = transvectant(c3, f2, 1).form()

# Covariants of order 4 (in degree 4)
delta2 = transvectant(f1, f2, 1).form()