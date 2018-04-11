import null as null
from Model.State import State
import numpy as np

class Node:
    UCTValue = 0.0
    N = 0 #number of simulations
    Q = 0 #number of wins
    C = 1 #weightage given to exploration

    def __init__(self,state):
        self.state = state

    def UCTUpdate(self):
        return (self.Q / self.N) + self.C * np.sqrt(np.log(self.N) / self.N)

    def getState(self):
        return self.state
