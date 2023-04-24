def compound_interest(p, r, t):
    A = p
    for i in range(t):
        A = A * (1 + r/100)
    CI = A - p
    print("Compound interest is", CI)

compound_interest(10000, 10.2, 5)