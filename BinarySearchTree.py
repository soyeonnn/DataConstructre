class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None


def print_inorder(node):
    """주어진 노드를 in-order 로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # root 노드부터 데이터를 비교하면서 저장할 위치를 찾는다
        compare_node = self.root
        prev_node = self.root
        switch = True
        while compare_node is not None:
            if compare_node.data > data:
                prev_node = compare_node
                compare_node = compare_node.left_child
                switch = True
            else:
                prev_node = compare_node
                compare_node = compare_node.right_child
                switch = False

        # 찾은 위치에 새로운 노드를 저장
        if switch:
            prev_node.left_child = new_node
        else:
            prev_node.right_child = new_node

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order 로 출력한다


# 비어 있는 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()