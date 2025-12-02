# p1_Search.py
# ---------
# Based on search.py from the UC Berkeley Pacman AI Projects.
# Original authors: John DeNero, Dan Klein, Brad Miller, Nick Hay, Pieter Abbeel.
# Original project link: http://ai.berkeley.edu
#
# Modifications for UCI EECS 118 by Mahmoud Elfar, 2025.
# This version includes changes to <TBD>.
#
# Licensing: You may use or extend this file for educational purposes
# provided that (1) solutions are not distributed or published,
# (2) this notice is retained, and (3) clear attribution to UC Berkeley is kept.


"""
In p1_Search.py, you will implement generic search algorithms which are called by
Pacman agents (in p1_SearchAgents.py).
"""

import util
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def cornersHeuristic(state, problem: SearchProblem) -> float:
    """Heuristic for the CornersProblem."""
    position, visited = state
    unvisited_corners = [corner for i, corner in enumerate(problem.corners) if not visited[i]]
    heuristic = 0
    current_position = position
    while unvisited_corners:
        distances = [(util.manhattanDistance(current_position, corner), corner) for corner in unvisited_corners]
        min_distance, closest_corner = min(distances)
        heuristic += min_distance
        current_position = closest_corner
        unvisited_corners.remove(closest_corner)
    return heuristic


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start_State=problem.getStartState()
    visited=set()
    stack=util.Stack()
    stack.push((start_State,[]))
    while not stack.isEmpty():
        current_State,actions=stack.pop()
        if problem.isGoalState(current_State):
            return actions
        if current_State not in visited:
            visited.add(current_State)
            for successor,action,stepCost in problem.getSuccessors(current_State):
                new_Actions=actions+[action]
                stack.push((successor,new_Actions))
    # util.raiseNotDefined()
    
                    

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    start_State=problem.getStartState()
    visited=set()
    queue=util.Queue()
    queue.push((start_State,[]))
    while not queue.isEmpty():
        current_State,actions=queue.pop()
        if problem.isGoalState(current_State):
            return actions
        if current_State not in visited:
            visited.add(current_State)
            for successor,action,stepCost in problem.getSuccessors(current_State):
                new_Actions=actions+[action]
                queue.push((successor,new_Actions))

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start_State=problem.getStartState()
    visited=set()
    priority_Queue=util.PriorityQueue()
    priority_Queue.push((start_State,[]),0)
    while not priority_Queue.isEmpty():
        current_State,actions=priority_Queue.pop()
        if problem.isGoalState(current_State):
            return actions
        if current_State not in visited:
            visited.add(current_State)
            for successor,action,stepCost in problem.getSuccessors(current_State):
                new_Actions=actions+[action]
                cost=problem.getCostOfActions(new_Actions)
                priority_Queue.push((successor,new_Actions),cost)


    # util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print("A* Search heuristic:", heuristic)
    start_State=problem.getStartState()
    visited=set()
    priority_Queue=util.PriorityQueue()
    priority_Queue.push((start_State,[]),0)
    while not priority_Queue.isEmpty():
        current_State,actions=priority_Queue.pop()
        if problem.isGoalState(current_State):
            return actions
        if current_State not in visited:
            visited.add(current_State)
            for successor,action,stepCost in problem.getSuccessors(current_State):
                new_Actions=actions+[action]
                cost=problem.getCostOfActions(new_Actions)+heuristic(successor,problem)
                # print("cost",cost)
                priority_Queue.push((successor,new_Actions),cost)

    # util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
