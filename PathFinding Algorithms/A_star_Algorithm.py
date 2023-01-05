class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + "-" + str(col)
        self.row = row
        self.col = col
        self.value = value
        self.g_score = float("inf")
        self.f_score = float("inf")
        self.previous = None


def aStarAlgo(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    # print(nodes[1][1].value)
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]
    startNode.g_score = 0
    startNode.f_score = startNode.g_score + calculateHeuristic(startNode, endNode)
    # print(startNode.f_score)

    # Now getting the MinHeap
    nodesToVisit = MinHeap([startNode])


def calculateHeuristic(startNode, endNode):
    # Here we are using Manhattan Distance for calculating heuristic
    a = startNode.row
    b = startNode.col
    c = endNode.row
    d = endNode.col
    dist = abs(c - a) + abs(d - b)
    return dist


# A function to initialize nodes of a graph with more details needed --
# -- as in class Node
def initializeNodes(graph):
    nodes = []

    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))

    return nodes


# MinHeap Class
class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each node is at
        self.nodePositionsInHeap = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if (
                childTwoIdx != -1
                and heap[childTwoIdx].f_score < heap[childOneIdx].f_score
            ):
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap].f_score < heap[currentIdx].f_score:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx].f_score < heap[parentIdx].f_score:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def remove(self):
        if self.isEmpty():
            return

        self.swap(0, len(self.heap) - 1, self.heap)
        node = self.heap.pop()
        del self.nodePositionsInHeap[node.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return node

    def insert(self, node):
        self.heap.append(node)
        self.nodePositionsInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodePositionsInHeap[heap[i].id] = j
        self.nodePositionsInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodePositionsInHeap

    def update(self, node):
        self.siftUp(self.nodePositionsInHeap[node.id], self.heap)


if __name__ == "__main__":
    grid = [
        [1, "S", 1, 1, 1],
        [1, "#", "#", "#", 1],
        [1, 1, 1, 1, 1],
        ["#", 1, "#", "#", "#"],
        [1, 1, 1, "E", 1],
    ]
    startRow = 0
    startCol = 1
    endRow = 4
    endCol = 3
    aStarAlgo(startRow, startCol, endRow, endCol, grid)
