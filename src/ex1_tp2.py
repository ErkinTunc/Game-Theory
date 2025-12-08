# Soient A et B les matrices de gain des joueurs I et II


def Stategy_Pures(A): # A est le matrice des gains du joueur I | A_ij
    """Détermine si le jeu admet une valeur en stratégies pures et retourne cette valeur si elle existe."""
    strategies_I = len(A)       # i
    strategies_II = len(A[0])   # j   
    
    # v^- = max min aij
    min_lignes = [min(A[i]) for i in range(strategies_I)]
    v_moins = max(min_lignes)
    
    # v^+ = min max aij
    max_colonnes = [max(A[i][j] for i in range(strategies_I)) for j in range(strategies_II)]
    v_plus = min(max_colonnes)
    
    if v_moins == v_plus:
        print("Le jeu admet une valeur en straties pures v = ", v_moins)
        return v_moins
    else:
        print("Le jeu n'admet pas de valeur en strategies pures")
        return None
    
if __name__ == "__main__":
    print("Exemple 1:")
    A1 = [[1, -2, 3],
          [-1, 4, 5],
          [2, 1, 6]]
    Stategy_Pures(A1)