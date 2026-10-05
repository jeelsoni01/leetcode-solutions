class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True

            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces