
import util

class SearchProblem:
    

    def getStartState(self):
        
        util.raiseNotDefined()

    def isGoalState(self, state):
      
        util.raiseNotDefined()

    def getSuccessors(self, state):
       
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
       
        util.raiseNotDefined()


def nullHeuristic(state, problem=None):
  
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    

    result = []
    visited = []

    p_queue = util.PriorityQueue()
    start = (problem.getStartState(), [], 0)
    p_queue.update(start, 0)

    while not p_queue.isEmpty():
        (node, path, cost) = p_queue.pop()
        if problem.isGoalState(node):
            result = path
            break

        if node not in visited:
            visited.append(node)
            for w in problem.getSuccessors(node):
                newPath = path + [w[1]]
                newCost = cost + w[2]
                newNode = (w[0], newPath, newCost)
                p_queue.update(newNode, newCost+heuristic(w[0],problem))

    return result

    util.raiseNotDefined()



astar = aStarSearch
