class SequenceCounter:
    """
    This class computes the number of prescribed sequences and associated multiplicities.
    """
    
    @staticmethod
    def count_sequences(b, l, w):
        """
        Computes the number of sequences x_1 >= x_2 >= ... >= x_l 
        of non-negative integers such that b >= x_1 and x_1 + ... + x_l = w.
        """
        if int(w) != w or w < 0:
            return (0)
        elif l == 0:
            return (0)
        elif l != 0 and w == 0:
            return (1)
        elif l == 1 and w != 0:
            return 1 if w <= b else 0
        else:
            result = 0
            for i in range(1, b + 1):
                result += SequenceCounter.count_sequences(i, l - 1, w - i)
            return (result)

    @staticmethod
    def compute_multiplicity(n, m, k):
        """
        Computes the number M_{m,n,k} = count_sequences(m, n, (nm-k)/2) - count_sequences(m, n, (nm-k)/2-1) 
        which is the multiplicity of V(k) in S^m(V(n)).
        """
        x = SequenceCounter.count_sequences(n, m, (m * n - k) / 2)
        y = SequenceCounter.count_sequences(n, m, (m * n - k) / 2 - 1)
        if m == 0 and k == 0:
            return (1)
        return (x - y)





class DecomposeTensor :
    """
    This class handles decompositions of tensor products of binary forms.
    """

    @staticmethod
    def tensor_product(r, s):
        """
        Computes the tensor product of V(r) with V(s).
        """
        r, s = max(r, s), min(r, s)
        d = {}
        for k in range(r - s, r + s + 1, 2) :
            d[f"V({k})"] = 1
        final = ""
        for key in d.keys() :
            final += f" + {d[key]}*{key}"
        return (final[3:])
        
    @staticmethod
    def tensor_product_symmetric(n1, n2, a, b):
        """
        Computes the tensor product of S^a(V(n1)) with S^b(V(n2)).
        """
        d = {}
        for k_a in range(n1 * a + 1):
            mult_a = SequenceCounter.compute_multiplicity(n1, a, k_a)
            if mult_a == 0:
                continue
            for k_b in range(n2 * b + 1):
                mult_b = SequenceCounter.compute_multiplicity(n2, b, k_b)
                if mult_b == 0:
                    continue
                for k in range(max(k_a, k_b) - min(k_a, k_b), k_a + k_b + 1, 2):
                    if k in d:
                        d[k] += mult_a * mult_b
                    else:
                        d[k] = mult_a * mult_b
        final = " "
        for key in d.keys():
            final += f" + {d[key]}*V({key})"
        return (final[3:], d)
    




class DecomposeSymmetric :
    """
    This class handles decompositions of symmetric powers of binary forms.
    """
    
    @staticmethod
    def decompose_binary(n, m):
        """
        Decomposes S^m(V(n)).
        """
        result = " "
        for k in range(m * n + 1):
            multiplicity = SequenceCounter.compute_multiplicity(n, m, k)
            if multiplicity == 0:
                continue
            result += f" + {multiplicity}*V({k})"
        result = result[4:] if len(result) > 4 else "V(0)"
        return (result)
    
    @staticmethod
    def decompose_binaries(n1, n2, n):
        """
        Computes the decomposition of S^n( V(n1) + V(n2) ).
        """
        if n == 0:
            return ("V(0)")
        d = {}
        for a in range(n + 1):
            b = n - a
            d_ab = DecomposeTensor.tensor_product_symmetric(n1, n2, a, b)[1]
            for key in d_ab:
                if key in d:
                    d[key] += d_ab[key]
                else:
                    d[key] = d_ab[key]
        result = " "
        for k in range(n * n1 + n * n2 + 1):
            if k not in d:
                continue
            result += f" + {d[k]}*V({k})"
        return (result[4:])