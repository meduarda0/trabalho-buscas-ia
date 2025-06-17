def iterativeDeepeningSearch(problem):
    profundidade = 0
    while True:
        resultado = depthLimitedSearch(problem, profundidade)
        if resultado != 'cutoff':
            return resultado
        profundidade += 1
