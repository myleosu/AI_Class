# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


class ChildNode:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    expanded_node = {}
    dfs_stack = util.Stack()
    dfs_stack.push(ChildNode(problem.getStartState(), None, None, 0))
    result_path = []
    while dfs_stack.isEmpty() is False:
        cur_node = dfs_stack.pop()
        if problem.isGoalState(cur_node.state) is True:
            result_path = []
            while cur_node.action is not None:
                result_path.append(cur_node.action)
                cur_node = cur_node.parent
            result_path.reverse()
            return result_path
        if cur_node.state not in expanded_node.keys():
            child_node_list = problem.expand(cur_node.state)
            expanded_node[cur_node.state] = None
            for child_node in child_node_list:
                dfs_stack.push(ChildNode(child_node[0], cur_node, child_node[1], cur_node[2]))
    return result_path
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    expanded_node = {}
    bfs_queue = util.Queue()
    bfs_queue.push(ChildNode(problem.getStartState(), None, None, 0))
    result_path = []
    while bfs_queue.isEmpty() is False:
        cur_node = bfs_queue.pop()
        if problem.isGoalState(cur_node.state) is True:
            result_path = []
            while cur_node.action is not None:
                result_path.append(cur_node.action)
                cur_node = cur_node.parent
            result_path.reverse()
            return result_path
        if cur_node.state not in expanded_node.keys():
            child_node_list = problem.expand(cur_node.state)
            expanded_node[cur_node.state] = None
            for child_node in child_node_list:
                bfs_queue.push(ChildNode(child_node[0], cur_node, child_node[1], cur_node[2]))
    return result_path
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    expanded_node = {}
    astar_priqueue = util.PriorityQueue()
    astar_priqueue.update(ChildNode(problem.getStartState(), None, None, 0), heuristic(problem.getStartState(), problem))
    result_path = []
    while astar_priqueue.isEmpty() is False:
        cur_node = astar_priqueue.pop()
        if problem.isGoalState(cur_node.state) is True:
            result_path = []
            while cur_node.action is not None:
                result_path.append(cur_node.action)
                cur_node = cur_node.parent
            result_path.reverse()
            return result_path
        if cur_node.state not in expanded_node.keys():
            child_node_list = problem.expand(cur_node.state)
            expanded_node[cur_node.state] = None
            for child_node in child_node_list:
                # print(heuristic(child_node[0], problem))
                astar_priqueue.update(ChildNode(child_node[0], cur_node, child_node[1], child_node[2] + cur_node.cost), child_node[2] + cur_node.cost + heuristic(child_node[0], problem))
    return result_path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
