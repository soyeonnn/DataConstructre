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

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            # 지우려는 노드가 root 노드일 때
            if self.root is node_to_delete:
                self.root = None
            else:  # 일반적인 경우
                if node_to_delete is parent_node.left_child:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        # 삭제하려는 노드에 오른쪽 자식만 있는 경우
        elif node_to_delete.left_child is None:
            # 삭제하려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 삭제하려는 노드가 부모 노드의 오른쪽 자식인 경우
            elif node_to_delete is parent_node.right_child:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            else:  # 삭제하려는 노드가 부모 노드의 왼쪽 자식인 경우
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
        # 삭제하려는 노드에 왼쪽 자식만 있는 경우
        elif node_to_delete.right_child is None:
            # 삭제하려는 노드가 root 노드일 때
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 삭제하려는 노드가 부모 노드의 왼쪽 자식인 경우
            if node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            else:  # 삭제하려는 노드가 부모 노드의 오른쪽 자식인 경우
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            # 지우려는 노드의 successor 받아오기
            successor = self.find_min(node_to_delete.right_child)
            # 삭제하려는 노드 데이터에 successor 데이터 저장
            node_to_delete.data = successor.data
            # successor 삭제
            if successor is successor.parent.left_child:  # successor 노드가 어떤 부모 노드의 왼쪽 자식일 때
                successor.parent.left_child = successor.right_child
            else:  # successor 노드가 삭제하려는 노드의 바로 오른쪽 자식일 때
                successor.parent.right_child = successor.right_child

            if successor.right_child is not None:  # successor 노드가 오른쪽 자식이 있을 떄
                successor.right_child.parent = successor.parent

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        temp_node = node

        while temp_node.left_child is not None:
            temp_node = temp_node.left_child

        return temp_node

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None 을 리턴한다"""
        compare_node = self.root

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while compare_node is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if compare_node.data == data:
                return compare_node
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            elif compare_node.data > data:
                compare_node = compare_node.left_child
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            else:
                compare_node = compare_node.right_child

    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
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
            new_node.parent = prev_node
            prev_node.left_child = new_node
        else:
            new_node.parent = prev_node
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

# 자식이 두 개 다 있는 노드 삭제
bst.delete(7)
bst.delete(11)

bst.print_sorted_tree()