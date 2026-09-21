class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []

        def dfs(node):
            if not node:
                result.append("#")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = iter(data.split(","))

        def dfs():
            val = next(values)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()