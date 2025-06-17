import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Problema import PuzzleProblem

def breadthFirstSearch(problem):
    no_inicial = search_tree.getStartNode(problem)

    fronteira = util.Queue()
    fronteira.push (no_inicial)
    visitados = set()

    while not fronteira.isEmpty():
        no_atual = fronteira.pop()

        if no_atual['STATE'] in visitados:
            continue

        visitados.add(no_atual['STATE'])

        if problem.isGoalState(no_atual['STATE']):
            return search_tree.getActionSequence(no_atual)

        for sucessor in problem.expand(no_atual['STATE']):
            no_filho = search_tree.getChildNode(sucessor, no_atual)
            fronteira.push(no_filho)

    return []
