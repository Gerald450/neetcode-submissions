# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        input: root
        output: right side view[int]

        edge: empty root

        plan:
        use bfs
        at every level append the last num
        '''
        from collections import deque
        if not root:
            return []
        otp = []

        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            otp.append(node.val)
        

        return otp

        '''
        q = []
        node = 1
        
        '''









        