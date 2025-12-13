
def pure_nash_equilibria(A, B):
    """
    Returns list of pure Nash equilibria (i, j) with 0-based indices.
    A[i][j] = payoff of player I
    B[i][j] = payoff of player II
    """
    n = len(A)
    m = len(A[0])

    # Best responses of player I to each column j
    br_I = []
    for j in range(m):
        col = [A[i][j] for i in range(n)]
        best = max(col)
        br_I.append({i for i in range(n) if A[i][j] == best})

    # Best responses of player II to each row i
    br_II = []
    for i in range(n):
        row = B[i]
        best = max(row)
        br_II.append({j for j in range(m) if B[i][j] == best})

    # Nash equilibria are intersections
    ne = []
    for i in range(n):
        for j in range(m):
            if i in br_I[j] and j in br_II[i]:
                ne.append((i, j))
    return ne

#------------------------- Test cases -------------------------
if __name__ == "__main__":
    
    # ----------- TD3 - Exercice 1 -----------
    print("Exemple 1:")
    A1 = [  # Player I
        [5.2, 4.4, 4.4],
        [4.2, 4.6, 3.9]
        ]
    B1 = [  # Player II
        [5.0, 4.4, 4.1],
        [4.2, 4.9, 4.3]
    ]
    if pure_nash_equilibria(A1, B1) == []:
        print("No pure Nash equilibria.")
    else:
        print("Pure Nash equilibria:", pure_nash_equilibria(A1, B1))
    
    # ----------- TD3 - Exercice 2 -----------
    print("\nExemple 2:")
    A2 = [  # Player I
        [19,  -42],
        [68,  -45]
    ]
    B2 = [  # Player II
        [19,  68],
        [-42, -45]
    ]
    if pure_nash_equilibria(A2, B2) == []:
        print("No pure Nash equilibria.")
    else:
        print("Pure Nash equilibria:", pure_nash_equilibria(A2, B2))