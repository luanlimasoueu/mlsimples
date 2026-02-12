def validar_tamanhos(X, Y):
    if len(X) != len(Y):
        raise ValueError("X e Y devem ter o mesmo tamanho")
