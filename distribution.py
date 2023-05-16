import gurobipy
import cvxpy as cp
import numpy as np
from typing import List, Dict

class Distribution:
    def direct2indirect(direct_edge: str) -> str: # convert u3u1 to UNu1u3
        nums = [int(direct_edge[1]), int(direct_edge[3])]
        nums.sort()
        return 'UNu' + str(nums[0]) + 'u' + str(nums[1])


    def __init__(self, external_edges, internal_edges):
        self.external_edges = external_edges
        self.internal_edges = internal_edges
        self.el = len(external_edges)
        self.il = len(internal_edges)
        self.outcomes = []
        self.edge2index = {}
        self.index2edge = {}
        self.edge2outcomes = {} # self.edge2outcomes[edge] is a set of cvxpy variables that have the edge presentnternal_edges)
        
        self.constraints = []

        edges = external_edges + internal_edges

        for i, edge in enumerate(edges):
            self.edge2index[edge] = i
            self.index2edge[i] = edge
            self.edge2outcomes[edge] = set()

        for num in range(2**(self.el + self.il)):
            binary = format(num, '0' + str(self.el + self.il) + 'b')[::-1] # 0 -> 00, 1 -> 10, 2 -> 01, 3 -> 11 if self.l = 1
            outcome = cp.Variable(name=str(binary))
            self.constraints += [outcome >= 0]
            self.constraints += [outcome <= 1]
            self.outcomes.append(outcome)
            for i, c in enumerate(binary):
                edge = self.index2edge[i]
                if c == '1':
                    self.edge2outcomes[edge].add(outcome)

    def __repr__(self):
        output = '--------------------------------------------------\n'
        output += 'Edges: ['
        for edge in self.edge2index.keys():
            output += edge + ', '
        output = output[:-2]
        output += ']\n'
        output += 'Outcomes: ['
        for outcome in self.outcomes:
            output += outcome.name() + ', '
        output = output[:-2]
        output += ']\n\n'
        output += 'Constraints: [\n'
        for constraint in self.constraints:
            output += '    ' + str(constraint) + '\n'
        output = output[:-2]
        output += '\n]\n'
        output += '--------------------------------------------------'
        return output


    def add_constraint(self, requirements: List[Dict[str, List[str]]], target: float):
        flags = [False] * len(self.outcomes)
        for requirement in requirements:
            external_exact = requirement['EE']
            internal_include = requirement['II']
            current_flags = self.__filter(external_exact, internal_include)
            self.__update_flags(flags, current_flags)

        outcomes = []
        for i, outcome in enumerate(self.outcomes):
            if flags[i]:
                outcomes.append(outcome)
        self.constraints += [sum(outcomes) == target]


    def find(self):
        problem = cp.Problem(cp.Minimize(0), self.constraints)
        problem.solve(solver=cp.ECOS, verbose=True)
        # problem.solve(solver=cp.GUROBI, verbose=True)
        print("SOLUTION: ")
        for variable in problem.variables():
            print('    %s = %s' % (variable.name(), variable.value))


    def __filter(self, external_exact: List[str], internal_include: List[str]) -> List[cp.expressions.variable.Variable]:
        '''
        Return a list of outcomes satisfying the present edge and the absent edge requirements
        '''
        external_mask = ['0'] * self.el
        if external_exact is not None:
            for external_edge in external_exact:
                external_mask[self.edge2index[external_edge]] = '1'
        external_mask = ''.join(external_mask)

        current_flags = []
        for outcome in self.outcomes:
            match = external_exact is None or outcome.name()[:self.el] == external_mask # must be exact match for external edges, None means no requirement

            for present_internal_edge in internal_include:
                if outcome not in self.edge2outcomes[present_internal_edge]:
                    match = False
            current_flags.append(match)
            
        return current_flags

    
    def __update_flags(self, flags: List[bool], current_flags: List[bool]):
        for i, current_flag in enumerate(current_flags):
            if current_flag:
                flags[i] = True # once a flag becomes True it stays True