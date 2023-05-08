# YC 1-3
from math import *
import fringes
import problems


def find_path(path):
    nav_path = []
    for i in range(0, len(path) - 1):
        if path[i][0] > path[i + 1][0]:
            nav_path.append("N")
        elif path[i][0] < path[i + 1][0]:
            nav_path.append("S")
        elif path[i][1] > path[i + 1][1]:
            nav_path.append("W")
        elif path[i][1] < path[i + 1][1]:
            nav_path.append("E")
    nav_path.append("Stop")
    return nav_path

# YC 1-3 & YC 1-6
def demo_bfs(start, goal, problem) -> list:
    solution = []
    explored = []
    parent = {}
    if start == goal:
        return solution.append("Goal")
    queue = fringes.Queue()
    queue.push(start)
    while (not queue.isEmpty()):
        node = queue.pop()
        explored.append(node)
        for i in problem.successor(node):
            if (i not in explored and not queue.contain(i)):
                parent[i] = node
                if i == goal:
                    path = [i]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    return path[::-1]
                queue.push(i)
    return []


def bfs(problem) -> list:
    total_path = []
    start = problem.get_initial_state()
    if isinstance(problem.get_goal_state(), list):
        total_goal = problem.get_goal_state()
    else:
        total_goal = [problem.get_goal_state()]

    for goal in total_goal:
        if goal not in total_path:
            total_path = total_path + demo_bfs(start, goal, problem)
            if len(total_goal) > 1 and goal != total_goal[-1]:
                start = goal
    total_path = find_path(total_path)
    for i in total_path:
        if i == 'Stop':
            total_path.remove(i)
    total_path.append('Stop')
    return total_path


def demo_dfs(start, goal, problem) -> list:
    solution = []
    explored = []
    parent = {}
    if start == goal:
        return solution.append("Goal")
    stack = fringes.Stack()
    stack.push(start)
    while (not stack.isEmpty()):
        node = stack.pop()
        explored.append(node)
        for i in problem.successor(node):
            if (i not in explored and not stack.contain(i)):
                parent[i] = node
                if i == goal:
                    path = [i]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    return path[::-1]
                stack.push(i)
    return []


def dfs(problem) -> list:
    total_path = []
    start = problem.get_initial_state()
    if isinstance(problem.get_goal_state(), list):
        total_goal = problem.get_goal_state()
    else:
        total_goal = [problem.get_goal_state()]

    for goal in total_goal:
        if goal not in total_path:
            total_path = total_path + demo_dfs(start, goal, problem)
            if len(total_goal) > 1 and goal != total_goal[-1]:
                start = goal
    total_path = find_path(total_path)
    for i in total_path:
        if i == 'Stop':
            total_path.remove(i)
    total_path.append('Stop')
    return total_path


def demo_ucs(start, goal, problem) -> list:
    solution = []
    explored = []
    parent = {}
    if start == goal:
        return solution.append("Goal")
    pqueue = fringes.PriorityQueue()
    pqueue.insert(0, start)
    while (not pqueue.is_empty()):
        cost, node = pqueue.remove()
        explored.append(node)
        for i in problem.successor(node):
            if (i not in explored and not pqueue.contain(i)):
                parent[i] = node
                if i == goal:
                    path = [i]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    return path[::-1]
                pqueue.insert(cost + 1, i)
            elif pqueue.contain(i) and pqueue.getPriority(i) > cost + 1:
                pqueue.updatePriority(i, cost + 1)
    return []


def ucs(problem) -> list:
    total_path = []
    start = problem.get_initial_state()
    if isinstance(problem.get_goal_state(), list):
        total_goal = problem.get_goal_state()
    else:
        total_goal = [problem.get_goal_state()]

    for goal in total_goal:
        if goal not in total_path:
            total_path = total_path + demo_ucs(start, goal, problem)
            if len(total_goal) > 1 and goal != total_goal[-1]:
                start = goal
    total_path = find_path(total_path)
    for i in total_path:
        if i == 'Stop':
            total_path.remove(i)
    total_path.append('Stop')
    return total_path


# YC 2-1
def heuristic_Euclidean(state):
	row_current, col_current = state[0]
	if (isinstance(state[1], list)):
		row_goal, col_goal = state[1][0]
	else:
		row_goal, col_goal = state[1]
	return sqrt((row_goal - row_current) ** 2 + (col_goal - col_current) ** 2)


def heuristic_Manhattan(state):
	row_current, col_current = state[0]
	if (isinstance(state[1], list)):
		row_goal, col_goal = state[1][0]
	else:
		row_goal, col_goal = state[1]
	return abs(row_goal - row_current) + abs(col_goal - col_current)


# YC 2-2
def heuristic_multi(state):
	current, goals = state
	return min(heuristic_Manhattan([current, goal]) for goal in goals)


# YC 2-3 & YC 2-4
def demo_astar(start, goal, problem, fn_heuristic, total_goal) -> list:
	parent = dict({start: None})

	trueCost = dict({start: 0}) # path cost

	explored = set()

	pq = fringes.PriorityQueue()

	pq.insert(0 + fn_heuristic([start, total_goal]), start)

	while pq:
		priority, current = pq.remove()

		explored.add(current)

		if (current == goal):
			total_goal.remove(goal)
			path = [goal]
			while path[-1] != start:
				path.append(parent[path[-1]])
			return path[::-1]

		for successor in problem.successor(current):
			if (successor not in explored and not pq.contain(successor)):
				parent[successor] = current
				trueCost[successor] = trueCost.get(
					parent[successor]) + 1 # g(v) = g(u) + step cost (suppose step cost = 1)
				pq.insert(trueCost[successor] + fn_heuristic(
					[successor, total_goal]), successor)  # true cost (path cost) + heuristic cost
	return []

def astar(problem, fn_heuristic) -> list:
	total_path = []
	start = problem.get_initial_state()
	if isinstance(problem.get_goal_state(), list):  # MultiFood
		total_goal = problem.get_goal_state()
		copy_total_goal = total_goal.copy()
		# Choose the nearest goal base on start position
		while(copy_total_goal):
			goal_chosen = copy_total_goal[0]
			min_h = fn_heuristic([start, [goal_chosen]])
			for goal in copy_total_goal:
				if (min_h > fn_heuristic([start, [goal]])):
					min_h = fn_heuristic([start, [goal]])
					goal_chosen = goal
			total_path += demo_astar(start, goal_chosen, problem, fn_heuristic, copy_total_goal)
			start = goal_chosen
	else:
		goal = problem.get_goal_state()  # SingleFood			
		total_path += demo_astar(start, goal, problem, fn_heuristic, [goal])			
	
	total_path = find_path(total_path)
	for i in total_path:
		if i == 'Stop':
			total_path.remove(i)
	total_path.append('Stop')
	return total_path


# YC2-5
def demo_gbfs(start, goal, problem, fn_heuristic, total_goal) -> list:
	parent = dict({start: None})

	explored = set()

	pq = fringes.PriorityQueue()

	pq.insert(fn_heuristic([start, total_goal]), start)

	while pq:
		priority, current = pq.remove()

		explored.add(current)

		if goal == current:
			total_goal.remove(goal)
			path = [goal]
			while path[-1] != start:
				path.append(parent[path[-1]])
			return path[::-1]

		for successor in problem.successor(current):
			if (successor not in explored and not pq.contain(successor)):
				parent[successor] = current
				pq.insert(fn_heuristic([successor, total_goal]), successor)
	return []


def gbfs(problem, fn_heuristic) -> list:
	total_path = []
	start = problem.get_initial_state()
	if isinstance(problem.get_goal_state(), list):  # MultiFood
		total_goal = problem.get_goal_state()
		copy_total_goal = total_goal.copy()
		# Choose the nearest goal base on start position
		while(copy_total_goal):
			goal_chosen = copy_total_goal[0]
			min_h = fn_heuristic([start, [goal_chosen]])
			for goal in copy_total_goal:
				if (min_h > fn_heuristic([start, [goal]])):
					min_h = fn_heuristic([start, [goal]])
					goal_chosen = goal
			total_path += demo_gbfs(start, goal_chosen, problem, fn_heuristic, copy_total_goal)
			start = goal_chosen
	else:
		goal = problem.get_goal_state()  # SingleFood			
		total_path += demo_gbfs(start, goal, problem, fn_heuristic, [goal])			
	
	total_path = find_path(total_path)
	for i in total_path:
		if i == 'Stop':
			total_path.remove(i)
	total_path.append('Stop')
	return total_path