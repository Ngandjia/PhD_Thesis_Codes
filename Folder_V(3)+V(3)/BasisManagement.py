# We import the SageMath library into Python
from sage.all import ideal

class BasisHandler:

    def __init__(self, I):
        # We initialize the class with an ideal I
        self.I = I
        self.G = self.I.groebner_basis()  # We compute the Gröbner basis

    def count_degrees(self, Generators) :
        """
        Method to count the degree occurrences in the basis.
        """
        d = {}
        for element in Generators:
            degree_label = f"Deg {element.degree()}"
            if degree_label in d.keys():
                d[degree_label] += 1
            else:
                d[degree_label] = 1
        return (d)
    
    def degree_per_binary(self, GeneratorsT) :
        """
        Method to count for each V(n) the degree occurrences in the basis.
        """
        d = {}
        for element in GeneratorsT :
            if f"degree {element[0].degree()} in {element[1]}" in d.keys() :
                d[f"degree {element[0].degree()} in {element[1]}"] += 1
            else :
                d[f"degree {element[0].degree()} in {element[1]}"] = 1
        for key, value in d.items() :
            print(f"{key} : {value}")

    def optimize_basis(self, G, T=None):
        """
        Method to minimize the basis by removing redundant elements.
        """
        import time
        if T == None :
            H = [element for element in G]  # We copy of Gröbner basis
            G = [element for element in G]  # We copy of Gröbner basis for modification
            start = time.time()  # We start time tracking using SageMath's cputime()
            for element in H:
                G_saved = [element for element in G]  # We backup the current Gröbner basis
                G.remove(element)  # We remove the current element

                # We check if the reduced Gröbner basis still generates the same ideal
                if ideal(G) == self.I:
                    continue  # If the reduced set is still the same ideal, skip
                else:
                    G = [element for element in G_saved]  # We restore the original Gröbner basis if necessary
            end = time.time()  # End time tracking

            print(f"Number of elements in minimized Gröbner basis : {len(G)}")
            print(f"The minimized Gröbner basis generates the ideal : {ideal(G) == self.I}")
            print(f"\nDone in {round(end - start, 2)} seconds\n")
            return (G)
        else :
            H = [element for element in T]
            T0 = [element[0] for element in T]
            start = time.time()
            for element in H :
                T0_saved = [element for element in T0]
                T_saved = [element for element in T]
                T.remove(element)
                T0.remove(element[0])
                if ideal(T0) == ideal(self.I) :
                    continue
                else :
                    T0 = [element for element in T0_saved]
                    T = [element for element in T_saved]
            end = time.time()

            print(f"Number of elements in minimized generating set : {len(T)}")
            print(f"The minimized basis generates the ideal : {ideal(T0) == self.I}")
            print(f"\nDone in {round(end - start, 2)} seconds\n")
            return (T0, T)    