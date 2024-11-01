class Node:
    def __init__(self, l = 0, r = 0):
        self.sum = 0
        self.lchild = None
        self.rchild = None
        self.l = l
        self.r = r


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr = nums
        self.root = Node()
        self.tree = self.build(self.root ,0, self.n - 1)

    def build(self,node, left , right):
        #bounds
        node.l = left
        node.r = right
        
        if left == right:  # leaf node
            node.sum = self.arr[left]
            return node

        mid = (left + right) // 2
        node.lchild = self.build(Node(),left, mid)
        node.rchild = self.build(Node(),mid + 1, right)

        node.sum = node.lchild.sum + node.rchild.sum
        return node

    def update(self, index: int, val: int) -> None:
        def update_node(node, index, val):
            if node.l == node.r:  
                node.sum = val
                return

            mid = (node.l + node.r) // 2
            if index <= mid:
                update_node(node.lchild, index, val)  
            else:
                update_node(node.rchild, index, val)  
            node.sum = node.lchild.sum + node.rchild.sum

        update_node(self.root, index, val)


    def sumRange(self, left: int, right: int) -> int:
        def summRange(node,left,right):
            if node.l >= left and node.r <= right:
                return node.sum
            
            mid = (node.r + node.l) // 2
            if right <= mid:
                return summRange(node.lchild,left,right)

            elif left > mid:
                return summRange(node.rchild,left,right)
            
            else:
                return summRange(node.lchild,left,right) + summRange(node.rchild,left,right)

        return summRange(self.root,left,right)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)