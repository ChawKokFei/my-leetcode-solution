from collections import deque
from collections import defaultdict


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # Using breadth first search, a graph is constructed
        # the lowest number of steps required to reach the
        # destination is simply the layer of the graph explored
        #
        # dfs is not used because it has worse performance
        #
        # visited hashmap stores the visited nodes
        # queue store the sequence of nodes to visit
        # currentQueueLen is to restrict the algorithm to
        # only visit nodes in the current level
        # steps is the number of steps required to reach the destination
        # targetIndex is the index of the destination
        # currentIndex is the index of the current visiting node
        # valueAndIndices is a hashmap that map value to its
        # indices (for jump -> j where: arr[i] == arr[j] and i != j.)

        valueAndIndices = defaultdict(list)
        visited = {}

        if len(arr) <= 1:
            return 0

        for i, value in enumerate(arr):
            valueAndIndices[value].append(i)
            visited[i] = False

        steps = 0
        targetIndex = len(arr) - 1
        queue = deque()
        queue.append(0)
        visited[0] = True
        currentIndex = 0

        while len(queue) != 0:
            currentQueueLen = len(queue)
            while currentQueueLen > 0:
                currentIndex = queue.popleft()
                visited[currentIndex] = True

                if currentIndex == targetIndex:
                    return steps

                previousAdjIndex = currentIndex - 1
                nextAdjIndex = currentIndex + 1

                if previousAdjIndex >= 0 and not visited[previousAdjIndex]:
                    queue.append(previousAdjIndex)

                if nextAdjIndex < targetIndex + 1 and not visited[nextAdjIndex]:
                    queue.append(nextAdjIndex)

                for index in valueAndIndices[arr[currentIndex]]:
                    if not visited[index]:
                        queue.append(index)

                # clear the list to prevent redundant search
                # since when any of the index for the value
                # is met, all the indices will already be
                # enqueued
                # https://leetcode.com/problems/jump-game-iv/solutions/3257792/C++-oror-Simple-BFS-oror-Reason-to-clear-the-map-explained-with-image/
                valueAndIndices[arr[currentIndex]].clear()

                currentQueueLen -= 1
            steps += 1

        return -1
