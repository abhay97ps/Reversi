from Bot.Node import Node
import time as Time


def MCUCT(state, turn):
    node = Node(state, turn)
    i = 0
    while i < 100:  # define criteria as req
        n = TreePolicy(node)  # select based on best UCT or expand if more nodes are left unexplored
        reward = Simulate(n)  # simulate and back propagate
        Update(n, reward, turn)
        i += 1
    return BestUCTChild(node).getState()  # return pos function required


def TreePolicy(node):
    node.getChildren()
    while node.Children:
        if node.notFullyExpanded():
            return Expand(node)
        else:
            node = BestUCTChild(node)
    return node


def Expand(node):
    new_node = node.unexploredChild()
    node.ExploredChildren.append(new_node)
    new_node.parent = node
    new_node.getChildren()
    return new_node


def Simulate(node):
    timeout = Time.time() + 1
    while node.isNotTerminal() and Time.time() < timeout / 4:
        node = node.randomNext()
        node.getChildren()
    return node.state.result()


def Update(node, reward, turn):
    while node is not None:
        node.N += 1
        if turn == reward:
            node.Q += 1  # win +1 loss +0
        node = node.parent  # check this back propagate and code this function in node class


def BestUCTChild(node):
    max_so_far = 0.0
    tbr = node
    for child in node.ExploredChildren:
        val = child.UCTValue()
        if val >= max_so_far:
            max_so_far = val
            tbr = child
    return tbr
