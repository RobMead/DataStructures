""" Representation of a generalised tree with a Tree class using a Node
    sub-class. Includes implementations of breadth first search and depth
    first search which are accessible via the Tree class. """

class Node():
    def __init__(self, val, parent = None, children = None):
        self.val = val
        self.parent = parent
        if children == None:
            self.children = []

    def __iter__(self, q = []):
        # Yield node value then look at children.
        yield self.val

        for child in self.children:
            for item in child:
                yield item

    def _bfs(self, q=[]):
        """Implementation of breadth first search"""

        # Yield node value then look at children.
        yield self.val

        if self.children != []:
            # Add children of current node to list q to look at later.
            q.extend([child for child in self.children])

        # Visit the nodes at the front of the queue which represent the nodes
        # on the current level of the graph.
        if q != []:
            for item in q.pop(0)._bfs():
                yield item

    def _dfs(self, result=[]):
        # Visit current node.
        result.append(self.val)

        # Iterate on children of current node.
        if self.children != []:
            for child in self.children:
                child._dfs()

        return result

class MyTree(object):
    def __init__(self, root = None):
        self.root = Node(root)

    def insert(self, val, parent):
        val = Node(val, parent=parent)
        parent.children.append(val)

    def __repr__(self):
        """ DFS as representation """
        return str(list(iter(self)))

    def bfs(self):
        """ Implementation of breadth first search"""
        return self.root._bfs()

    def dfs(self):
        """ Depth first search withou using any iteration """
        return self.root._dfs()

    def __iter__(self):
        """ Depth first search as the iterator """
        return iter(self.root)

t = MyTree('root')
t.insert('root child 1', t.root)
t.insert('root child 2', t.root)
t.insert("root child 1's child", t.root.children[0])
t.insert("root child 1's second child", t.root.children[0])
t.insert("root child 2's child", t.root.children[1])
