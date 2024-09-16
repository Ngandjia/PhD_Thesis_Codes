# We import the SageMath library into Python
from sage.all import factorial

# We import some modules containing differential operators
from DifferentialOperators import Operator

class Weight :

    def nullity(G, suppress_output=False) :
        """
        Compute for each element of G, the maximal wight of all vectors appearing in its decomposition into irreducible elements.
        """
        counter = 0
        L = []
        for f in G :
            h = f
            g = f
            counter += 1
            saved = f
            f = Operator.X(f)
            count = 1
            while f != 0 :
                saved = f
                f = Operator.X(f)
                count += 1
            for lamb in range(66) :
                if Operator.Z(saved) == lamb * saved :
                    L.append(lamb)
                    break
            if suppress_output == False :
                print(f"Element {counter} :\ndegree = {h.degree()}; X^{count}(f) = 0; Z(X^{count-1}(f)) = {lamb} X^{count-1}(f)")
            f = Operator.Y(g)
            count = 1
            while f != 0 :
                f = Operator.Y(f)
                count += 1
            if suppress_output == False :
                print(f"Y^{count}(f) = 0\n")
        if suppress_output == True :
            return (max(L))

    def weights(G) :
        """
        Individual weights.
        """
        m = Weight.nullity(G, True)
        for index, f in enumerate(G) :
            for i in range(-m, m + 1) :
                if Operator.Z(f) == i * f :
                    print(f"Element {index + 1} : {i}")
                    break
    
    def highest_weights(G) :
        """
        Determine the highest weight vectors that determine the remaining vectors of G.
        """
        count = 0
        L = []
        m = Weight.nullity(G, True)
        for index, f in enumerate(G) :
            for i in range(-m, m + 1) :
                if Operator.Z(f) == i * f :
                    if Operator.X(f) == 0 :
                        count += 1
                        L.append([Operator.Ytimes(G[index], j) for j in range(len(G)) if Operator.Ytimes(G[index], j) != 0])
                        print(f"\nElement {index + 1} : {i} -- > This is a highest weight vector!")
                    else :
                        print(f"\nElement {index + 1} : {i}")
        return (L)

    def weight_decomposition(G) :
        """
        Determine for each element of G, its weight decomposition.
        """
        counter = 0

        Total_generators_number = 0
        Total_generators_set = []
        Total_decomposition = {}

        for j in range(0, len(G)) :
            counter += 1
            f = G[j]

            # We compute the (common) weight of all the components of f
            for lamb in range(-66, 66) :
                    if Operator.Z(f) == lamb * f :
                        w = lamb
                        break

            # We compute the smallest integer N, such that X^N(f) = 0.         
            saved = f
            f = Operator.X(f)
            count = 1
            while f != 0 :
                saved = f
                f = Operator.X(f)
                count += 1
            q = count
            q0 = count

            # We compute the weight of the highest weight vector X^(N-1)(f)          
            for lamb in range(66) :
                if Operator.Z(saved) == lamb * saved :
                    N = lamb
                    break

            # We compute the decomposition of f            
            f = G[j]
            dict_confirmation = {}
            dict_components = {}

            for i in range(min(N, w + 2*(q0 - 1)), -1, -2) :
                q = q - 1
                if (i + w)/2 < 0 :
                    break
                    
                num = factorial((i - w)/2) * factorial((i + w)/2 + q)
                den = factorial((i + w)/2) * factorial((i - w)/2 - q)
                coefficient = int(num / den)
                component = Operator.Ytimes(Operator.Xtimes(f, q), q) / coefficient

                if component != 0 :
                    dict_confirmation[f"V({i})"] = 'yes'
                    dict_components[f"V({i})"] = component
                    Total_generators_set.append((component, f"V({i})"))

                f = f - component
                if not(Operator.Z(component) - w * component == Operator.Z(f) - w * f == Operator.Xtimes(f, q) == 0) :
                    print('There is an intellectual or a coding mistake')
                if f == 0 :
                    break
            
            Total_generators_number = Total_generators_number + len(dict_confirmation.keys())
            
            for key, value in dict_confirmation.items() :
                if key in Total_decomposition.keys() :
                    Total_decomposition[key] += 1
                else :
                    Total_decomposition[key] = 1

            # Execution
            print("")
            print(f"Element {counter} : {len(dict_confirmation.keys())} generators")
            print(w, q, N)
            print(dict_confirmation)
            
            s = 0
            for element in dict_components.values() :
                s = s + element
            print(s == G[j])
            print("")

        print("")    
        print("")
        print(f"The total number of generators is {Total_generators_number}")
        print(f"The decomposition is given by :")
        for key, value in Total_decomposition.items() :
            print(f"{key} : {value}")
            
        T = Total_generators_set
        return (T)