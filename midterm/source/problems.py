from typing import *
import os
from copy import *


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# YC1-1
class SingleFoodSearchProblem:
    def __init__(self, filepath):
        self.matrix = SingleFoodSearchProblem.read_maze(filepath)
        self.initial_state = SingleFoodSearchProblem.get_initial_state(self)
        self.goal_state = SingleFoodSearchProblem.get_goal_state(self)

    def successor(self, state: tuple[int, int]):
        successors = []
        row, col = state

        if self.matrix[row + 1][col] != "%":
            successors.append((row + 1, col))  # up
        if self.matrix[row - 1][col] != "%":
            successors.append((row - 1, col))  # down
        if self.matrix[row][col + 1] != "%":
            successors.append((row, col + 1))  # right
        if self.matrix[row][col - 1] != "%":
            successors.append((row, col - 1))  # left

        return successors

    def goal_test(self, state: tuple[int, int]):
        return state == self.goal_state

    def path_cost(self, path: list):
        return len(path) - 1

    def read_maze(filepath):
        f = open(filepath, "r")
        matrix = []
        while (line := f.readline()):
            row = []
            for char in line:
                row.append(char)
            matrix.append(row)
        f.close()
        return matrix

    def print_maze(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end="")
        print()

    def get_initial_state(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j] == 'P'):
                    return (i, j)

    def get_goal_state(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j] == '.'):
                    return (i, j)

    def print_initial_state(self):
        print(self.initial_state)

    def print_goal_state(self):
        print(self.goal_state)

# YC1-4
    def animate(self, actions) -> None:
        clear_console()
        self.print_maze()
        self.print_initial_state()
        self.print_goal_state()

        copy_matrix = deepcopy(self.matrix)
        copy_initial_state = deepcopy(list(self.initial_state))

        for action in actions:
            if (action == "Stop"):
                return None
            row, col = copy_initial_state
            enter = input()
            if (enter == ''):
                if (action == "N"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row - 1, col]
                    copy_matrix[row - 1][col] = 'P'
                elif (action == "S"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row + 1, col]
                    copy_matrix[row + 1][col] = 'P'
                elif (action == "W"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row, col - 1]
                    copy_matrix[row][col - 1] = 'P'
                elif (action == "E"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row, col + 1]
                    copy_matrix[row][col + 1] = 'P'

                copy_initial_state = tuple(copy_initial_state)

                clear_console()

                # Print maze
                for i in range(0, len(copy_matrix)):
                    for j in range(0, len(copy_matrix[i])):
                        print(copy_matrix[i][j], end="")
                print()

                print(copy_initial_state)
                self.print_goal_state()

        return None


# YC 1-5
class MultiFoodSearchProblem:
    def __init__(self, filepath):
        self.matrix = MultiFoodSearchProblem.read_maze(filepath)
        self.initial_state = MultiFoodSearchProblem.get_initial_state(self)
        self.goal_state = MultiFoodSearchProblem.get_goal_state(self)

    def successor(self, state: tuple[int, int]):
        successors = []
        row, col = state

        if self.matrix[row + 1][col] != "%":
            successors.append((row + 1, col))  # up
        if self.matrix[row - 1][col] != "%":
            successors.append((row - 1, col))  # down
        if self.matrix[row][col + 1] != "%":
            successors.append((row, col + 1))  # right
        if self.matrix[row][col - 1] != "%":
            successors.append((row, col - 1))  # left

        return successors

    def goal_test(self, state: tuple[int, int]):
        return state in self.goal_state

    def path_cost(self, path: list):
        return len(path) - 1

    def read_maze(filepath):
        f = open(filepath, "r")
        matrix = []
        while (line := f.readline()):
            row = []
            for char in line:
                row.append(char)
            matrix.append(row)
        f.close()
        return matrix

    def print_maze(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end="")
        print()

    def get_initial_state(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j] == 'P'):
                    return (i, j)

    def get_goal_state(self):
        is_goal = []
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if (self.matrix[i][j] == '.'):
                    is_goal.append((i, j))
        return is_goal

    def print_initial_state(self):
        print(self.initial_state)

    def print_goal_state(self):
        print(self.goal_state)

    def animate(self, actions) -> None:
        clear_console()
        self.print_maze()
        self.print_initial_state()
        self.print_goal_state()

        copy_matrix = deepcopy(self.matrix)
        copy_initial_state = deepcopy(list(self.initial_state))

        for action in actions:
            if (action == "Stop"):
                return None
            row, col = copy_initial_state
            enter = input()
            if (enter == ''):
                if (action == "N"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row - 1, col]
                    copy_matrix[row - 1][col] = 'P'
                elif (action == "S"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row + 1, col]
                    copy_matrix[row + 1][col] = 'P'
                elif (action == "W"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row, col - 1]
                    copy_matrix[row][col - 1] = 'P'
                elif (action == "E"):
                    copy_matrix[row][col] = ' '
                    copy_initial_state = [row, col + 1]
                    copy_matrix[row][col + 1] = 'P'

                copy_initial_state = tuple(copy_initial_state)

                clear_console()

                # Print maze
                for i in range(0, len(copy_matrix)):
                    for j in range(0, len(copy_matrix[i])):
                        print(copy_matrix[i][j], end="")
                print()

                print(copy_initial_state)
                self.print_goal_state()

        return None


# YC 3-1
class EightQueenProblem:
    def __init__(self, file_path):
        self.matrix = EightQueenProblem.read_matrix(file_path)
        self.h = self.heuristic(self.matrix)

    def read_matrix(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matrix = []
            for line in lines:
                row = []
                for x in line:
                    if x != " " and x != '\n':
                        row.append(x)
                matrix.append(row)
        return matrix

    def print_matrix(self, matrix):
        number = 1
        for i in range(len(matrix)):
            for j in range(0, len(matrix[i])):
                if len(matrix[i][j]) > 1:
                    number = 2
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '\n':
                    continue
                if number == 1:
                    print(matrix[i][j] + " ", end="")
                else:
                    if len(matrix[i][j]) == 2:
                        print(matrix[i][j] + " ", end="")
                    else:
                        print(matrix[i][j] + "  ", end="")
            print()

    # Function below using for counting the number Queen attack together
    def heuristic(self, matrix):
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "Q":
                    for m in range(j + 1, len(matrix[i])):
                        if matrix[i][m] == "Q":
                            count += 1
                    l = i  # k, l use for index from top to right to bottom
                    k = j  # o, p use for index from top to left to bottom
                    o = i
                    p = j
                    while o <= len(matrix[i]) - 2 and p > 0:
                        o += 1
                        p -= 1
                        if matrix[o][p] == "Q":
                            count += 1
                    while l <= len(matrix[i]) - 2 and k <= len(matrix[i]) - 2:
                        l += 1
                        k += 1
                        if matrix[l][k] == "Q":
                            count += 1
        return count

# YC 3-2
    def hill_climbing_search(self):
        current_state = self.matrix
        current_h = self.heuristic(current_state)

        while True:
            best_h = current_h
            best_state = current_state
            for i in range(len(current_state)):
                for j in range(len(current_state)):

                    if current_state[j][i] == "Q":
                        for k in range(len(current_state)):
                            if k != j:
                                neighbor_state = deepcopy(current_state)
                                neighbor_state[k][i] = "Q"
                                neighbor_state[j][i] = "0"
                                neighbor_h = self.heuristic(neighbor_state)
                            if neighbor_h < best_h:
                                best_h = neighbor_h
                                best_state = neighbor_state
            if best_h >= current_h:
                return current_state
            current_state = best_state
            current_h = best_h
